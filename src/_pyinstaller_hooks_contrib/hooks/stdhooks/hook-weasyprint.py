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
# Tested on version weasyprint 53.4 using Windows 10 and python 3.8
# For weasyprint < 53.0 the required libs are
# libs = [
#     'gobject-2.0', 'libgobject-2.0-0', 'libgobject-2.0.so.0', 'libgobject-2.0.dylib',
#     'pango-1.0', 'libpango-1.0-0', 'libpango-1.0.so.0', 'libpango-1.0.dylib',
#     'pangocairo-1.0', 'libpangocairo-1.0-0', 'libpangocairo-1.0.so.0', 'libpangocairo-1.0.dylib',
#     'fontconfig', 'libfontconfig', 'libfontconfig-1.dll', 'libfontconfig.so.1', 'libfontconfig-1.dylib',
#     'pangoft2-1.0', 'libpangoft2-1.0-0', 'libpangoft2-1.0.so.0', 'libpangoft2-1.0.dylib'
# ]

import ctypes.util
import os
from pathlib import Path

from PyInstaller.depend.utils import _resolveCtypesImports
from PyInstaller.utils.hooks import collect_data_files, logger

datas = collect_data_files('weasyprint')

binaries = []

# NOTE: Update this if weasyprint requires more libraries
libs = [
    'gobject-2.0-0', 'gobject-2.0', 'libgobject-2.0-0', 'libgobject-2.0.so.0', 'libgobject-2.0.dylib',
    'pango-1.0-0', 'pango-1.0', 'libpango-1.0-0', 'libpango-1.0.so.0', 'libpango-1.0.dylib',
    'harfbuzz', 'harfbuzz-0.0', 'libharfbuzz-0', 'libharfbuzz.so.0', 'libharfbuzz.so.0', 'libharfbuzz.0.dylib',
    'fontconfig-1', 'fontconfig', 'libfontconfig', 'libfontconfig-1.dll', 'libfontconfig.so.1', 'libfontconfig-1.dylib',
    'pangoft2-1.0-0', 'pangoft2-1.0', 'libpangoft2-1.0-0', 'libpangoft2-1.0.so.0', 'libpangoft2-1.0.dylib'
]

try:
    lib_basenames = []
    for lib in libs:
        libname = ctypes.util.find_library(lib)
        if libname is not None:
            lib_basenames += [os.path.basename(libname)]
    if lib_basenames:
        resolved_libs = _resolveCtypesImports(lib_basenames)
        for resolved_lib in resolved_libs:
            binaries.append((resolved_lib[1], '.'))
except Exception as e:
    logger.warning("Error while trying to find system-installed depending libraries: %s", e)

if not binaries:
    logger.warning("Depending libraries not found - weasyprint will likely fail to work!")

# fontconfig_path = Path(ctypes.util.find_library('libfontconfig-1'))
# datas += [(str(fontconfig_path.parent.parent / 'etc/fonts'), 'etc/fonts')]