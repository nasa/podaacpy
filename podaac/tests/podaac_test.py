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

from ..podaac import Podaac
from ..podaac_utils import PodaacUtils
import os
import requests
import xml.etree.ElementTree as ET
from nose.tools import assert_raises
import unittest
from future.moves.urllib.error import HTTPError


class test_podaac(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.podaac = Podaac()
        self.podaac_utils = PodaacUtils()

    # test case for the function load_dataset_md()
    def test_dataset_metadata(self):
        dataset_id = 'PODAAC-GHMG2-2PO01'
        dataset_short_name = 'OSDPD-L2P-MSG02'
        dataset_md = self.podaac.dataset_metadata(
            dataset_id, dataset_short_name)
        root = ET.fromstring(dataset_md.encode('utf-8'))
        short_name = root[1][0].attrib

        assert dataset_md != None
        assert str(short_name['id']) == dataset_short_name
        assert_raises(requests.exceptions.HTTPError, self.podaac.dataset_metadata,
                      'PODAAC-GHMG2-2PO01', 'OSDPD-L2P-MSG02', 'is')
        assert_raises(Exception, self.podaac.dataset_metadata,
                      short_name='OSDPD-L2P-MSG02')

    # test case for the fucntion load_granule_md()
    def test_granule_metadata(self):
        dataset_id = 'PODAAC-GHMG2-2PO01'
        dataset_short_name = 'OSDPD-L2P-MSG02'
        granule_name = '20120912-MSG02-OSDPD-L2P-MSG02_0200Z-v01.nc'
        granule_md = self.podaac.granule_metadata(
            dataset_id, dataset_short_name, granule_name)
        root = ET.fromstring(granule_md.encode('utf-8'))
        short_name = root[1][0].attrib

        assert granule_md != None
        assert str(short_name['id']) == dataset_short_name
        assert_raises(requests.exceptions.HTTPError,
                      self.podaac.granule_metadata, dataset_id='PODAAC', format='is')
        assert_raises(Exception,
                      self.podaac.granule_metadata, format='is')

    # test case for the function load_last24hours_datacasting_granule_md()
    def test_load_last24hours_datacasting_granule_md(self):
        dataset_id = 'PODAAC-ASOP2-25X01'
        dataset_short_name = 'ASCATA-L2-25km'
        format = 'datacasting'
        items_per_page = 10
        granule_md = self.podaac.load_last24hours_datacasting_granule_md(
            dataset_id, dataset_short_name, format, items_per_page)
        root = ET.fromstring(granule_md.encode('utf-8'))
        dataset_id_ = root[0][3].text

        assert granule_md != None
        assert dataset_id_ == dataset_id
        assert_raises(requests.exceptions.HTTPError, self.podaac.load_last24hours_datacasting_granule_md,
                      'PODAAC-ASOP2-25X01', 'ASCATA-L2-25km', format='iso')
        assert_raises(Exception, self.podaac.load_last24hours_datacasting_granule_md,
                      short_name='ASCATA-L2-25km', format='iso')

    # test case for the function load_dataset_variables
    def test_dataset_variable(self):
        dataset_id = 'PODAAC-ASOP2-25X01'
        dataset_variables = self.podaac.dataset_variables(dataset_id)

        assert_raises(requests.exceptions.HTTPError,
                      self.podaac.dataset_variables, dataset_id='PODAAC')

    # test case for the function search_dataset()
    def test_dataset_search(self):
        format = 'atom'
        items_per_page = '400'
        datasets = self.podaac.dataset_search(
            format=format, items_per_page=items_per_page)
        root = ET.fromstring(datasets.encode('utf-8'))
        service_name = "PO.DAAC Dataset Search Service"
        test_service_name = root[3][0].text.split('\t')[3][:-1]

        assert datasets != None
        assert test_service_name == service_name
        assert_raises(requests.exceptions.HTTPError,
                      self.podaac.dataset_search, format='iso')

    # test case for the function search_granule()
    def test_granule_search(self):
        test_dataset_id = 'PODAAC-ASOP2-25X01'
        start_time = '2013-01-01T01:30:00Z'
        end_time = '2014-01-01T00:00:00Z'
        bbox = '-45,-45,45,45'
        start_index = '1'
        format = 'atom'
        granules = self.podaac.granule_search(
            dataset_id=test_dataset_id, start_time=start_time, end_time=end_time, bbox=bbox, start_index=start_index, format=format)
        root = ET.fromstring(granules.encode('utf-8'))
        dataset_id = root.find('{http://www.w3.org/2005/Atom}entry').find(
            '{http://podaac.jpl.nasa.gov/opensearch/}datasetId').text.split('\t')[3]

        assert granules != None
        assert test_dataset_id == dataset_id
        assert_raises(requests.exceptions.HTTPError,
                      self.podaac.granule_search, dataset_id='PODAAC', format='html')
        assert_raises(Exception,
                      self.podaac.granule_search, format='html')

    # test case for the function granule_preview()
    def test_granule_preview(self):
        dataset_id = 'PODAAC-ASOP2-25X01'
        image_variable = 'wind_speed'
        path = os.path.dirname(os.path.abspath(__file__))
        image_data = self.podaac.granule_preview(
            dataset_id=dataset_id, image_variable=image_variable, path=path)

        assert image_data != None

        path = os.path.join(os.path.dirname(__file__),
                            dataset_id + '.png')
        os.remove(path)
        assert_raises(Exception,
                      self.podaac.granule_preview, image_variable='hello')
        assert_raises(HTTPError,
                      self.podaac.granule_preview,
                      dataset_id='PODAAC-ASOP2-25X01', image_variable='hello')

    # test case for the function granule_subset
    def test_granule_subset(self):
        path = os.path.dirname(os.path.abspath(__file__)) + "/test.json"
        subset_token = self.podaac.granule_subset(input_file_path=path)

        assert subset_token != ''

    # test case for the function subset_status
    def test_subset_status(self):
        test_status = "unknown"
        token_1 = "a"
        status_1 = self.podaac.subset_status(token=token_1)
        token_2 = "012"
        status_2 = self.podaac.subset_status(token=token_2)

        assert test_status == status_1
        assert test_status == status_2

    # test case for the function extract_l4_granule()
    def test_extract_l4_granule(self):
        dataset_id = 'PODAAC-GHCMC-4FM02'
        test_format = '.nc'
        path = os.path.dirname(os.path.abspath(__file__))
        granule_name = self.podaac.extract_l4_granule(
            dataset_id, path)
        length = len(granule_name)
        format = granule_name[length - 3:length]

        assert granule_name != None
        assert format == test_format
        assert_raises(Exception, self.podaac.extract_l4_granule,
                      dataset_id='ABCDEF')

        path = os.path.join(os.path.dirname(__file__), granule_name)
        os.remove(path)

    # test case for the function list_available_granule_search_dataset_ids()
    def test_list_available_granule_search_dataset_ids(self):
        data = self.podaac_utils.list_available_granule_search_dataset_ids()

        assert data != None
        assert type(data) is list
        assert len(data) != 0

    # test case for the function
    # list_available_granule_search_dataset_short_names()
    def test_list_available_granule_search_dataset_short_names(self):
        data = self.podaac_utils.list_available_granule_search_dataset_short_names()

        assert data != None
        assert type(data) is list
        assert len(data) != 0

    # test case for the function
    # list_available_granule_search_level2_dataset_ids()
    def test_list_available_granule_search_level2_dataset_ids(self):
        data = self.podaac_utils.list_available_granule_search_level2_dataset_ids()

        assert data != None
        assert type(data) is list
        assert len(data) != 0

    # test case for the function
    # list_available_granule_search_level2_dataset_short_names()
    def test_list_available_granule_search_level2_dataset_short_names(self):
        data = self.podaac_utils.list_available_granule_search_level2_dataset_short_names()

        assert data != None
        assert type(data) is list
        assert len(data) != 0

    # test case for the function list_available_extract_granule_dataset_ids()
    def test_list_available_extract_granule_dataset_ids(self):
        data = self.podaac_utils.list_available_extract_granule_dataset_ids()

        assert data != None
        assert type(data) is list
        assert len(data) != 0

    # test case for the function
    # list_available_extract_granule_dataset_short_names()
    def test_list_available_extract_granule_dataset_short_names(self):
        data = self.podaac_utils.list_available_extract_granule_dataset_short_names()

        assert data != None
        assert type(data) is list
        assert len(data) != 0
