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

from .. import podaac 
import os 
import xml.etree.ElementTree as ET


#test case for the function load_dataset_md()
def test_load_dataset_md():
	datasetId = 'PODAAC-GHMG2-2PO01'
	datasetShortName = 'OSDPD-L2P-MSG02'
 	dataset_md = podaac.load_dataset_md(datasetId, datasetShortName)
	root = ET.fromstring(dataset_md.encode('utf-8'))
	shortName = root[1][0].attrib

	assert dataset_md != None 
	assert str(shortName['id']) == datasetShortName

#test case for the fucntion load_granule_md() 
def test_load_granule_md():
	datasetId = 'PODAAC-GHMG2-2PO01'
	datasetShortName = 'OSDPD-L2P-MSG02'
	granuleName = '20120912-MSG02-OSDPD-L2P-MSG02_0200Z-v01.nc'
	granule_md =  podaac.load_granule_md(datasetId, datasetShortName, granuleName)
	root = ET.fromstring(granule_md.encode('utf-8'))
	shortName = root[1][0].attrib

	assert granule_md != None 
	assert str(shortName['id']) == datasetShortName

#test case for the function load_last24hours_datacasting_granule_md()
def test_load_last24hours_datacasting_granule_md():
	datasetId = 'PODAAC-ASOP2-25X01'
	datasetShortName = 'ASCATA-L2-25km'
	format = 'datacasting'
	itemsPerPage = 10
	granule_md = podaac.load_last24hours_datacasting_granule_md(datasetId, datasetShortName, format, itemsPerPage)
	root = ET.fromstring(granule_md.encode('utf-8'))
	datasetId_ = root[0][3].text

	assert granule_md != None 
	assert datasetId_ == datasetId

#test case for the function search_dataset()
def test_search_dataset():
	format = 'atom'
	itemsPerPage = '400'
	datasets = podaac.search_dataset(format=format, itemsPerPage=itemsPerPage)
	root = ET.fromstring(datasets.encode('utf-8'))
	service_name = "PO.DAAC Dataset Search Service"
	test_service_name = root[3][0].text.split('\t')[3][:-1]

	assert datasets != None
	assert test_service_name == service_name


#test case for the function search_granule()
def test_search_granule():
	testDatasetId = 'PODAAC-ASOP2-25X01'
	startTime = '2013-01-01T01:30:00Z'
	endTime = '2014-01-01T00:00:00Z'
	bbox = '-45,-45,45,45'
	startIndex = '1'
	format = 'atom'
	granules = podaac.search_granule(datasetId=testDatasetId, startTime=startTime, endTime=endTime, bbox=bbox, startIndex=startIndex, format=format)
	root = ET.fromstring(granules.encode('utf-8'))
	datasetId = root.find('{http://www.w3.org/2005/Atom}entry').find('{http://podaac.jpl.nasa.gov/opensearch/}datasetId').text
	print datasetId

	assert granules != None 
	assert testDatasetId == datasetId


#test case for the function load_image_granule()  
def test_load_image_granule(): 
	datasetId = 'PODAAC-ASOP2-25X01'
	shortName = 'ASCATA-L2-25km'
	granuleName = 'ascat_20130719_230600_metopa_35024_eps_o_250_2200_ovw.l2.nc'
	bbox = '45,0,180,90'
	srs = 'EPSG:4326'
	height = '300'
	width = '200'
	data = podaac.load_image_granule(datasetId, shortName, granuleName, bbox, height, width, srs)
	test_data = data[0].split('/')
	length = len(test_data)

	assert data != None 
	assert test_data[length-1] == datasetId+'.jpg'

	path = os.path.join(os.path.dirname(__file__), '../'+datasetId+'.jpg')
	os.remove(path)

#test case for the function extract_granule()
def test_extract_granule():
	datasetId = 'PODAAC-ASOP2-25X01'
	shortName = 'ASCATA-L2-25km'
	granuleName = 'ascat_20130719_230600_metopa_35024_eps_o_250_2200_ovw.l2.nc'
	bbox = '45,0,180,90'
	format = 'netcdf'
	data = podaac.extract_granule(datasetId, shortName, granuleName, bbox, format)
	test_data = data[0].split('/')
	length =  len(test_data)

	assert data != None
	assert test_data[length-1] == granuleName
	
	path = os.path.join(os.path.dirname(__file__), '../ascat_20130719_230600_metopa_35024_eps_o_250_2200_ovw.l2.nc')
	os.remove(path)

#test case for the function list_available_granule_search_datasetIds()
def test_list_available_granule_search_datasetIds():
	data = podaac.list_available_granule_search_datasetIds()

	assert data != None
	assert type(data) is list
	assert len(data) != 0

#test case for the function list_available_granule_search_datasetShortNames()
def test_list_available_granule_search_datasetShortNames():
	data = podaac.list_available_granule_search_datasetShortNames()

	assert data != None
	assert type(data) is list
	assert len(data) != 0

#test case for the function list_available_granule_search_level2_datasetIds()
def test_list_available_granule_search_level2_datasetIds():
	data = podaac.list_available_granule_search_level2_datasetIds()

	assert data != None
	assert type(data) is list
	assert len(data) != 0

#test case for the function list_available_granule_search_level2_datasetShortNames()
def test_list_available_granule_search_level2_datasetShortNames():
	data = podaac.list_available_granule_search_level2_datasetShortNames()

	assert data != None
	assert type(data) is list
	assert len(data) != 0

#test case for the function list_available_image_granule_datasetIds()
def test_list_available_image_granule_datasetIds():
	data = podaac.list_available_image_granule_datasetIds()

	assert data != None
	assert type(data) is list
	assert len(data) != 0

#test case for the function list_available_image_granule_datasetShortNames()
def test_list_available_image_granule_datasetShortNames():
	data = podaac.list_available_image_granule_datasetShortNames()

	assert data != None
	assert type(data) is list
	assert len(data) != 0

#test case for the function list_available_extract_granule_datasetIds()
def test_list_available_extract_granule_datasetIds(): 
	data = podaac.list_available_extract_granule_datasetIds()

	assert data != None
	assert type(data) is list
	assert len(data) != 0

#test case for the function list_available_extract_granule_datasetShortNames()
def test_list_available_extract_granule_datasetShortNames():
	data = podaac.list_available_extract_granule_datasetShortNames()

	assert data != None
	assert type(data) is list
	assert len(data) != 0