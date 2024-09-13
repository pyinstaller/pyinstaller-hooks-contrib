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

from PyInstaller.compat import is_darwin, is_linux
from PyInstaller.utils.hooks import copy_metadata, collect_entry_point

if is_darwin:
    backend = 'cocoa'
elif is_linux:
    backend = 'gtk'
else:
    backend = 'winforms'

hiddenimports = [f'toga_{backend}', f'toga_{backend}.factory']

datas = copy_metadata("toga.core")

for ep in ["toga.backends", "setuptools_scm.parse_scm"]:
    datas_, hiddenimports_ = collect_entry_point(ep)
    datas += datas_
    hiddenimports += hiddenimports_
