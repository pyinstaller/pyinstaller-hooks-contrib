# ------------------------------------------------------------------
# Copyright (c) 2020 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------
#
# Hook for the winloop (windows version of uvloop) package: https://pypi.python.org/pypi/winloop
#
from PyInstaller.utils.hooks import collect_submodules

hiddenimports = collect_submodules('winloop')
