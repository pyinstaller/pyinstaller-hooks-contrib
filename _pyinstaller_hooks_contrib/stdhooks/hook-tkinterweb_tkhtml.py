# ------------------------------------------------------------------
# Copyright (c) 2025 PyInstaller Development Team.
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

# Collect files from 'tkhtml'
datas = collect_data_files('tkinterweb_tkhtml')

# Collect binaries from 'tkhtml'
binaries = collect_dynamic_libs('tkinterweb_tkhtml')
