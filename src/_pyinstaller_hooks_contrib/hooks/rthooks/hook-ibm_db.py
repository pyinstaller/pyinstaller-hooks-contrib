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

# runtime hook for pyinstaller and module ibm_db
# For Microsoft-Windows, add_dll_directory for clidriver in bundle.
# Conditionally recreate clidriver environment variables
# for bundled clidriver executables.
#
# For documentation please see
# ...
# This runtime hook works alongside the matching analysis hook
# for ibm_db and shares all of the prerequisites mentioned in the
# analysis hook.
#
# The aim of the hook is to conditionally establish the same
# clidriver environment variables on the target environment
# that were present at the build environment.  The idea is
# that specific environment variables whose names begin with prefix
# DB2 (along with some others)  get recreated on the target
# environment before the bundled python script gets launched.
# The assumption is that the target-environment does not
# have any Db2-client installed already and will instead use
# the bundled clidriver as packaged by the analysis hook-ibm_db.py .
# In particular the changes are conditional in the sense that
# if any of the environment-variables already are defined on
# the target environment then this hook won't change them.
# In other words, only set these DB2* environment variables if they
# are not already set.
# The design is that the analysis hook for ibm_db has created
# a file in the bundled-directory that contains x=y
# tuples without any section-headers, being
# environment variable settings from the source-environment.
# This hook interprets that file to conditionally
# re-establish the same variables on the target.


def _pyi_rthook():
    import os
    import sys
    import configparser
    import itertools
    clidriver_vars_file = sys._MEIPASS + os.sep + ".clidriver_environment"
    for (root, dirs, files) in os.walk(sys._MEIPASS, topdown=True):
        if dirs and "clidriver" in dirs:
            clidriver_bin = root + os.sep + "clidriver" + os.sep + "bin"
            if sys.platform == "linux" and os.path.isdir(clidriver_bin):
                clidriver_lib = root + os.sep + "clidriver" + os.sep + "lib"
                clidriver_libicc = clidriver_lib + os.sep + "icc"
                add_ld_library_path = clidriver_lib + os.pathsep +\
                    clidriver_libicc
                old_ld_library_path = os.environ.get('LD_LIBRARY_PATH', '')
                if old_ld_library_path == '':
                    os.environ['LD_LIBRARY_PATH'] = add_ld_library_path
                else:
                    os.environ['LD_LIBRARY_PATH'] = add_ld_library_path +\
                                                    os.pathsep +\
                                                    old_ld_library_path
            if sys.platform == "win32" and os.path.isdir(clidriver_bin):
                os.add_dll_directory(clidriver_bin)
    if not os.path.isfile(clidriver_vars_file):
        pass
    else:
        cfg = configparser.ConfigParser()
        with open(clidriver_vars_file) as fp:
            cfg.read_file(itertools.chain(['[global]'], fp),
                          source=clidriver_vars_file)
        for key, val in cfg.items('global'):
            ukey = key.upper()
            if ukey in os.environ:
                pass
            else:
                if val != '':
                    os.environ[ukey] = val


_pyi_rthook()
del _pyi_rthook
