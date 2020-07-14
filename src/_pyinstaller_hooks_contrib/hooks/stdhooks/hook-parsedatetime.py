#-----------------------------------------------------------------------------
# Copyright (c) 2005-2020, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License (version 2
# or later) with exception for distributing the bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#
# SPDX-License-Identifier: (GPL-2.0-or-later WITH Bootloader-exception)
#-----------------------------------------------------------------------------

"""
Fixes https://github.com/pyinstaller/pyinstaller/issues/4995

Modules under parsedatetime.pdt_locales.* are lazily loaded using __import__.
But they are conviniently listed in parsedatetime.pdt_locales.locales.

Tested on versions:

- 1.1.1
- 1.5
- 2.0
- 2.6 (latest)

"""

from PyInstaller.utils.hooks import exec_statement


locales = exec_statement(
"""
try:
    from parsedatetime.pdt_locales import locales
except ImportError:
    pass
else:
    [print(i) for i in locales]
""")

if len(locales):
    # Older versions were structured and loaded differently so don't need this
    # support.
    hiddenimports = ["parsedatetime.pdt_locales." + i for i in locales.split()]
    assert len(hiddenimports)

