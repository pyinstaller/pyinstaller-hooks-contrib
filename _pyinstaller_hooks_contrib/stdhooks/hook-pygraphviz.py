# ------------------------------------------------------------------
# Copyright (c) 2021 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------
import os
import pathlib

from PyInstaller import compat, isolated
from PyInstaller.depend import bindepend
from PyInstaller.utils.hooks import get_module_file_attribute, is_module_satisfies, logger


def _find_graphviz_programs(is_pygraphviz2):
    # Collect graphviz programs that might be called from `pygaphviz.agraph.AGraph`
    # In system installations on macOS and Linux, several of these are commonly symbolic links to a single executable.
    if is_pygraphviz2:
        # https://github.com/pygraphviz/pygraphviz/blob/pygraphviz-2.0/pygraphviz/agraph.py#L1334-L1343
        program_names = (
            "gc",
            "acyclic",
            "gvpr",
            "gvcolor",
            "ccomps",
            "sccmap",
            "tred",
            "unflatten",
        )
        logger.info("hook-pygraphviz: collecting graphviz executables for pygraphviz >= 2.0...")
    else:
        # https://github.com/pygraphviz/pygraphviz/blob/pygraphviz-1.14/pygraphviz/agraph.py#L1330-L1348
        program_names = (
            "neato",
            "dot",
            "twopi",
            "circo",
            "fdp",
            "nop",
            "osage",
            "patchwork",
            "gc",
            "acyclic",
            "gvpr",
            "gvcolor",
            "ccomps",
            "sccmap",
            "tred",
            "sfdp",
            "unflatten",
        )
        logger.info("hook-pygraphviz: collecting graphviz executables for pygraphviz < 2.0...")

    @isolated.decorate
    def _get_executables_info(program_names):
        import pathlib

        import pygraphviz

        # Check if pygraphviz/bin directory exists
        try:
            import pygraphviz.bin
            bin_dir = pygraphviz.bin.__path__[0]
            bin_dir = pathlib.Path(bin_dir).resolve()
        except ImportError:
            bin_dir = None

        # Resolve every program using pygraphviz's own resolver, and determine if executable is bundled with package
        # (PyPI wheel) or taken from system.
        program_info = {}
        g = pygraphviz.agraph.AGraph()
        for program_name in program_names:
            try:
                program_executable = g._get_prog(program_name)
            except Exception:
                continue

            program_path = pathlib.Path(program_executable).resolve()
            is_bundled = bin_dir and bin_dir in program_path.parents

            program_info[program_name] = program_executable, is_bundled

        return program_info

    executables_info = _get_executables_info(program_names)
    if not executables_info:
        logger.warning("hook-pygraphviz: no graphviz program executable was discovered!")
        return []

    # Display info
    for program_name in program_names:
        info = executables_info.get(program_name, None)
        if info is None:
            logger.debug("hook-pygraphviz: %r: not found!", program_name)
        else:
            program_path, is_bundled = info
            logger.debug(
                "hook-pygraphviz: %r [%s]: %r", program_name, 'bundled' if is_bundled else 'system', program_path
            )

    # Construct binaries list and check that all programs are collected from the same location
    binaries = []

    program_locations = set()
    program_bundled = []

    for program_name, (program_path, is_bundled) in executables_info.items():
        binaries.append((program_path, os.path.join('pygraphviz', 'bin') if is_bundled else '.'))

        # Validation
        program_location = pathlib.Path(program_path).parent
        program_locations.add(program_location)
        program_bundled.append(is_bundled)

    if len(program_locations) != 1:
        raise SystemExit(
            "ERROR: collection of graphviz programs from multiple locations is not supported! "
            f"Location: {sorted(program_locations)}"
        )

    if all(program_bundled):
        logger.info("hook-pygraphviz: graphviz programs were collected from the package/wheel.")
    elif not all(program_bundled):
        logger.info("hook-pygraphviz: graphviz programs were collected from system installation.")
    else:
        raise SystemExit(
            "ERROR: a mixture of bundled and system graphviz programs is not supported!"
        )

    return binaries


def _find_graphviz_shared_library():
    # Get path to pygraphviz._graphviz extension module
    extension_file = pathlib.Path(get_module_file_attribute('pygraphviz._graphviz')).resolve()
    pacakge_directory = extension_file.parent

    # Path to bundled libraries directory used by pygraphviz >= 2.0 wheels:
    #  - Windows: package_directory/../pygraphviz.libs (delvewheel)
    #  - macOS: package_directory/.dylibs (relocate)
    #  - linux: package_directory/../pygraphviz.libs (auditwheel)
    if compat.is_darwin:
        bundled_lib_dir = pacakge_directory / ".dylibs"
    else:
        bundled_lib_dir = pacakge_directory.parent / "pygraphviz.libs"

    # Perform binary dependency analysis on the extension module
    graphviz_lib_candidates = ['cdt', 'gvc', 'cgraph']

    search_paths = [bundled_lib_dir] if bundled_lib_dir.is_dir() else []
    if hasattr(bindepend, 'get_imports'):
        # PyInstaller >= 6.0
        extension_imports = [
            path for name, path in bindepend.get_imports(str(extension_file), search_paths)
            if path is not None
        ]
    else:
        # PyInstaller < 6.0
        extension_imports = bindepend.getImports(str(extension_file))
        # The old getImports() does not perform explicit fullpath resolution; so on Windows, it returns just basenames.
        if compat.is_win:
            extension_imports = [
                bindepend.getfullnameof(name, search_paths) for name in extension_imports
            ]  # NOTE: unresolved paths will be empty and discarded below

    graphviz_lib_paths = [
        pathlib.Path(path).resolve() for path in extension_imports
        if any(candidate in os.path.basename(path) for candidate in graphviz_lib_candidates)
    ]

    if not graphviz_lib_paths:
        return None, False

    return graphviz_lib_paths[0], graphviz_lib_paths[0].parent == bundled_lib_dir


binaries = []
datas = []

is_pygraphviz2 = is_module_satisfies("pygraphviz >= 2.0")

# Collect graphviz programs - either from the build system, or from wheel (pygraphviz >= 2.0)
binaries += _find_graphviz_programs(is_pygraphviz2)

# Find the graphviz shared library against which the pygraphviz._graphviz extension is linked
graphviz_library, is_bundled = _find_graphviz_shared_library()
if not graphviz_library:
    logger.warning("hook-pygraphviz: could not determine location of graphviz shared libraries!")
else:
    logger.info(
        "hook-pygraphviz: graphviz shared library: %r (%s)",
        str(graphviz_library),
        'bundled' if is_bundled else 'system',
    )

    if is_bundled:
        if compat.is_win:
            # Just in case, explicitly collect delvewheel directory
            if is_module_satisfies("PyInstaller >= 5.6"):
                from PyInstaller.utils.hooks import collect_delvewheel_libs_directory
                datas, binaries = collect_delvewheel_libs_directory("pygraphviz", datas=datas, binaries=binaries)
            else:
                graphviz_library_dir = graphviz_library.parent
                datas += [(str(graphviz_library_dir), graphviz_library_dir.name)]
        elif compat.is_linux:
            # Suppress creation of top-level symlinks for wheel-bundled libraries.
            # Requires PyInstaller >= 6.11.0; no-op in earlier versions.
            bindepend_symlink_suppression = ['**/pygraphviz.libs/lib*.so*']
    else:
        # System copy; try to collect graphviz plugins
        if compat.is_win:
            # Under Windows, we have several installation variants:
            #  - official installers and builds from https://gitlab.com/graphviz/graphviz/-/releases
            #  - chocolatey
            #  - msys2
            #  - Anaconda
            # In all variants, the plugins and the config file are located in the `bin` directory, next to the program
            # executables and shared libraries.
            plugin_dir = graphviz_library.parent
            plugin_dest_dir = '.'  # Collect into top-level application directory.
            # Official builds and Anaconda use unversioned `gvplugin-{name}.dll` plugin names, while msys2 uses
            # versioned `libgvplugin-{name}-{version}.dll` plugin names (with "lib" prefix).
            plugin_pattern = '*gvplugin*.dll'
        else:
            # Plugins should be located in `graphviz` directory next to shared libraries.
            plugin_dir = graphviz_library.parent / 'graphviz'
            plugin_dest_dir = 'graphviz'  # Collect into graphviz sub-directory.

            if compat.is_darwin:
                plugin_pattern = '*gvplugin*.dylib'
            else:
                # Collect only versioned .so library files (for example, `/lib64/graphviz/libgvplugin_core.so.6` and
                # `/lib64/graphviz/libgvplugin_core.so.6.0.0`; the former usually being a symbolic link to the latter).
                # The unversioned .so library files (such as `lib64/graphviz/libgvplugin_core.so`), if available, are
                # meant for linking (and are usually installed as part of development package).
                plugin_pattern = '*gvplugin*.so.*'

        logger.info("hook-pygraphviz: collecting graphviz plugins from directory: %r", str(plugin_dir))

        binaries += [(str(file), plugin_dest_dir) for file in plugin_dir.glob(plugin_pattern)]
        datas += [(str(file), plugin_dest_dir) for file in plugin_dir.glob("config*")]  # e.g., `config6`
