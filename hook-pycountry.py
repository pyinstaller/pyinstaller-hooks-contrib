from PyInstaller.utils.hooks import copy_metadata, collect_data_files
datas = copy_metadata("pycountry") + collect_data_files("pycountry")