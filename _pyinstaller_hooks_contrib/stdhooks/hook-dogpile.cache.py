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

from PyInstaller.utils.hooks import collect_submodules

# Backends are registered as dotted module paths and loaded by dogpile's
# PluginLoader, so static analysis cannot discover them. Ignore import failures
# for backends whose optional dependencies are not installed.
hiddenimports = collect_submodules('dogpile.cache.backends', on_error='ignore')
