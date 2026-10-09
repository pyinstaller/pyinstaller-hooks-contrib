# ------------------------------------------------------------------
# Copyright (c) 2020 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------

# Hook for imageio: http://imageio.github.io/

from PyInstaller.utils.hooks import collect_data_files, collect_submodules, copy_metadata, is_module_satisfies

datas = collect_data_files('imageio', subdir="resources")

# ImageIO >= 2.37.2 reads its version from the distribution metadata at import time.
if is_module_satisfies('imageio >= 2.37.2'):
    datas += copy_metadata('imageio')

# imageio plugins are imported lazily since ImageIO version 2.11.0.
# They are very light-weight, so we can safely include all of them.
hiddenimports = collect_submodules('imageio.plugins')
