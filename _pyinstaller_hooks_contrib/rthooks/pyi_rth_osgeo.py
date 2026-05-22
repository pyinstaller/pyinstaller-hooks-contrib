#-----------------------------------------------------------------------------
# Copyright (c) 2015-2020, PyInstaller Development Team.
#
# This file is distributed under the terms of the Apache License 2.0
#
# The full license is available in LICENSE, distributed with
# this software.
#
# SPDX-License-Identifier: Apache-2.0
#-----------------------------------------------------------------------------

import os
import sys

# Installing `osgeo` Conda packages requires to set `GDAL_DATA`

is_win = sys.platform.startswith('win')
if is_win:

    gdal_data = os.path.join(sys._MEIPASS, 'data', 'gdal')
    if not os.path.exists(gdal_data):

        gdal_data = os.path.join(sys._MEIPASS, 'Library', 'share', 'gdal')
        if not os.path.exists(gdal_data):
            # last attempt, check if one of the required files is in the
            # generic folder Library/data.
            generic_folder = os.path.join(sys._MEIPASS, 'Library', 'data')
            # 'gcs.csv' is included by gdal <= 2.4.4
            # 'gdalicon.png' is included by gdal >= 2.4.4 (and presumeably earlier)
            if os.path.exists(os.path.join(generic_folder, 'gcs.csv')) or \
                    os.path.exists(os.path.join(generic_folder, 'gdalicon.png')):
                gdal_data = generic_folder

else:
    gdal_data = os.path.join(sys._MEIPASS, 'share', 'gdal')

if os.path.exists(gdal_data):
    os.environ['GDAL_DATA'] = gdal_data
