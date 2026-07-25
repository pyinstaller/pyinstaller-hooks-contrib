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
os_service_types ships the OpenStack service-type authority as a JSON data
file, and ``os_service_types/__init__.py`` calls
``pbr.version.VersionInfo('os-service-types')`` at import time, which reads the
installed distribution metadata.

This hook was tested with os-service-types 1.9.0.
"""

from PyInstaller.utils.hooks import collect_data_files, copy_metadata

datas = copy_metadata('os-service-types')
datas += collect_data_files('os_service_types')
