"""
pysoundfile:
https://github.com/bastibe/SoundFile
"""

import os
from PyInstaller.utils.hooks import get_package_paths

# get path of soundfile
sfp = get_package_paths('soundfile')

# add the binaries
bins = os.path.join(sfp[0], "_soundfile_data")
binaries = []
datas = [(bins, "_soundfile_data")]
