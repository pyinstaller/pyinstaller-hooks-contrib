from PyInstaller.utils.hooks import copy_metadata, collect_data_files
datas = copy_metadata("countryinfo") + collect_data_files("countryinfo")
