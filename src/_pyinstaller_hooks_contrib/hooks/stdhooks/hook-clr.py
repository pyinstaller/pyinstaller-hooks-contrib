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


"""
pythonnet requires both clr.pyd and Python.Runtime.dll,
but the latter isn't found by PyInstaller.
"""


import ctypes.util
from PyInstaller.log import logger

try:
    import importlib.metadata as importlib_metadata
except ImportError:
    import importlib_metadata

binaries = []

# Try finding Python.Runtime.dll via distribution's file list
dist_files = importlib_metadata.files('pythonnet')
if dist_files is not None:
    runtime_dll_files = [f for f in dist_files if f.match('Python.Runtime.dll')]
    if len(runtime_dll_files) == 1:
        runtime_dll_file = runtime_dll_files[0]
        binaries = [(runtime_dll_file.locate(), runtime_dll_file.parent.as_posix())]
        logger.debug("hook-clr: Python.Runtime.dll discovered via metadata.")
    elif len(runtime_dll_files) > 1:
        logger.warning("hook-clr: multiple instances of Python.Runtime.dll listed in metadata - cannot resolve.")

# Fall back to the legacy way
if not binaries:
    runtime_dll_file = ctypes.util.find_library('Python.Runtime')
    if runtime_dll_file:
        binaries = [(runtime_dll_file, '.')]
        logger.debug('hook-clr: Python.Runtime.dll discovered via legacy method.')

if not binaries:
    raise Exception('Python.Runtime.dll not found')

# These modules are imported inside Python.Runtime.dll
hiddenimports = ["platform", "warnings"]
