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

from PyInstaller.utils.hooks import copy_metadata

# Try to collect metadata for `mcp`, if available; the version information is required by `sentry_sdk.integrations.mcp`
# to decide on correct patching codepath:
# https://github.com/getsentry/sentry-python/blob/2.70.0/sentry_sdk/integrations/mcp.py#L975-L982
datas = []
try:
    datas += copy_metadata("mcp")
except Exception:  # support both PyInstaller 6.x and 5.x
    pass
