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

# Tested on Windows 10 1809 64bit with scikit-learn 0.22.1 and Python 3.7
hiddenimports = ['sklearn.neighbors.typedefs',
                 'sklearn.utils._cython_blas',
                 'sklearn.neighbors.quad_tree',
                 'sklearn.tree._utils']
