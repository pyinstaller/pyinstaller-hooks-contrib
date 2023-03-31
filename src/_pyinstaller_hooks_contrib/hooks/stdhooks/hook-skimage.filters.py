# ------------------------------------------------------------------
# Copyright (c) 2021 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE.GPL.txt, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------

from PyInstaller.utils.hooks import is_module_satisfies, collect_submodules

if is_module_satisfies("scikit_image >= 0.19.0"):
    # In scikit-image 0.19.0, `skimage.filters` switched to lazy module loading, so we need to collect all submodules.
    hiddenimports = collect_submodules('skimage.filters', filter=lambda name: name != 'skimage.filters.tests')
elif is_module_satisfies("scikit_image >= 0.18.0"):
    # The following missing module prevents import of skimage.feature with skimage 0.18.x.
    hiddenimports = ['skimage.filters.rank.core_cy_3d', ]
