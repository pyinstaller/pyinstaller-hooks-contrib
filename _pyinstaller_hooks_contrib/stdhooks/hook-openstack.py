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
openstacksdk is imported as ``openstack``.

``openstack/version.py`` calls ``pbr.version.VersionInfo('openstacksdk')`` at
import time, which reads the installed distribution metadata, so the metadata
must be collected or importing the package raises.

``openstack.config`` loads ``config/defaults.json`` and its JSON schemas from
the package directory at run-time, and ``openstack.config.vendors`` globs the
vendor profiles (JSON and YAML) from ``config/vendors/``; a missing vendor
profile is silently ignored, so the whole ``config`` directory is collected.

Service proxies and resource classes live in per-service sub-packages that are
resolved by service type and microversion at run-time, so they are collected as
hidden imports.

This hook was tested with openstacksdk 4.24.0.
"""

from PyInstaller.utils.hooks import collect_data_files, collect_submodules, copy_metadata

datas = copy_metadata('openstacksdk')
datas += collect_data_files('openstack', subdir='config')

hiddenimports = collect_submodules('openstack', filter=lambda name: name != 'openstack.tests')
