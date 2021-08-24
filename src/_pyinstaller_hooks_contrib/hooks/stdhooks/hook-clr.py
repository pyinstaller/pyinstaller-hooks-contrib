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
from PyInstaller.compat import is_win, getsitepackages
from PyInstaller.utils.hooks import is_module_satisfies, logger
from pathlib import Path

try:
    from importlib.metadata import files
except ImportError:
    from import_lib.metadata import files

# pythonnet is available for all platforms using .NET and Mono,
# but tested only on Windows using .NET.

if is_win:
    datas = []

    filepaths =  [f for f in files('pythonnet') if 'Python.Runtime.dll' in str(f)]
    if len(filepaths) == 1:
        pyruntime_path = filepaths[0]
        datas = [(pyruntime_path.locate(), pyruntime_path.parent.as_posix())]
    elif len(filepaths) > 1:
        logger.warning('More than one Python.Runtime.dll found in site packages! Cannot resolve.')

    if len(datas) == 0:
        # Fallback to legacy way of finding Python.Runtime dependency
        library = ctypes.util.find_library('Python.Runtime')
        if library:
            datas = [(library, '.')]
            logger.warning('Legacy method of finding Python.Runtime.dll was used!')

    if not datas:
        raise Exception('Python.Runtime.dll not found')
