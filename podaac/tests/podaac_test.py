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
        datasetId = 'PODAAC-GHMG2-2PO01'
        datasetShortName = 'OSDPD-L2P-MSG02'
        dataset_md = self.podaac.load_dataset_md(datasetId, datasetShortName)
        root = ET.fromstring(dataset_md.encode('utf-8'))
        shortName = root[1][0].attrib

        assert dataset_md != None
        assert str(shortName['id']) == datasetShortName
        assert_raises(requests.exceptions.HTTPError, self.podaac.load_dataset_md,
                      'PODAAC-GHMG2-2PO01', 'OSDPD-L2P-MSG02', 'is')

    # test case for the fucntion load_granule_md()
    def test_load_granule_md(self):
        datasetId = 'PODAAC-GHMG2-2PO01'
        datasetShortName = 'OSDPD-L2P-MSG02'
        granuleName = '20120912-MSG02-OSDPD-L2P-MSG02_0200Z-v01.nc'
        granule_md = self.podaac.load_granule_md(
            datasetId, datasetShortName, granuleName)
        root = ET.fromstring(granule_md.encode('utf-8'))
        shortName = root[1][0].attrib

        assert granule_md != None
        assert str(shortName['id']) == datasetShortName
        assert_raises(requests.exceptions.HTTPError,
                      self.podaac.load_granule_md, format='is')

    # test case for the function load_last24hours_datacasting_granule_md()
    def test_load_last24hours_datacasting_granule_md(self):
        datasetId = 'PODAAC-ASOP2-25X01'
        datasetShortName = 'ASCATA-L2-25km'
        format = 'datacasting'
        itemsPerPage = 10
        granule_md = self.podaac.load_last24hours_datacasting_granule_md(
            datasetId, datasetShortName, format, itemsPerPage)
        root = ET.fromstring(granule_md.encode('utf-8'))
        datasetId_ = root[0][3].text

        assert granule_md != None
        assert datasetId_ == datasetId
        assert_raises(requests.exceptions.HTTPError, self.podaac.load_last24hours_datacasting_granule_md,
                      'PODAAC-ASOP2-25X01', 'ASCATA-L2-25km', format='iso')

    # test case for the function search_dataset()
    def test_search_dataset(self):
        format = 'atom'
        itemsPerPage = '400'
        datasets = self.podaac.search_dataset(
            format=format, itemsPerPage=itemsPerPage)
        root = ET.fromstring(datasets.encode('utf-8'))
        service_name = "PO.DAAC Dataset Search Service"
        test_service_name = root[3][0].text.split('\t')[3][:-1]

        assert datasets != None
        assert test_service_name == service_name
        assert_raises(requests.exceptions.HTTPError,
                      self.podaac.search_dataset, format='iso')

    # test case for the function search_granule()
    def test_search_granule(self):
        testDatasetId = 'PODAAC-ASOP2-25X01'
        startTime = '2013-01-01T01:30:00Z'
        endTime = '2014-01-01T00:00:00Z'
        bbox = '-45,-45,45,45'
        startIndex = '1'
        format = 'atom'
        granules = self.podaac.search_granule(
            datasetId=testDatasetId, startTime=startTime, endTime=endTime, bbox=bbox, startIndex=startIndex, format=format)
        root = ET.fromstring(granules.encode('utf-8'))
        datasetId = root.find('{http://www.w3.org/2005/Atom}entry').find(
            '{http://podaac.jpl.nasa.gov/opensearch/}datasetId').text
        print datasetId

        assert granules != None
        assert testDatasetId == datasetId
        assert_raises(requests.exceptions.HTTPError,
                      self.podaac.search_granule, format='html')

    # test case for the function load_image_granule()
    def test_load_image_granule(self):
        datasetId = 'PODAAC-ASOP2-25X01'
        shortName = 'ASCATA-L2-25km'
        granuleName = 'ascat_20130719_230600_metopa_35024_eps_o_250_2200_ovw.l2.nc'
        bbox = '45,0,180,90'
        srs = 'EPSG:4326'
        height = '300'
        width = '200'
        data = self.podaac.load_image_granule(
            datasetId, shortName, granuleName, bbox, height, width, srs)
        test_data = data[0].split('/')
        length = len(test_data)

        assert data != None
        assert test_data[length - 1] == datasetId + '.png'
        assert_raises(Exception, self.podaac.load_image_granule,
                      datasetId="HBJHKASD")

        path = os.path.join(os.path.dirname(__file__),
                            '../' + datasetId + '.png')
        os.remove(path)
        path = os.path.join(os.path.dirname(__file__),
                            '../' + "HBJHKASD" + '.png')
        os.remove(path)

    # test case for the function extract_granule()
    def test_extract_granule(self):
        datasetId = 'PODAAC-ASOP2-25X01'
        shortName = 'ASCATA-L2-25km'
        granuleName = 'ascat_20130719_230600_metopa_35024_eps_o_250_2200_ovw.l2.nc'
        bbox = '45,0,180,90'
        format = 'netcdf'
        data = self.podaac.extract_granule(
            datasetId, shortName, granuleName, bbox, format)
        test_data = data[0].split('/')
        length = len(test_data)

        assert data != None
        assert test_data[length - 1] == granuleName
        assert_raises(Exception, self.podaac.extract_granule,
                      datasetId='PODAAC-ASOP2-25X01')

        path = os.path.join(os.path.dirname(
            __file__), '../ascat_20130719_230600_metopa_35024_eps_o_250_2200_ovw.l2.nc')
        os.remove(path)

    # test case for the function extract_l4_granule()
    def test_extract_l4_granule(self):
        datasetId = 'PODAAC-GHCMC-4FM02'
        shortName = 'CMC0.2deg-CMC-L4-GLOB-v2.0'
        test_format = '.nc'
        path = os.path.dirname(os.path.abspath(__file__))
        granuleName = self.podaac.extract_l4_granule(
            datasetId, shortName, path)
        length = len(granuleName)
        format = granuleName[length - 3:length]

        assert granuleName != None
        assert format == test_format
        assert_raises(Exception, self.podaac.extract_l4_granule,
                      datasetId='ABCDEF')

        path = os.path.join(os.path.dirname(__file__), granuleName)
        os.remove(path)

    # test case for the function list_available_granule_search_datasetIds()
    def test_list_available_granule_search_datasetIds(self):
        data = self.podaac_utils.list_available_granule_search_datasetIds()

        assert data != None
        assert type(data) is list
        assert len(data) != 0

    # test case for the function
    # list_available_granule_search_datasetShortNames()
    def test_list_available_granule_search_datasetShortNames(self):
        data = self.podaac_utils.list_available_granule_search_datasetShortNames()

        assert data != None
        assert type(data) is list
        assert len(data) != 0

    # test case for the function
    # list_available_granule_search_level2_datasetIds()
    def test_list_available_granule_search_level2_datasetIds(self):
        data = self.podaac_utils.list_available_granule_search_level2_datasetIds()

        assert data != None
        assert type(data) is list
        assert len(data) != 0

    # test case for the function
    # list_available_granule_search_level2_datasetShortNames()
    def test_list_available_granule_search_level2_datasetShortNames(self):
        data = self.podaac_utils.list_available_granule_search_level2_datasetShortNames()

        assert data != None
        assert type(data) is list
        assert len(data) != 0

    # test case for the function list_available_image_granule_datasetIds()
    def test_list_available_image_granule_datasetIds(self):
        data = self.podaac_utils.list_available_image_granule_datasetIds()

        assert data != None
        assert type(data) is list
        assert len(data) != 0

    # test case for the function
    # list_available_image_granule_datasetShortNames()
    def test_list_available_image_granule_datasetShortNames(self):
        data = self.podaac_utils.list_available_image_granule_datasetShortNames()

        assert data != None
        assert type(data) is list
        assert len(data) != 0

    # test case for the function list_available_extract_granule_datasetIds()
    def test_list_available_extract_granule_datasetIds(self):
        data = self.podaac_utils.list_available_extract_granule_datasetIds()

        assert data != None
        assert type(data) is list
        assert len(data) != 0

    # test case for the function
    # list_available_extract_granule_datasetShortNames()
    def test_list_available_extract_granule_datasetShortNames(self):
        data = self.podaac_utils.list_available_extract_granule_datasetShortNames()

        assert data != None
        assert type(data) is list
        assert len(data) != 0
