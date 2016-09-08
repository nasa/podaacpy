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

import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET


class PodaacUtils:

    def __init__(self):
        self.URL = 'http://podaac.jpl.nasa.gov/ws/'

    def list_available_granule_search_level2_dataset_ids(self):
        '''Convenience function which returns an up-to-date \
                list of available level2 granule dataset id's.

        :returns: a comma-seperated list of granule dataset id's

        '''
        dataset_ids = []
        url = 'http://podaac.jpl.nasa.gov/l2ssIngest/datasets'
        response = requests.get(url)
        data = response.json()

        for item in data["datasets"]:
            dataset_ids.append(item["persistentId"])

        return dataset_ids

    def list_available_granule_search_level2_dataset_short_names(self):
        '''Convenience function which returns an up-to-date \
                list of available level2 granule dataset short names.

        :returns: a comma-seperated list of granule dataset short names.

        '''
        dataset_ids = []
        url = 'http://podaac.jpl.nasa.gov/l2ssIngest/datasets'
        response = requests.get(url)
        data = response.json()

        for item in data["datasets"]:
            dataset_ids.append(item["shortName"])

        return dataset_ids

    def list_available_granule_search_dataset_ids(self):
        '''Convenience function which returns an up-to-date \
                list of available granule dataset id's.

        :returns: a comma-seperated list of granule dataset id's

        '''
        data_part1 = requests.get(
            self.URL + 'search/dataset/?format=atom&itemsPerPage=400').text
        data_part2 = requests.get(
            self.URL + 'search/dataset?startIndex=400&itemsPerPage=400&format=atom').text
        root1 = ET.fromstring(data_part1.encode('utf-8'))
        root2 = ET.fromstring(data_part2.encode('utf-8'))

        dataset_ids = []
        for entry in root1.findall('{http://www.w3.org/2005/Atom}entry'):
            dataset_id = entry.find(
                '{http://podaac.jpl.nasa.gov/opensearch/}datasetId').text
            dataset_id = dataset_id.split('\t')[3][:-1]
            dataset_ids.append(dataset_id)

        for entry in root2.findall('{http://www.w3.org/2005/Atom}entry'):
            dataset_id = entry.find(
                '{http://podaac.jpl.nasa.gov/opensearch/}datasetId').text
            dataset_id = dataset_id.split('\t')[3][:-1]
            dataset_ids.append(dataset_id)

        dataset_ids_level1 = []
        dataset_ids_level2 = self.list_available_granule_search_level2_dataset_ids()
        dataset_ids_level1 = list(set(dataset_ids) - set(dataset_ids_level2))

        return dataset_ids_level1

    def list_available_granule_search_dataset_short_names(self):
        '''Convenience function which returns an up-to-date \
                list of available granule dataset short names.

        :returns: a comma-seperated list of granule dataset short names.

        '''
        data_part1 = requests.get(
            self.URL + 'search/dataset/?format=atom&itemsPerPage=400').text
        data_part2 = requests.get(
            self.URL + 'search/dataset?startIndex=400&itemsPerPage=400&format=atom').text
        root1 = ET.fromstring(data_part1.encode('utf-8'))
        root2 = ET.fromstring(data_part2.encode('utf-8'))

        dataset_short_names = []
        for entry in root1.findall('{http://www.w3.org/2005/Atom}entry'):
            name = entry.find(
                '{http://podaac.jpl.nasa.gov/opensearch/}shortName').text
            name = name.split('\t')[3][:-1]
            dataset_short_names.append(name)

        for entry in root2.findall('{http://www.w3.org/2005/Atom}entry'):
            name = entry.find(
                '{http://podaac.jpl.nasa.gov/opensearch/}shortName').text
            name = name.split('\t')[3][:-1]
            dataset_short_names.append(name)

        # dataset_short_names_level1 = []
        dataset_short_names_level2 = self.list_available_granule_search_level2_dataset_short_names()
        dataset_short_names_level1 = list(
            set(dataset_short_names) - set(dataset_short_names_level2))

        return dataset_short_names_level1

    def list_available_extract_granule_dataset_ids(self):
        '''Convenience function which returns an up-to-date \
                list of available granule dataset id's which can be \
                used in the granule extraction service.

        :returns: a comma-seperated list of granule dataset id's.

        '''
        dataset_ids = []
        html = requests.get(self.URL + 'extract/granule/index.html')
        soup = BeautifulSoup(html.text, 'html.parser')

        table = soup.find("table", {"id": "tblDataset"})
        rows = table.find_all('tr')
        rows.remove(rows[0])

        for row in rows:
            x = row.find_all('td')
            dataset_ids.append(x[0].text.encode('utf-8'))

        return dataset_ids

    def list_available_extract_granule_dataset_short_names(self):
        '''Convenience function which returns an up-to-date \
                list of available granule dataset short names which can be \
                used in the granule extraction service.

        :returns: a comma-seperated list of granule dataset short names.

        '''
        dataset_short_names = []
        html = requests.get(self.URL + 'extract/granule/index.html')
        soup = BeautifulSoup(html.text, 'html.parser')

        table = soup.find("table", {"id": "tblDataset"})
        rows = table.find_all('tr')
        rows.remove(rows[0])

        for row in rows:
            x = row.find_all('td')
            dataset_short_names.append(x[1].text.encode('utf-8'))

        return dataset_short_names
