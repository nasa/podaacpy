# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ..podaac_data_source import Podaac
from ..podaac_utils import PodaacUtils
import os
import requests
import xml.etree.ElementTree as ET
from nose.tools import assert_raises
import unittest


class test_podaac(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.podaac = Podaac()
        self.podaac_utils = PodaacUtils()

    # test case for the function load_dataset_md()
    def test_load_dataset_md(self):
        dataset_id = 'PODAAC-GHMG2-2PO01'
        dataset_short_name = 'OSDPD-L2P-MSG02'
        dataset_md = self.podaac.load_dataset_md(dataset_id, dataset_short_name)
        root = ET.fromstring(dataset_md.encode('utf-8'))
        short_name = root[1][0].attrib

        assert dataset_md != None
        assert str(short_name['id']) == dataset_short_name
        assert_raises(requests.exceptions.HTTPError, self.podaac.load_dataset_md,
                      'PODAAC-GHMG2-2PO01', 'OSDPD-L2P-MSG02', 'is')

    # test case for the fucntion load_granule_md()
    def test_load_granule_md(self):
        dataset_id = 'PODAAC-GHMG2-2PO01'
        dataset_short_name = 'OSDPD-L2P-MSG02'
        granule_name = '20120912-MSG02-OSDPD-L2P-MSG02_0200Z-v01.nc'
        granule_md = self.podaac.load_granule_md(
            dataset_id, dataset_short_name, granule_name)
        root = ET.fromstring(granule_md.encode('utf-8'))
        short_name = root[1][0].attrib

        assert granule_md != None
        assert str(short_name['id']) == dataset_short_name
        assert_raises(requests.exceptions.HTTPError,
                      self.podaac.load_granule_md, format='is')

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

    # test case for the function search_dataset()
    def test_search_dataset(self):
        format = 'atom'
        items_per_page = '400'
        datasets = self.podaac.search_dataset(
            format=format, items_per_page=items_per_page)
        root = ET.fromstring(datasets.encode('utf-8'))
        service_name = "PO.DAAC Dataset Search Service"
        test_service_name = root[3][0].text.split('\t')[3][:-1]

        assert datasets != None
        assert test_service_name == service_name
        assert_raises(requests.exceptions.HTTPError,
                      self.podaac.search_dataset, format='iso')

    # test case for the function search_granule()
    def test_search_granule(self):
        test_dataset_id = 'PODAAC-ASOP2-25X01'
        start_time = '2013-01-01T01:30:00Z'
        end_time = '2014-01-01T00:00:00Z'
        bbox = '-45,-45,45,45'
        start_index = '1'
        format = 'atom'
        granules = self.podaac.search_granule(
            dataset_id=test_dataset_id, start_time=start_time, end_time=end_time, bbox=bbox, start_index=start_index, format=format)
        root = ET.fromstring(granules.encode('utf-8'))
        dataset_id = root.find('{http://www.w3.org/2005/Atom}entry').find(
            '{http://podaac.jpl.nasa.gov/opensearch/}datasetId').text
        print(dataset_id)

        assert granules != None
        assert test_dataset_id == dataset_id
        assert_raises(requests.exceptions.HTTPError,
                      self.podaac.search_granule, format='html')

    # test case for the function load_image_granule()
    def test_load_image_granule(self):
        dataset_id = 'PODAAC-ASOP2-25X01'
        short_name = 'ASCATA-L2-25km'
        granule_name = 'ascat_20130719_230600_metopa_35024_eps_o_250_2200_ovw.l2.nc'
        bbox = '45,0,180,90'
        srs = 'EPSG:4326'
        height = '300'
        width = '200'
        data = self.podaac.load_image_granule(
            dataset_id, short_name, granule_name, bbox, height, width, srs)
        test_data = data[0].split('/')
        length = len(test_data)

        assert data != None
        assert test_data[length - 1] == dataset_id + '.png'
        assert_raises(Exception, self.podaac.load_image_granule,
                      dataset_id="HBJHKASD")

        path = os.path.join(os.path.dirname(__file__),
                            '../' + dataset_id + '.png')
        os.remove(path)
        path = os.path.join(os.path.dirname(__file__),
                            '../' + "HBJHKASD" + '.png')
        os.remove(path)

    # test case for the function extract_granule()
    def test_extract_granule(self):
        dataset_id = 'PODAAC-ASOP2-25X01'
        short_name = 'ASCATA-L2-25km'
        granule_name = 'ascat_20130719_230600_metopa_35024_eps_o_250_2200_ovw.l2.nc'
        bbox = '45,0,180,90'
        format = 'netcdf'
        data = self.podaac.extract_granule(
            dataset_id, short_name, granule_name, bbox, format)
        test_data = data[0].split('/')
        length = len(test_data)

        assert data != None
        assert test_data[length - 1] == granule_name
        assert_raises(Exception, self.podaac.extract_granule,
                      dataset_id='PODAAC-ASOP2-25X01')

        path = os.path.join(os.path.dirname(
            __file__), '../ascat_20130719_230600_metopa_35024_eps_o_250_2200_ovw.l2.nc')
        os.remove(path)

    # test case for the function extract_l4_granule()
    def test_extract_l4_granule(self):
        dataset_id = 'PODAAC-GHCMC-4FM02'
        short_name = 'CMC0.2deg-CMC-L4-GLOB-v2.0'
        test_format = '.nc'
        path = os.path.dirname(os.path.abspath(__file__))
        granule_name = self.podaac.extract_l4_granule(
            dataset_id, short_name, path)
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

    # test case for the function list_available_image_granule_dataset_ids()
    def test_list_available_image_granule_dataset_ids(self):
        data = self.podaac_utils.list_available_image_granule_dataset_ids()

        assert data != None
        assert type(data) is list
        assert len(data) != 0

    # test case for the function
    # list_available_image_granule_dataset_short_names()
    def test_list_available_image_granule_dataset_short_names(self):
        data = self.podaac_utils.list_available_image_granule_dataset_short_names()

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
