# Copyright 2016-2018 California Institute of Technology.
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

from ..oceancolor import OceanColor
import os
import requests
import xml.etree.ElementTree as ET
from nose.tools import assert_raises
import unittest
from future.moves.urllib.error import HTTPError


class TestOceanColor(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.oceancolor = OceanColor()

    # test case for the function file_search()
    def test_file_search(self):
        data = self.oceancolor.file_search(sensor='octs', sdate='1996-11-01', edate='1997-01-01',
                dtype='L3b', add_url='1', results_as_file='1', search='*DAY_CHL*')

        assert data != None
        print(data)
        assert type(data) is type(u'')
        assert len(data) != 0

        assert_raises(Exception, self.oceancolor.file_search, sensor='random')
        assert_raises(Exception, self.oceancolor.file_search, sdate='1996-11-01', edate='1997-01-01',
                dtype='L3b', add_url='1', results_as_file='1', search='*DAY_CHL*')

    # test case for the function get_file(()
    def test_get_file(self):
        url = 'https://oceandata.sci.gsfc.nasa.gov/cgi/getfile/O1996307.L3b_DAY_CHL.nc'
        path = os.path.dirname(os.path.abspath(__file__))
        granule_name = self.oceancolor.get_file(url, path)

        assert granule_name != None
        assert_raises(Exception, self.oceancolor.get_file,
                      url='ABCDEF')

        path = os.path.join(os.path.dirname(__file__), granule_name)
        os.remove(path)
