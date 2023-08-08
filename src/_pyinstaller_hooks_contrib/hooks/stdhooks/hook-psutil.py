# ------------------------------------------------------------------
# Copyright (c) 2023 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE.GPL.txt, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------
# A fully customizable messagebox for customtkinter!
# (extension/add-on)
# ------------------------------------------------------------------
import os

# see https://github.com/giampaolo/psutil/blob/release-5.9.5/psutil/_common.py#L856
# This will exclude `curses` for os.name == 'nt'
if os.name == 'nt':
    excludedimports = ["curses"]
