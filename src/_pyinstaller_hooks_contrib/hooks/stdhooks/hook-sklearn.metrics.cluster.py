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

# Tested on Windows 7 64bit with scikit-learn 0.17 and Python 2.7
hiddenimports = ['sklearn.utils.sparsetools._graph_validation',
                 'sklearn.utils.sparsetools._graph_tools',
                 'sklearn.utils.lgamma',
                 'sklearn.utils.weight_vector']
