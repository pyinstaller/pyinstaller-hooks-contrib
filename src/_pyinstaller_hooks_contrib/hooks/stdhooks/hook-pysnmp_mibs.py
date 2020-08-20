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

# pysnmp_mibs provides MIBS files for pysnmp. It contains MIB files
# '.py' files which are treated as data files and are loaded by [what are they loaded by?]

from PyInstaller.utils.hooks import collect_data_files

datas = collect_data_files('pysnmp_mibs', include_py_files=True)
