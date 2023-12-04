# ------------------------------------------------------------------
# Copyright (c) 2020 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE.GPL.txt, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------

from PyInstaller.utils.hooks import (
    logger,
    collect_data_files,
    is_module_satisfies,
    collect_dynamic_libs,
    collect_submodules,
    get_package_paths,
)

if is_module_satisfies("PyInstaller >= 6.0"):
    module_collection_mode = "pyz+py"
    warn_on_missing_hiddenimports = False

    datas = collect_data_files(
        "torch",
        excludes=[
            "**/*.h",
            "**/*.hpp",
            "**/*.cuh",
            "**/*.lib",
            "**/*.cpp",
            "**/*.pyi",
            "**/*.cmake",
        ],
    )
    binaries = collect_dynamic_libs("torch")
    hiddenimports = collect_submodules("torch")
else:
    datas = [(get_package_paths("torch")[1], "torch")]

# With torch 2.0.0, PyInstaller's modulegraph analysis hits the recursion limit.
# So, unless the user has already done so, increase it automatically.
if is_module_satisfies("torch >= 2.0.0"):
    import sys

    new_limit = 5000
    if sys.getrecursionlimit() < new_limit:
        logger.info("hook-torch: raising recursion limit to %d", new_limit)
        sys.setrecursionlimit(new_limit)
