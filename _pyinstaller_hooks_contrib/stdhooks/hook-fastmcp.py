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

# See https://github.com/PrefectHQ/fastmcp/blob/v4.0.4/fastmcp_slim/fastmcp/__init__.py#L35-L38
datas = []
for dist_name in ['fastmcp-slim', 'fastmcp']:
    try:
        datas += copy_metadata(dist_name)
    except Exception:  # support both PyInstaller 6.x and 5.x
        pass
