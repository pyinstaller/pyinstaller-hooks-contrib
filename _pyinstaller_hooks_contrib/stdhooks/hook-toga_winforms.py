# ------------------------------------------------------------------
# Copyright (c) 2024 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------

from PyInstaller.utils.hooks import collect_data_files, collect_dynamic_libs

# Collect DLLs from `toga_winforms/libs/WebView2`.
# TODO: only one of win-arm64, win-x64, win-x86 from `runtimes` sub-directory needs to be collected.
binaries = collect_dynamic_libs('toga_winforms')

# Collect default icon from `resources`, and license/readme from `toga_winforms/libs/WebView2`
datas = collect_data_files('toga_winforms')
