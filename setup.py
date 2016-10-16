# Copyright 2016 California Institute of Technology.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os.path
from setuptools import find_packages, setup

# Package data
# ------------
_author = 'Lewis John McGibbney'
_author_email = 'lewismc@apache.org'
_classifiers = [
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Intended Audience :: Information Technology',
    'Intended Audience :: Science/Research',
    'Topic :: Scientific/Engineering',
    'Development Status :: 5 - Production/Stable',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Software Development :: Libraries :: Python Modules',
]
_description = 'PO.DAAC Python API'
_download_url = 'http://pypi.python.org/pypi/podaacpy/'
_requirements = ["beautifulsoup4", "future", "requests"]
_keywords = ['dataset', 'granule', 'compliance', 'nasa', 'jpl', 'podaac']
_license = 'Apache License, Version 2.0'
_long_description = 'A python utility library for interacting with NASA JPLs PO.DAAC'
_name = 'podaacpy'
_namespaces = []
_test_suite = 'podaac.tests'
_url = 'https://github.com/lewismc/podaacpy'
_version = '1.4.0'
_zip_safe = False

# Setup Metadata
# --------------


def _read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

_header = '*' * len(_name) + '\n' + _name + '\n' + '*' * len(_name)
_longDescription = '\n\n'.join([
    _header,
    _read('README.rst')
])
open('doc.txt', 'w').write(_longDescription)


setup(
    author=_author,
    author_email=_author_email,
    classifiers=_classifiers,
    description=_description,
    download_url=_download_url,
    include_package_data=True,
    install_requires=_requirements,
    keywords=_keywords,
    license=_license,
    long_description=_long_description,
    name=_name,
    namespace_packages=_namespaces,
    packages=find_packages(),
    test_suite=_test_suite,
    url=_url,
    version=_version,
    zip_safe=_zip_safe,
)
