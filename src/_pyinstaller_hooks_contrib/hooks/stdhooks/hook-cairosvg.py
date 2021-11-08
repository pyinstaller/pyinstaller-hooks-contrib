# ------------------------------------------------------------------
# Copyright (c) 2021 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE.GPL.txt, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------
from ctypes.util import find_library

from PyInstaller.utils.hooks import collect_data_files

datas = collect_data_files('cairosvg')

libs = ['cairo-2', 'cairo', 'libcairo-2']
binaries = []
for lib in libs:
    p = find_library(lib)
    if p is not None:
        binaries += [(find_library(lib), '.')]
