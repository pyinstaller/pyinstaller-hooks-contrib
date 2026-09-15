# ------------------------------------------------------------------
# Copyright (c) 2026 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------

# Hook for the fastmcp module: https://github.com/PrefectHQ/fastmcp

from PyInstaller.utils.hooks import copy_metadata

datas = copy_metadata('fastmcp')
