# Azurerm is a lite api to microsoft azure.
# Azurerm is using pkg_resources internally which is not supported by py-installer.
# This hook will collect the module metadata.
# Tested with Azurerm 0.10.0
from PyInstaller.utils.hooks import copy_metadata

datas = copy_metadata("azurerm")
