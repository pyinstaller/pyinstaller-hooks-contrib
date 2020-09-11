"""
accessible_output2: http://hg.q-continuum.net/accessible_output2
"""

from PyInstaller.utils.hooks import collect_dynamic_libs

binaries = []
datas = collect_dynamic_libs('accessible_output2')
