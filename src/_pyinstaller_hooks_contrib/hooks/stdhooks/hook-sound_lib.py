"""
sound_lib: http://hg.q-continuum.net/sound_lib
"""

from PyInstaller.utils.hooks import collect_dynamic_libs

binaries = []
datas = collect_dynamic_libs('sound_lib')
