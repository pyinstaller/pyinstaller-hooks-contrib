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

# Supports python3.8 and higher, pyinstaller 6.8.0 and higher,
#   and python-ibm_db 3.2.3 wheel and higher.
#
# Standard-hook for the python-ibm_db module version 3.2.3 and higher
# Tested with linux x64 and microsoft-windows operating systems.
# No support yet for macos, aix, cygwin, bsd, zlinux...
#
# BIG ASSUMPTION is that you bundle clidriver with your app with pyinstaller
#
# If you do NOT want to bundle clidriver (i.e. your target workstations
#  for your app will already have a clidriver installed and configured
#  then do not use this hook for python ibm_db.
#
# To use this hook, copy it to your workstation for example into
#    the same directory as your python-script that you want to
#    bundle. Use `pyinstaller --additional-hooks-directory=/path/to/directory
#    where /path/to/directory is the the directory containing this hook file.
#
# To get more feedback , use the `--log-level=info` option to pyinstaller.

# TODO
# support directory/file based environment-variables from the list at
#  https://www.ibm.com/docs/en/db2/11.5?topic=variables-supported-environment
# test on cygwin ( clidriver environment)
# add support for the "message 0 could not be retrieved" SQL10007N.
# add support for AIX, bsd, solaris etc.
# add support for hook config from specfile, for db2dsdriver.cfg, certificates
# add support for hook config from specfile, for envt-vars per above
#   ( pass on these env-vars to a runtime hook?)
# add support for hook config, licence-file for clidriver (z/os or i-series)
# add conditional support (automatic detection) for ibm_db_sa, ibm_db_django

import os
import sys
import configparser
import io

from PyInstaller.compat import is_linux, is_win, is_py38
from PyInstaller.utils.hooks import is_module_satisfies
from PyInstaller import log as log


def hook(hook_api):
    hlog = log.getLogger(__name__)
    datafiles = []
    warning_count = 0
    if not is_module_satisfies('ibm_db >= 3.2.3'):
        hlog.warning("hook-ibm_db.py needs ibm_db v3.2.3 or higher")
        warning_count += 1
    else:
        hlog.debug("ibm_db hook: ibm_db version is compatible ")
    if not is_py38:
        hlog.warning("hook-ibm_db.py needs python at least 3.8 or higher")
        warning_count += 1
    else:
        hlog.debug("ibm_db hook: the python version is compatible")
    if not is_module_satisfies('pyinstaller >= 6.8.0'):
        hlog.warning("ibm_db hook: needs pyinstaller at least 6.8.0 or higher")
        warning_count += 1
    else:
        hlog.debug("ibm_db hook: the pyinstaller version is compatible")

    clidriver_path = os.environ.get('DB2_CLI_DRIVER_INSTALL_PATH')
    if clidriver_path is None:
        hlog.debug("ibm_db_hook: DB2_CLI_DRIVER_INSTALL_PATH is unset")
    else:
        log.info("ibm_db hook: DB2_CLI_DRIVER_INSTALL_PATH {clidriver_path}")
    site_pkgs = ""
    for directory in sys.path:
        if 'site-packages' in directory:
            site_pkgs = directory
            hlog.info(f"ibm_db_hook: site_packages {site_pkgs}")
            break
    if site_pkgs == "":
        hlog.warning("ibm_db hook: Cannot find site-packages on sys.path")
        warning_count += 1
    else:
        if not os.path.isdir(site_pkgs):
            hlog.warning("ibm_db hook: Missing directory {site_pkgs)")
            warning_count += 1

    if clidriver_path == "" or clidriver_path is None:
        clidriver_path = os.path.join(site_pkgs, 'clidriver')
        hlog.debug(f"ibm_db hook: checking clidriver at {clidriver_path}")
    if warning_count == 0 and not os.path.isdir(clidriver_path):
        hlog.warning("ibm_db hook: site-packages has no clidriver")
        warning_count += 1
    else:
        hlog.info(f"ibm_db hook: found {clidriver_path}")
    old_path = os.environ.get('PATH')
    if old_path is not None:
        hlog.info(f"ibm_db hook: PATH is {old_path}")
    else:
        hlog.error("ibm_db hook: PATH is unset")
        warning_count += 1
    cliini_path = os.environ.get('CLIINIPATH')
    if cliini_path is None:
        hlog.debug("ibm_db hook: CLIINIPATH variable value is unset")
    else:
        hlog.debug("ibm_db hook: CLIINIPATH variable value {cliini_path}")
        if os.path.isdir(cliini_path):
            cliini_path = cliini_path + os.sep + 'db2cli.ini'
        if os.path.isfile(cliini_path):
            hlog.debug("ibm_db hook: found file {cliini_path}")
            datafiles += [(cliini_path, './clidriver' + os.sep + 'cfg')]
        else:
            hlog.warning("ibm_db hook: missing file {cliini_path}")
            warning_count += 1
    db2dsdriver_cfg_path = os.environ.get('DB2DSDRIVER_CFG_PATH')
    if db2dsdriver_cfg_path is None:
        hlog.debug("ibm_db hook: DB2DSDRIVER_CFG_PATH variable is unset")
    else:
        hlog.debug("ibm_db hook: DB2DSDRIVER_CFG_PATH {db2dsdriver_cfg_path}")
        if os.path.isfile(db2dsdriver_cfg_path):
            datafiles += [(db2dsdriver_cfg_path,
                           './clidriver' + os.sep + 'cfg')]
    # regardless of the operating-system capture any clidriver specific
    # environment variables to a config file, and supply that file as
    # a datafile for bundling, for later interpolation by the runtime
    # hook for ibm_db
    # selected host-specific environment variables for v11.5.9 clidriver are
    # not bundled. Either use defaults or set them manually suitably for
    # the bundled package on the target environment. Examples not bundled:
    # ,'DB2DIAGPATH'  (omitted, will use defaults if bundled)
    # ,'DB2_CLI_DRIVER_INSTALL_PATH' (omitted, handled separately)
    # ,'DB2CLIINIPATH' (omitted, handled separately)
    # ,'DB2_CLIENT_HOSTNAME' (omitted, cannot allow dups, will default)
    clivars = ['DB2ACCOUNT',
               'DB2BIDI',
               'DB2CODEPAGE',
               'DB2GRAPHICUNITCODESERVER',
               'DB2LOCALE',
               'DB2TERRITORY',
               'DB2DOMAINLIST',
               'DB2_FORCE_NLS_CACHE',
               'DB2SORCVBUF',
               'DB2SOSNDBUF',
               'DB2TCP_CLIENT_RCVTIMEOUT',
               'DB2_NO_FORK_CHECK',
               'DB2_ENABLE_LDAP',
               'DB2LDAP_BASEDN',
               'DB2LDAP_CLIENT_PROVIDER',
               'DB2LDAPHOST',
               'DB2LDAP_KEEP_CONNECTION',
               'DB2LDAP_SEARCH_SCOPE',
               'DB2NOEXITLIST',
               'AUTHENTICATION',
               'PROTOCOL',
               'PWDPLUGIN',
               'KRBPLUGIN',
               'ALTHOSTNAME',
               'ALTPORT',
               'INSTANCE',
               'BIDI'
               ]
    found_vars = dict()
    count_vars = 0
    for var in clivars:
        if var in os.environ:
            hlog.debug(f"ibm_db hook: Found clidriver env variable {var}")
            var_value = os.environ[var]
            uvar = var.upper()
            found_vars[uvar] = var_value
            count_vars += 1
    if count_vars == 0:
        hlog.info("ibm_db hook: There are no clidriver env variables defined")
    else:
        hlog.info(f"ibm_db hook: Found {count_vars} CLIDRIVER env variables")
        clidriver_vars = os.path.dirname(os.path.abspath(__file__)) +\
            os.sep + '.clidriver_environment'
        if os.path.isfile(clidriver_vars):
            os.remove(clidriver_vars)
            hlog.debug(f"removed previous {clidriver_vars}")
        buf = io.StringIO()
        ini_file = configparser.ConfigParser()
        for i in found_vars.keys():
            ini_file.set('DEFAULT', i, found_vars[i])
        ini_file.write(buf)
        buf.seek(0)
        next(buf)
        with open(clidriver_vars, 'w') as fd:
            fd.write(buf.read())
        hlog.info(f"ibm_db hook: created file {clidriver_vars}")
        datafiles += [(clidriver_vars, ".")]
        hlog.debug(f"ibm_db hook: Added {clidriver_vars} to datas for bundle")

    if is_linux:
        ibm_db_libs_path = os.path.join(site_pkgs, 'ibm_db.libs')
        if not os.path.isdir(ibm_db_libs_path):
            hlog.warning(f"ibm_db hook: missing {ibm_db_libs_path}")
            warning_count += 1
        else:
            hlog.info(f"ibm_db hook: found {ibm_db_libs_path}")
            binfiles = [(ibm_db_libs_path+'/lib*', 'ibm_db.libs')]
            binfiles += [(clidriver_path+'/lib/*', 'ibm_db.libs')]
            datafiles += [(clidriver_path, './clidriver')]
            if (warning_count == 0):
                hook_api.add_binaries(binfiles)
                hook_api.add_datas(datafiles)
            else:
                hlog.error(f"ibm_db hook: got {warning_count} warnings\
                             please resolve these first. ibm_db is not\
                             bundled until there are no warnings")
    elif is_win:
        if warning_count == 0:
            binfiles = [(clidriver_path, './clidriver')]
            hook_api.add_binaries(binfiles)
            hook_api.add_datas(datafiles)
        else:
            hlog.error(f"ibm_db hook: got {warning_count} warnings\
                             please resolve these first. ibm_db is not\
                             bundled until there are no warnings")

    else:
        hlog.warning("ibm_db hook:  your O/S is not yet supported")
