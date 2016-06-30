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

import requests, urllib
from bs4 import BeautifulSoup as bs
import os
import xml.etree.ElementTree as ET

class PodaacUtils:

	def __init__(self):
		self.URL = 'http://podaac.jpl.nasa.gov/ws/'

	def list_available_granule_search_level2_datasetIds(self):
		'''Convenience function which returns an up-to-date \
			list of available level2 granule dataset id's.

		:returns: a comma-seperated list of granule dataset id's

		'''
		datasetIds = []
		html = requests.get(self.URL+'search/granule/index.html')
		soup = bs(html.text, 'html.parser')

		table = soup.find("table", {"id": "tblDataset2"})
		rows = table.find_all('tr')
		rows.remove(rows[0])

		for row in rows:
			x = row.find_all('td')
			datasetIds.append(x[0].text.encode('utf-8'))

		return datasetIds

	def list_available_granule_search_level2_datasetShortNames(self):
		'''Convenience function which returns an up-to-date \
			list of available level2 granule dataset short names.

		:returns: a comma-seperated list of granule dataset short names.

		'''
		datasetShortNames = []
		html = requests.get(self.URL+'search/granule/index.html')
		soup = bs(html.text, 'html.parser')

		table = soup.find("table", {"id": "tblDataset2"})
		rows = table.find_all('tr')
		rows.remove(rows[0])

		for row in rows:
			x = row.find_all('td')
			datasetShortNames.append(x[1].text.encode('utf-8'))

		return datasetShortNames


	def list_available_granule_search_datasetIds(self):
		'''Convenience function which returns an up-to-date \
			list of available granule dataset id's.

		:returns: a comma-seperated list of granule dataset id's

		'''
		data_part1 = requests.get(self.URL+'search/dataset/?format=atom&itemsPerPage=400').text
		data_part2 = requests.get(self.URL+'search/dataset?startIndex=400&itemsPerPage=400&format=atom').text 
		root1 = ET.fromstring(data_part1.encode('utf-8'))
		root2 = ET.fromstring(data_part2.encode('utf-8'))

		datasetIds = []
		for entry in root1.findall('{http://www.w3.org/2005/Atom}entry'):
			Id = entry.find('{http://podaac.jpl.nasa.gov/opensearch/}datasetId').text
			Id = Id.split('\t')[3][:-1]
			datasetIds.append(Id)

		for entry in root2.findall('{http://www.w3.org/2005/Atom}entry'):
			Id = entry.find('{http://podaac.jpl.nasa.gov/opensearch/}datasetId').text
			Id = Id.split('\t')[3][:-1]
			datasetIds.append(Id)

		datasetIds_level1 = []
		datasetIds_level2 = self.list_available_granule_search_level2_datasetIds()
		datasetIds_level1 = list(set(datasetIds) - set(datasetIds_level2))

		return datasetIds_level1

	def list_available_granule_search_datasetShortNames(self):
		'''Convenience function which returns an up-to-date \
			list of available granule dataset short names.

		:returns: a comma-seperated list of granule dataset short names.

		'''
		data_part1 = requests.get(self.URL+'search/dataset/?format=atom&itemsPerPage=400').text
		data_part2 = requests.get(self.URL+'search/dataset?startIndex=400&itemsPerPage=400&format=atom').text 
		root1 = ET.fromstring(data_part1.encode('utf-8'))
		root2 = ET.fromstring(data_part2.encode('utf-8'))

		datasetShortNames = []
		for entry in root1.findall('{http://www.w3.org/2005/Atom}entry'):
			Name = entry.find('{http://podaac.jpl.nasa.gov/opensearch/}shortName').text
			Name = Name.split('\t')[3][:-1]
			datasetShortNames.append(Name)
			
		for entry in root2.findall('{http://www.w3.org/2005/Atom}entry'):
			Name = entry.find('{http://podaac.jpl.nasa.gov/opensearch/}shortName').text
			Name = Name.split('\t')[3][:-1]
			datasetShortNames.append(Name)

		#datasetShortNames_level1 = []
		datasetShortNames_level2 = self.list_available_granule_search_level2_datasetShortNames()
		datasetShortNames_level1 = list(set(datasetShortNames) - set(datasetShortNames_level2))

		return datasetShortNames_level1

	def list_available_image_granule_datasetIds(self):
		'''Convenience function which returns an up-to-date \
			list of available granule dataset id's which can be \
			used in the imagery service.

		:returns: a comma-seperated list of granule dataset id's

		'''
		datasetIds = []
		html = requests.get(self.URL+'image/granule/index.html')
		soup = bs(html.text, 'html.parser')

		table = soup.find("table", {"id": "tblDataset"})
		rows = table.find_all('tr')
		rows.remove(rows[0])

		for row in rows:
			x = row.find_all('td')
			datasetIds.append(x[0].text.encode('utf-8'))

		return datasetIds

	def list_available_image_granule_datasetShortNames(self):
		'''Convenience function which returns an up-to-date \
			list of available granule dataset short names which can be \
			used in the imagery service.

		:returns: a comma-seperated list of granule dataset short names.

		'''
		datasetShortNames = []
		html = requests.get(self.URL+'image/granule/index.html')
		soup = bs(html.text, 'html.parser')

		table = soup.find("table", {"id": "tblDataset"})
		rows = table.find_all('tr')
		rows.remove(rows[0])

		for row in rows:
			x = row.find_all('td')
			datasetShortNames.append(x[1].text.encode('utf-8'))

		return datasetShortNames

	def list_available_extract_granule_datasetIds(self):
		'''Convenience function which returns an up-to-date \
			list of available granule dataset id's which can be \
			used in the granule extraction service.

		:returns: a comma-seperated list of granule dataset id's.

		'''
		datasetIds = []
		html = requests.get(self.URL+'extract/granule/index.html')
		soup = bs(html.text, 'html.parser')
		
		table = soup.find("table", {"id": "tblDataset"})
		rows = table.find_all('tr')
		rows.remove(rows[0])

		for row in rows:
			x = row.find_all('td')
			datasetIds.append(x[0].text.encode('utf-8'))

		return datasetIds

	def list_available_extract_granule_datasetShortNames(self):
		'''Convenience function which returns an up-to-date \
			list of available granule dataset short names which can be \
			used in the granule extraction service.

		:returns: a comma-seperated list of granule dataset short names.

		'''
		datasetShortNames = []
		html = requests.get(self.URL+'extract/granule/index.html')
		soup = bs(html.text, 'html.parser')
		
		table = soup.find("table", {"id": "tblDataset"})
		rows = table.find_all('tr')
		rows.remove(rows[0])

		for row in rows:
			x = row.find_all('td')
			datasetShortNames.append(x[1].text.encode('utf-8'))

		return datasetShortNames