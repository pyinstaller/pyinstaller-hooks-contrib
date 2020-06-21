# ------------------------------------------------------------------
# Copyright (c) 2020 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE.GPL.txt, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------
from setuptools import setup, Command
import os
import datetime

DIR = os.path.dirname(__file__)


class BumpVersion(Command):
    """Bump the package version in the source files."""
    description = 'Bump the version in all registered files.'
    user_options = [
        ('major', None,
         'Bump the major (leftmost) version number. If specified, build/minor version numbers will be set to 0.'),
        ('minor', None, 'Bump the minor (middle) version number. If specified, the build NO will be set to 0.'),
        ('build', None, 'Bump the build (rightmost) version number. (Default)')
    ]
    
    def get_version_tuple(self, str_ver):
        return list(int(x) for x in str_ver.split('.'))
    
    def initialize_options(self):
        self.major = False
        self.minor = False
        self.build = True
    
    def finalize_options(self):
        if self.major:
            self.major = True
            self.minor = False
            self.build = False
        elif self.minor:
            self.major = False
            self.minor = True
            self.build = False
        else:
            self.major = False
            self.minor = False
            self.build = True
    
    def run(self):
        import re
        # REGEX:
        #  [0-9]+  - First part of version: [4].0.1
        #  [.][0-9]*  - Second part of version: 4[.0].1
        #  [.]*[0-9]*  - Third - and optional - part of version
        #  [^.]$  - The entire string must not end with a dot
        version_regex = re.compile('[0-9]+[.][0-9]*[.]*[0-9]*[^.]$')
        
        # List of ABSOLUTE file paths of files to bump
        files = [
            os.path.abspath(os.path.join(DIR, 'src/_pyinstaller_hooks_contrib/__init__.py'))
        ]
        for file in files:
            old_file = open(file).readlines()
            changed = False
            
            for i in range(len(old_file)):
                # Get rid of line endings, if they exist
                line = old_file[i].replace('\n', '')
                
                # If the line starts with version, try and bump it
                if line.startswith('__version__'):
                    print('Line {ln} in {file} appears to be a version. Attempting to bump...'.format(ln=i, file=file))
                    line = line.split(' = ')[1].replace(' ', '').replace("'", '')
                    m = version_regex.match(line)
                    if m:
                        # Convert a "valid" version to a tuple of ints
                        ver = self.get_version_tuple(m.string)
                        print(ver)
                        
                        # If the tuple isn't valid - not len(3) - then it's not a valid version
                        if len(ver) not in (2, 3):
                            print('Invalid version number. Skipping...')
                            continue
                        
                        if len(ver) == 3:
                            if self.major:
                                ver[0] += 1
                                ver[1] = 0
                                ver[2] = 0
                                
                            elif self.minor:
                                ver[1] += 1
                                ver[2] = 0
                            else:
                                ver[2] += 1
                        else:
                            if datetime.datetime.now().year != ver[0]:
                                ver[0] = datetime.datetime.now().year
                                ver[1] = 0
                            else:
                                ver[1] += 1
                        
                        ver = '.'.join(str(x) for x in ver)
                        
                        old_file[i] = old_file[i].replace(m.string, ver)
                        print('Version bumped from {} to {}.'.format(m.string, ver))
                        changed = True
                    else:
                        print('No version found - {file}:{ln}'.format(ln=i, file=file))
            
            if changed:
                # Write the changes to the file
                with open(file, 'w') as f:
                    f.writelines(old_file)
                # And print that to the console.
                print('Changes written to {}'.format(file))
                        

setup(
    setup_requires="setuptools >= 30.3.0",
    entry_points={
        'pyinstaller40': [
            'hook-dirs = _pyinstaller_hooks_contrib.hooks:get_hook_dirs',
            'tests = _pyinstaller_hooks_contrib.tests:get_test_dirs'
        ]
    },
    cmdclass={
        'bump': BumpVersion
    },
    long_description_content_type='text/markdown'
)
