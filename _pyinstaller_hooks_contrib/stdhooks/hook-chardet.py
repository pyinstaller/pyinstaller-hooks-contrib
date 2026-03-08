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

from PyInstaller.utils.hooks import is_module_satisfies

# Starting with v7.0.0, we need to collect mypy extension, and the data files from chardet/models
if is_module_satisfies("chardet >= 7.0.0"):
    from PyInstaller.utils.hooks import collect_data_files
    from _pyinstaller_hooks_contrib.utils.mypy import find_mypyc_module_for_dist

    hiddenimports = find_mypyc_module_for_dist('chardet')
    datas = collect_data_files('chardet')
