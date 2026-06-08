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

from PyInstaller.utils.hooks import collect_data_files, collect_submodules, is_module_satisfies

datas = collect_data_files('dash')

# dash 4.2.0 introduced `dash.backends` with programmatically imported backend modules.
hiddenimports = []
if is_module_satisfies('dash>=4.2.0'):
    hiddenimports += collect_submodules('dash.backends')
