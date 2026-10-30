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

from PyInstaller.compat import importlib_metadata
from PyInstaller.utils.hooks import copy_metadata

# Both webrtcvad and webrtcvad-wheels install the webrtcvad module, but its
# version lookup uses the metadata of the distribution that provided it.
datas = []
for distribution in importlib_metadata.packages_distributions().get('webrtcvad', []):
    datas += copy_metadata(distribution)
