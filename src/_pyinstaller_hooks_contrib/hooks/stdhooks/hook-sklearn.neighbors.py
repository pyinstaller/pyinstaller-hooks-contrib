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

hiddenimports = [
    'sklearn.neighbors._typedefs',
    'sklearn.neighbors._quad_tree',
    'sklearn.tree._criterion',  # must be added here, not in sklearn.tree hook
]
