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
"""
keystoneauth1 is the authentication library used by openstacksdk and the
OpenStack client tools.

Auth plugins are discovered through stevedore, using the
``keystoneauth1.plugin`` entry-point namespace, so the distribution metadata is
required and the plugin modules are not reachable by static analysis.

The test suite and the ``keystoneauth1.fixture`` test-support package are
skipped: they are not used at run-time, and ``keystoneauth1.fixture`` requires
the optional ``fixtures`` library.

This hook was tested with keystoneauth1 5.19.0.
"""

from PyInstaller.utils.hooks import collect_submodules, copy_metadata

_EXCLUDED = ('keystoneauth1.tests', 'keystoneauth1.fixture')

datas = copy_metadata('keystoneauth1')

hiddenimports = collect_submodules('keystoneauth1', filter=lambda name: name not in _EXCLUDED)
