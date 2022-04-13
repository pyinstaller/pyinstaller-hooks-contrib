# ------------------------------------------------------------------
# Copyright (c) 2020 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE.GPL.txt, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------

# Hook for weasyprint: https://pypi.python.org/pypi/WeasyPrint
# Tested on version weasyprint 0.24 using Windows 10 and python 3.9

import os

from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.compat import is_win

datas, binaries = [], []
datas += collect_data_files('weasyprint')

# the dll_directories code is equivalent to the one in weasyprint/text/ffi.py
if is_win:
    dll_directories = os.getenv(
        'WEASYPRINT_DLL_DIRECTORIES',
        'C:\\Program Files\\GTK3-Runtime Win64\\bin').split(';')

    for dll_directory in dll_directories:
        if os.path.isdir(dll_directory):
            binaries.append((os.path.join(dll_directory, '*.dll'), '.'))
        if os.path.isdir(os.path.join(os.path.dirname(dll_directory), 'etc')):
            datas.append((os.path.join(os.path.dirname(dll_directory), 'etc'), 'etc'))
