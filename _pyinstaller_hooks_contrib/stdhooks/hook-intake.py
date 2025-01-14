# ------------------------------------------------------------------
# Copyright (c) 2024 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------

from PyInstaller.utils.hooks import copy_metadata, collect_submodules, is_module_satisfies

hiddenimports = collect_submodules('intake')
datas = copy_metadata('intake')

# Attention: Since PyInstaller basically process the modules that are
# imported in the code, and in the case of intake, when the plugin's
# drivers are installed, they are automatically get used via the main
# intake module. So, we need to check if the plugin's driver is installed
# and then process it in PyInstaller construction procedure to get the
# hidden imports and datas of the plugin.

# List of all intake available plugins with their
# module names on https://github.com/orgs/intake/repositories?type=all
OPTIONAL_PLUGINS = [
    'intake_xarray',
    'intake_parquet',
    'intake_sql',
    'intake_elasticsearch',
    'intake_spark',
    'intake_accumulo',
    'intake_solr',
    'intake_geopandas',
    'intake_mongo',
    'intake_google_analytics',
    'intake_streamz',
    'intake_postgres',
    'intake_hbase',
    'intake_sroka',
    'intake_avro',
    'intake_esm',
    'intake_snappy',
    'intake_odbc',
    'intake_netflow',
    'intake_pcap',
    'intake_astro',
    'intake_splunk',
    'intake_dremio',
    'intake_duckdb'
]

for plugin in OPTIONAL_PLUGINS:
    if is_module_satisfies(plugin):
        metadata_datas = copy_metadata(plugin)
        if metadata_datas:
            datas.extend(metadata_datas)
        hiddenimports.extend(collect_submodules(plugin))
