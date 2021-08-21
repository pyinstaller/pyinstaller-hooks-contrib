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
from PyInstaller.utils.hooks import is_module_satisfies
from pathlib import Path

# pythonnet is available for all platforms using .NET and Mono,
# but tested only on Windows using .NET.

if is_win:
    pyruntime = 'Python.Runtime'
    library = ctypes.util.find_library(pyruntime)
    datas = []
    if library:
        datas = [(library, '.')]
    else:
        # find Python.Runtime.dll in pip-installed pythonnet package
        if is_module_satisfies('pythonnet < 3.0.0'):
            pyruntime_path_prefix = ''
        else:
            pyruntime_path_prefix = 'pythonnet/runtime/'

        for sitepack in [Path(s).resolve() for s in getsitepackages()]:
            library = sitepack / f'{pyruntime_path_prefix}{pyruntime}.dll'
            if library.exists():
                datas = [(library, f'{pyruntime_path_prefix if not "" else "."}')]
        if not datas:
            raise Exception(pyruntime + ' not found')
