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

from PyInstaller.utils.hooks import collect_dynamic_libs

# include versioned .so files as well
binaries = collect_dynamic_libs('torch', py_dylib_patterns=['*.dll', '*.dylib', 'lib*.so', 'lib*.so.*'])
