# ------------------------------------------------------------------
# Copyright (c) 2026 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------

from PyInstaller.utils.hooks import (
    collect_data_files,
    collect_submodules,
    copy_metadata,
)

datas = copy_metadata("adbc_driver_manager")
# include_py_files=True is required: collect_data_files excludes .py files by default
datas += collect_data_files(
    "adbc_driver_manager",
    include_py_files=True,
    includes=["_static_version.py"],
)
hiddenimports = collect_submodules("adbc_driver_manager")
