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

from PyInstaller.utils.hooks import collect_all, is_module_satisfies

_ , datas, hiddenimports = collect_all('intake')


# Attention: Since PyInstaller basically process the modules that are 
# imported in the code, and in the case of intake, when the plugin's 
# drivers are installed, they are automatically get used via the main 
# intake module. So, we need to check if the plugin's driver is installed 
# and then process it in PyInstaller construction procedure to get the 
# hidden imports and datas of the plugin.

# List of all intake available plugins with their 
# module names on https://github.com/orgs/intake/repositories?type=all
OPTIONAL_PLUGINS = {
    'intake-xarray': {
        'import_name': 'intake_xarray'
    },
    'intake-parquet': {
        'import_name': 'intake_parquet'
    },
    'intake-sql': {
        'import_name': 'intake_sql'
    },
    'intake-elasticsearch': {
        'import_name': 'intake_elasticsearch'
    },
    'intake-spark': {
        'import_name': 'intake_spark'
    },
    'intake-accumulo': {
        'import_name': 'intake_accumulo'
    },
    'intake-solr': {
        'import_name': 'intake_solr'
    },
    'intake_geopandas': {
        'import_name': 'intake_geopandas'
    },
    'intake-mongo': {
        'import_name': 'intake_mongo'
    },
    'intake-google-analytics': {
        'import_name': 'intake_google_analytics'
    },
    'intake-streamz': {
        'import_name': 'intake_streamz'
    },
    'intake-postgres': {
        'import_name': 'intake_postgres'
    },
    'intake-hbase': {
        'import_name': 'intake_hbase'
    },
    'intake-sroka': {
        'import_name': 'intake_sroka'
    },
    'intake-avro': {
        'import_name': 'intake_avro'
    },
    'intake-esm': {
        'import_name': 'intake_esm'
    },
    'intake-snappy': {
        'import_name': 'intake_snappy'
    },
    'intake-odbc': {
        'import_name': 'intake_odbc'
    },
    'intake-netflow': {
        'import_name': 'intake_netflow'
    },
    'intake-pcap': {
        'import_name': 'intake_pcap'
    },
    'intake-astro': {
        'import_name': 'intake_astro'
    },
    'intake-splunk': {
        'import_name': 'intake_splunk'
    },
    'intake-dremio': {
        'import_name': 'intake_dremio'
    },
    'intake-duckdb': {
        'import_name': 'intake_duckdb'
    }
}

for plugin_info in OPTIONAL_PLUGINS.values():
    if is_module_satisfies(plugin_info['import_name']):
        binaries ,plugin_datas, plugin_imports = collect_all(plugin_info['import_name'])
        datas.extend(plugin_datas)
        hiddenimports.extend(plugin_imports)