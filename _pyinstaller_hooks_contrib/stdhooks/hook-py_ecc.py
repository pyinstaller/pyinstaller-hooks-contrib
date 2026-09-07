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

from PyInstaller.utils.hooks import copy_metadata, is_module_satisfies

# Starting with py-ecc 7.0.0, version information is obtained from metadata.
if is_module_satisfies('py-ecc >= 7.0.0'):
    datas = copy_metadata('py-ecc')
