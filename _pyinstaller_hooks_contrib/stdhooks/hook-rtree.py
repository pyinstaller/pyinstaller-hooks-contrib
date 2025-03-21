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

import pathlib

from PyInstaller import compat
from PyInstaller.utils.hooks import collect_dynamic_libs, get_package_paths
from _pyinstaller_hooks_contrib.compat import get_installer_for_dist


# Query the installer of the `rtree` distribution.
installer = get_installer_for_dist('rtree')

if installer == 'conda':
    from PyInstaller.utils.hooks import conda

    # In Anaconda-packaged `rtree`, `libspatialindex` and `libspatialindex_c` shared libs are packaged in a separate
    # `libspatialindex` package. Collect the libraries into `rtree/lib` sub-directory to simulate PyPI wheel layout.
    binaries = conda.collect_dynamic_libs('libspatialindex', dest='rtree/lib', dependencies=False)
else:
    # pip-installed package. The shared libs are usually placed in `rtree/lib` directory.
    binaries = collect_dynamic_libs('rtree')

    # With rtree >= 1.1.0, Linux PyPI wheels place the shared library in a `Rtree.libs` top-level directory.
    # In rtree 1.4.0, the directory was renamed to `rtree.libs`
    if compat.is_linux:
        _, rtree_dir = get_package_paths('rtree')
        for candidate_dir_name in ('rtree.libs', 'Rtree.libs'):
            rtree_libs_dir = pathlib.Path(rtree_dir).parent / candidate_dir_name
            if not rtree_libs_dir.is_dir():
                continue
            binaries += [
                (str(lib_file), candidate_dir_name) for lib_file in rtree_libs_dir.glob("libspatialindex*.so*")
            ]
