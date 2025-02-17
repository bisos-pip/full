#!/usr/bin/env python

# Template File:  /bisos/apps/defaults/begin/templates/purposed/pyModule/python/setup.py
# Blee Panel: /bisos/git/auth/bxRepos/blee-binders/bisos-core/bisos-pip/bisos.pycs/pipPackaging/_nodeBase_/fullUsagePanel-en.org

# b:py3:pypi:setup/pkgName Arguments  :pkgName "somePkg" :pkgNameSpace "bisos"
####+BEGIN: b:py3:pypi:setup/pkgName :comment "Auto Detected" :pkgName "py3-all" :pkgNameSpace "bisos"

import setuptools
import re

def pkgName():
        return 'bisos.py3-all'

def description():
    ''' Extract title from ./_description.org which is expected to have a #+title: line. '''
    try:
        with open('./_description.org') as file:
            while line := file.readline():
                if match := re.search(r'^#\+title: (.*)',  line.rstrip()):
                    return match.group(1)
            return 'MISSING TITLE in ./_description.org'
    except IOError:
        return  'ERROR: Could not read ./_description.org file.'

def longDescription():
    ''' Read README.rst as a string. '''
    fileName = './README.rst'
    try:
        with open(fileName) as file:
           result = file.read()
        return result
    except IOError:
        return  f'ERROR: Could not read {fileName} file.'

####+END:

# b:py3:pypi:setup/version Arguments  :forSys t :forPyPi t :constant "666"
####+BEGIN: b:py3:pypi:setup/version :comment "Auto Detected"

# ./pypiUploadVer DID NOT exist -- forPypiVersion=0.24 -- forLocalVersion=0.12 -- constant=NA
def pkgVersion():
        return '0.12'

####+END:

# b:py3:pypi:setup/requires :extras ; :requirements "requirements.txt" (bring here requirements.txt)
####+BEGIN: b:py3:pypi:setup/requires :extras () :requirements "requires.outside"

requires = [
'bisos.b',
'bisos.banna',
'bisos.bashStandaloneIcmSeed',
'bisos.basics',
'bisos.binsprep',
'bisos.bootstrap',
'bisos.bpo',
'bisos.bx-bases',
'bisos.bxoGitlab',
'bisos.capability',
'bisos.capSpecs',
'bisos.cmdb',
'bisos.cntnr',
'bisos.common',
'bisos.core',
'bisos.coreDist',
'bisos.crypt',
'bisos.csPlayer',
'bisos.currents',
'bisos.debian',
'bisos.examples',
'bisos.facter',
'bisos.gcipher',
'bisos.githubApi',
'bisos.gossonot',
'bisos.graphviz',
'bisos.lcnt',
'bisos.marmee',
'bisos.mmwsIcm',
'bisos.pals',
'bisos.platform',
'bisos.provision',
'bisos.pycs',
'bisos.qmail',
'bisos.regfps',
'bisos.sbom',
'bisos.siteRegistrars',
'bisos.things',
'bisos.transit',
'bisos.usgAcct',
'bisos.virsh',
]
####+END:


# b:py3:pypi:setup/scripts :comment
####+BEGIN: b:py3:pypi:setup/scripts :comment ""

scripts = [
]
####+END:

# b:py3:pypi:setup/dataFiles :comment
####+BEGIN: b:py3:pypi:setup/dataFiles :comment "Instead of ./MANIFEST.in or in pyproject.toml"

data_files = [
(' ',  ['lh-agpl3-LICENSE.txt', '_description.org', 'README.rst']),
]
####+END:

# :pkgName "--auto--"  --- results in use of name=pkgName(),
####+BEGIN: b:py3:pypi:setup/funcArgs :comment "defaults to --auto--"

setuptools.setup(
    name=pkgName(),  # 'bisos.py3-all'
    version=pkgVersion(),
    packages=setuptools.find_packages(),
    scripts=scripts,
    data_files=data_files,
    include_package_data=True,
    zip_safe=False,
    author='Mohsen Banan',
    author_email='libre@mohsen.1.banan.byname.net',
    maintainer='Mohsen Banan',
    maintainer_email='libre@mohsen.1.banan.byname.net',
    license='AGPL',
    description=description(),
    long_description=longDescription(),
    install_requires=requires,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ]
    )

####+END:
