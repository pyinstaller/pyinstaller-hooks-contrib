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

from PyInstaller.utils.hooks import collect_data_files, copy_metadata

# `procrastinate` reads its SQL files (`sql/queries.sql`, `sql/schema.sql`, and the migrations in
# `sql/migrations`) via `importlib.resources`.
datas = collect_data_files('procrastinate')

# `procrastinate.metadata` reads the distribution metadata via `importlib.metadata` when the top-level
# `procrastinate` package is imported.
datas += copy_metadata('procrastinate')
