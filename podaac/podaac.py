# Copyright 2016-2019 California Institute of Technology.
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

from future.moves.urllib.parse import urlencode
from future.moves.urllib.request import urlopen, urlretrieve
from future.moves.http.client import HTTPSConnection
import gzip
import json
import ntpath
import os
import requests
import time
import defusedxml.ElementTree as ET
import zipfile

URL = 'https://podaac.jpl.nasa.gov/ws/'
IMAGE_URL = 'https://podaac-tools.jpl.nasa.gov/l2ss-services/l2ss/preview/'
HEADERS = {
    'User-Agent': 'Podaacpy Python Library v2.4.0'
}


class Podaac:

    def __init__(self):
        """Sets the base WebServices URL to https://podaac.jpl.nasa.gov/ws/"""
        self.URL = 'https://podaac.jpl.nasa.gov/ws/'

    def dataset_metadata(self, dataset_id='', short_name='', _format='iso'):
        '''Dataset metadata service retrieves the metadata of a \
                dataset on PO.DAACs dataset catalog using the following \
                parameters: dataset_id, short_name, and format.

        :param dataset_id: dataset persistent ID. dataset_id or short_name \
                is required for this metadata service.
        :type dataset_id: :mod:`string`

        :param short_name: dataset short_name. dataset_id or short_name \
                is required for this metadata service.
        :type short_name: :mod:`string`

        :param _format: metadata format. Default format is iso.
        :type _format: :mod:`string`

        :returns: an xml response based on the requested 'format'. Options \
        are 'iso' and 'gcmd'.

        '''
        try:
            url = self.URL + 'metadata/dataset/?'
            if dataset_id:
                url = url + 'datasetId=' + dataset_id
            if short_name:
                url = url + '&shortName=' + short_name
            url = url + '&format=' + _format
            metadata = requests.get(url, headers=HEADERS)
            status_codes = [404, 400, 503, 408]
            if metadata.status_code in status_codes:
                metadata.raise_for_status()

        except requests.exceptions.HTTPError as error:
            print(error)
            raise

        return metadata.text

    def dataset_search(self, keyword='', start_time='', end_time='', start_index='', dataset_id='', short_name='',
                       instrument='', satellite='', file_format='', status='', process_level='', sort_by='',
                       bbox='', items_per_page='50', _format='atom', full='False'):
        '''Dataset Search service searches PO.DAAC's dataset catalog, over \
                Level 2, Level 3, and Level 4 datasets, using the following parameters: \
                dataset_id, short_name, start_time, end_time, bbox, and others.

        :param keyword: keyword specifies search text to search for datasets. \
                Example: 'modis'
        :type keyword: :mod:`string`

        :param start_time: start time in the format of YYYY-MM-DDTHH:mm:ssZ. \
                'Z' is the time-offset, where 'Z' signifies UTC or an actual \
                offset can be used. Example: 2012-01-22T01:21:21Z
        :type start_time: :mod:`time`

        :param end_time: stop time in the format of YYYY-MM-DDTHH:mm:ssZ. \
                'Z' is the time-offset, where 'Z' signifies UTC or an actual \
                offset can be used. Example: 2012-01-22T01:21:21Z
        :type end_time: :mod:`time`

        :param start_index: start index of entries found for search. Example: 1
        :type start_index: :mod:`int`

        :param items_per_page: number of results per page for \
                opensearch result. If format is not specified, format is set \
                to 50. The value range is from 0 to 400
        :type items_per_page: :mod:`int`

        :param dataset_id: dataset persistent ID. \
                Example: PODAAC-MODSA-T8D9N
        :type dataset_id: :mod:`string`

        :param short_name: dataset short_name. \
                Example: MODIS_AQUA_L3_SST_THERMAL_8DAY_9KM_NIGHTTIME
        :type short_name: :mod:`string`

        :param instrument: dataset instrument. Example: MODIS
        :type instrument: :mod:`string`

        :param satellite: dataset satellite. Example: AQUA
        :type satellite: :mod:`string`

        :param file_format: dataset data format. \
                Possible values: HDF, NetCDF
        :type file_format: :mod:`string`

        :param status: dataset status. \
                Possible values: OPEN, PREVIEW, SIMULATED, RETIRED
        :type status: :mod:`string`

        :param processLevel: dataset processing level. \
                Possible values: 1B, 2, 2P, 3, 4
        :type processLevel: :mod:`string`

        :param _format: response format. If format is not specified, \
                format is set to atom. Possible values: atom, html.
        :type _format: :mod:`string`

        :param sort_by: determines ordering of response. If sort_by \
                is not specified, sort order is by score (most relevant \
                dataset first). Possible values: timeAsc, timeDesc, \
                popularityAsc, popularityDesc.
        :type sort_by: :mod:`string`

        :param bbox: bounding box for spatial search. format \
                should look like "bbox=0.0,-45.0,180.0,40.0" which is \
                in order of west, south, east, north. Longitude values needs \
                to be in range of [-180.0,180.0]. Example: 0.0,-45.0,180.0,40.0
        :type bbox: :mod:`string`

        :param full: "true" to return response with complete PO.DAAC \
                metadata per entry. If full is not specified, full is set to false. \
                Possible values: true, false
        :type full: :mod:`string`

        :returns: the specified response format. If format is not specified, \
                format is set to atom. Possible values: atom, html

        '''
        try:
            url = self.URL + 'search/dataset/?'
            url = url + 'itemsPerPage=' + items_per_page + '&format=' + \
                _format + '&full=' + full

            if keyword:
                url = url + '&keyword=' + keyword
            if start_time:
                url = url + '&startTime=' + start_time
            if end_time:
                url = url + '&endTime=' + end_time
            if bbox:
                url = url + '&bbox=' + bbox
            if start_index:
                url = url + '&startIndex=' + start_index
            if dataset_id:
                url = url + '&datasetId=' + dataset_id
            if short_name:
                url = url + '&shortName=' + short_name
            if instrument:
                url = url + '&instrument=' + instrument
            if satellite:
                url = url + '&satellite=' + satellite
            if file_format:
                url = url + '&fileFormat=' + file_format
            if status:
                url = url + '&status=' + status
            if process_level:
                url = url + '&processLevel=' + process_level
            if sort_by:
                url = url + '&sortBy=' + sort_by
            if bbox:
                url = url + '&bbox=' + bbox
            datasets = requests.get(url, headers=HEADERS)
            status_codes = [404, 400, 503, 408]
            if datasets.status_code in status_codes:
                datasets.raise_for_status()

        except requests.exceptions.HTTPError as error:
            print(error)
            raise

        return datasets.text

    def dataset_variables(self, dataset_id):
        '''Given a PO.DAAC dataset identifier this function will return list of dataset variables.

        :param dataset_id: dataset persistent ID. dataset_id \
                is required for this metadata service.
        :type dataset_id: :mod:`string`

        :returns: a list of dataset variables for the dataset.

        '''

        dataset_url = ""
        dataset_variables = []
        dataset = self.granule_search(dataset_id=dataset_id)
        root = ET.fromstring(dataset.encode('utf-8'))
        dataset_entry = root.findall("./{http://www.w3.org/2005/Atom}entry")[0]
        dataset_links = dataset_entry.findall("{http://www.w3.org/2005/Atom}link")
        for link in dataset_links:
            if link.attrib['title'] == "OPeNDAP URL":
                dataset_url = link.attrib['href'].replace('html', 'ddx')
                break
        try:
            dataset_ddx_response = requests.get(dataset_url, headers=HEADERS)
            status_codes = [404, 400, 503, 408]
            if dataset_ddx_response.status_code in status_codes:
                dataset_ddx_response.raise_for_status()

            root = ET.fromstring(dataset_ddx_response.text.encode('utf-8'))
            dataset_vars = root.findall("{http://xml.opendap.org/ns/DAP/3.2#}Array")
            dataset_vars.extend(root.findall("{http://xml.opendap.org/ns/DAP/3.2#}Grid"))
            for variable in dataset_vars:
                dataset_variables.append(variable.attrib['name'])

        except requests.exceptions.HTTPError as error:
            print("It's likely that variable search is not available for your dataset. " +
                  "Please see https://github.com/nasa/podaacpy/issues/128")
            print(error)
            raise
        return dataset_variables

    def granule_metadata(self, dataset_id='', short_name='', granule_name='', _format='iso'):
        '''Granule metadata service retrieves the metadata of a granule \
                on PO.DAACs catalog in ISO-19115.

        :param dataset_id: dataset persistent ID. dataset_id or short_name \
                is required for this metadata service.
        :type dataset_id: :mod:`string`

        :param short_name: dataset short_name. dataset_id or short_name \
                is required for this metadata service.
        :type short_name: :mod:`string`

        :param granule_name: granule name. granule name is required \
                for this metadata service.
        :type granule_name: :mod:`string`

        :param _format: metadata format. Default format is iso.
        :type _format: :mod:`string`

        :returns: an xml response based on the requested 'format'.

        '''

        try:
            url = self.URL + 'metadata/granule/?'
            if dataset_id:
                url = url + 'datasetId=' + dataset_id
            else:
                raise Exception("Dataset Id is required")
            if short_name:
                url = url + '&shortName=' + short_name
            if granule_name:
                url = url + '&granuleName=' + granule_name

            url = url + '&format=' + _format
            granule_md = requests.get(url, headers=HEADERS)
            status_codes = [404, 400, 503, 408]
            if granule_md.status_code in status_codes:
                granule_md.raise_for_status()

        except requests.exceptions.HTTPError as error:
            print(error)
            raise

        return granule_md.text

    def last24hours_datacasting_granule_md(self, dataset_id='',
                                           short_name='', _format='datacasting', items_per_page=50):
        '''Granule metadata service retrieves metadata for a list \
                of granules archived within the last 24 hours in Datacasting \
                format.

        :param dataset_id: dataset persistent ID. dataset_id or short_name \
                is required for this metadata service.
        :type dataset_id: :mod:`string`

        :param short_name: dataset short_name. dataset_id or short_name \
                is required for this metadata service.
        :type short_name: :mod:`string`

        :param _format: metadata format. Must set to 'datacasting'.
        :type _format: :mod:`string`

        :param items_per_page: number of results per page. Default value is 50. \
                The value range is from 0 to 5000.
        :type items_per_page: :mod:`int`

        :returns: an xml response based on the requested 'format'. Options \
                are 'iso' and 'gcmd'.

        '''

        try:
            url = self.URL + 'metadata/granule/?'
            if dataset_id:
                url = url + 'datasetId=' + dataset_id
            else:
                raise Exception("Dataset Id is required")
            if short_name:
                url = url + '&shortName=' + short_name

            url = url + '&itemsPerPage=' + \
                str(items_per_page) + '&format=' + _format
            granule_md = requests.get(url, headers=HEADERS)
            status_codes = [404, 400, 503, 408]
            if granule_md.status_code in status_codes:
                granule_md.raise_for_status()

        except requests.exceptions.HTTPError as error:
            print(error)
            raise

        return granule_md.text

    def granule_search(self, dataset_id='', start_time='', end_time='', bbox='', start_index='', sort_by='timeAsc',
                       items_per_page='50', _format='atom'):
        '''Search Granule does granule searching on PO.DAAC level 2 swath \
                datasets (individual orbits of a satellite), and level 3 & 4 \
                gridded datasets (time averaged to span the globe). Coverage \
                footpritnt polygons are used to enable spatial search on level 2 \
                swath dataset. Currently, our footprints can contain no data and \
                also gaps in the swath data. Spatial search on level 2 data can \
                return granules where actual data does not intersect the selected \
                bounding box but its footprint intersects the selected bounding \
                box. The following parameters are supported: dataset_id, \
                short_name, start_time, end_time, bbox, and others.

        :param dataset_id: dataset persistent ID. dataset_id or short_name \
                is required for a granule search. Example: PODAAC-ASOP2-25X01
        :type dataset_id: :mod:`string`

        :param start_time: start time in the format of YYYY-MM-DDTHH:mm:ssZ. \
                'Z' is the time-offset, where 'Z' signifies UTC or an actual offset \
                can be used. Example: 2013-01-01T01:30:00Z
        :type start_time: :mod:`time`

        :param end_time: stop time in the format of YYYY-MM-DDTHH:mm:ssZ. \
                'Z' is the time-offset, where 'Z' signifies UTC or an actual \
                offset can be used. Example: 2014-01-01T00:00:00Z
        :type end_time: :mod:`time`

        :param bbox: bounding box for spatial search. format should look \
                like "bbox=0,0,180,90" which is in order of west, south, east, \
                north. Longitude values needs to be in range of [-180, 180]. \
                Latitude values needs to be in range of [-90, 90]. For level \
                2 datasets, spatial search is available for a subset. Call the \
                list_available_Level2_dataset_ids and \
                list_available_level2_datasetShortNames functions to see the \
                subset. BBox example: 0,0,180,90
        :type bbox: :mod:`string`

        :param start_index: start index of entries found for search. \
                Example: 1
        :type start_index: :mod:`int`

        :param items_per_page: number of results per page for opensearch \
                result. If format is not specified, format is set to 50. The \
                value range is from 0 to 400
        :type items_per_page: :mod:`int`

        :param sort_by: determines ordering of response. Possible \
                values: timeAsc, timeDesc.
        :type sort_by: :mod:`string`

        :param _format: response format. If format is not specified, \
                format is set to atom. Possible values: atom, html.
        :type _format: :mod:`string`

        :returns: an xml response based on the requested 'format'. Options \
                are 'atom' and 'html'.

        '''

        try:
            url = self.URL + 'search/granule/?'
            if dataset_id:
                url = url + 'datasetId=' + dataset_id
            else:
                raise Exception("Dataset Id is required")
            if start_time:
                url = url + '&startTime=' + start_time
            if end_time:
                url = url + '&endTime=' + end_time
            if bbox:
                url = url + '&bbox=' + bbox
            if start_index:
                url = url + '&startIndex=' + start_index

            url = url + '&sortBy=' + sort_by + \
                '&itemsPerPage=' + items_per_page + '&format=' + _format
            granules = requests.get(url, headers=HEADERS)
            status_codes = [404, 400, 503, 408]
            if granules.status_code in status_codes:
                granules.raise_for_status()

        except requests.exceptions.HTTPError as error:
            print(error)
            raise

        return granules.text

    def granule_preview(self, dataset_id='', image_variable='', path=''):
        '''The PODAAC Image service renders granules in the \
                PO.DAACs catalog to images such as jpeg and/or png. \
                This image service also utilizes OGC WMS protocol. \
                (http://www.opengeospatial.org/standards/wms). If the \
                granule does not have any data in the given selected \
                bounding box, HTTP 500 will be thrown since there is \
                no data to be imaged. Granule Search service can be used \
                to find level 2 swath data. However, the level 2 \
                spatial search uses coverage footprint polygons \
                generated for each granule, and this footprint can \
                contain no data or gaps. If the selected bounding box \
                resides on no data or gaps, HTTP 500 will be thrown. \
                There are three request methods in this service. They \
                are GetCapabilities, GetLegendGraphic, and GetMap.

        :param dataset_id: dataset persistent ID. dataset_id or \
                short_name is required for a granule search. Example: \
                PODAAC-ASOP2-25X01 :mod:`string`
        :type dataset_id: :mod:`string`

        :param image_variable: variables of the granule which have \
                'Preview Images'.  Image variables can be found \
                from Dataset Variable service. Use "id" from "imgVariable" \
                element.\
        :type image_variable: :mod:`string`

        :param path: Destination directory into which the granule \
                needs to be downloaded.
        :type format: :mod:`string`

        :returns: a png image file.

        '''

        try:
            bbox = '-180,-90,180,90'
            if dataset_id == '':
                raise Exception("Required dataset_id")
            image_data = self.granule_search(dataset_id=dataset_id, bbox=bbox)
            root = ET.fromstring(image_data.encode('utf-8'))

            # fetching the [URL Template]
            url_template = ''
            for entry in root.iter('{http://www.w3.org/2005/Atom}entry'):
                for element in entry:
                    if element.tag == '{http://www.w3.org/2005/Atom}link':
                        if element.attrib['title'] == "Preview Image":
                            url_template = element.attrib['href']
                            break

            if url_template == '':
                raise Exception(
                    "Preview Image not available for this dataset.")
            url = url_template + '/' + image_variable + '.png'
            if path == '':
                path = os.path.join(os.path.dirname(
                    __file__), dataset_id + '.png')
            else:
                path = path + '/' + dataset_id + '.png'
            with open(path, 'wb') as image:
                image.write(urlopen(url).read())

        except Exception as e:
            print(e)
            raise

        return image

    def granule_subset(self, input_file_path, path=''):
        '''Subset Granule service allows users to Submit subset jobs. \
        Use of this service should be preceded by a Granule Search in \
        order to identify and generate a list of granules to be subsetted. \
        NOTE : At present PODAAC's granule subsetting service is only \
        restricted to Level2 granules.

        :param input_file_path: path to a json file which contains the \
        the request that you want to send to PO.DAAC
        :type input_file_path: :mod:`string`

        :param path: path to a directory where you want the subsetted \
        dataset to be stored.
        :type path: :mod:`string`

        :returns: a string token which can be used to determine the status\
        of a subset task.

        '''
        data = open(input_file_path, 'r+')
        input_data = json.load(data)
        input_string = json.dumps(input_data)

        # submit subset request
        params = urlencode({'query': input_string})
        headers = {
            "Content-type": "application/x-www-form-urlencoded", "Accept": "*"}
        conn = HTTPSConnection("podaac.jpl.nasa.gov")
        conn.request("POST", "/ws/subset/granule?request=submit",
                     params, headers)
        response = conn.getresponse()

        data = response.read().decode('utf-8')
        result = json.loads(data)
        token = result['token']
        conn.close()

        flag = 0
        while flag == 0:
            url = url = self.URL + "subset/status?token=" + token
            subset_response = requests.get(url, headers=HEADERS).text
            subset_response_json = json.loads(subset_response)
            status = subset_response_json['status']
            if status == "done":
                flag = 1
            if status == "error":
                raise Exception("Unexpected error during subset job, post your issue to the PO.DAAC forum https://podaac.jpl.nasa.gov/forum/")
            time.sleep(1)

        download_url = subset_response_json['resultURLs'][0]
        split = download_url.split('/')
        length = len(split)
        zip_file_name = split[length - 1]
        if path == '':
            zip_path = os.path.join(os.path.dirname(__file__), zip_file_name)
        else:
            zip_path = path + '/' + zip_file_name
        response = urlretrieve(download_url, zip_path)
        zip_content = zipfile.ZipFile(zip_path)
        for i in zip_content.infolist():
            granule_name = i.filename
        zip_content.extractall(path=path)
        print("Podaacpy completed granule subset task for granule '%s'. Granule available at '%s'." % (granule_name, path))
        os.remove(zip_path)
        return granule_name

    def subset_status(self, token=''):
        '''Subset Granule Status service allows users to check the status \
        of submitted subset job.
        The possible status that it returns include the following.. ::

          * "submitted" : returned on successful submission of the request.
          * "error" : returned when there is error in the JSON POST request.
          * "unknown" : returned when the datasetId you sent is not valid.
          * "done" : returned when subsetting job you submitted is done.

        :param token: string token that is returned by PO.DAAC whilst \
        submitting a subset request.
        :type token: :mod:`string`

        :returns: the a status string of the subset request.

        '''
        url = self.URL + "subset/status?token=" + token
        subset_data = requests.get(url, headers=HEADERS).text
        subset_data_json = json.loads(subset_data)
        status = subset_data_json['status']

        return status

    def extract_l4_granule(self, dataset_id='', path=''):
        '''This is an additional function that we have provided apart \
        from the available webservices. The extract_l4_granule helps \
        retrieve the level 4 datasets from OPeNDAP server directly, \
        accompanied by the search granule for retrieving granule name \
        related to the specific dataset_id.

        :param dataset_id: dataset persistent ID. dataset_id or \
                short_name is required for a granule search. Example: \
                PODAAC-ASOP2-25X01
        :type dataset_id: :mod:`string`

        :param path: Destination directory into which the granule \
                needs to be downloaded.
        :type format: :mod:`string`

        :returns: string representation of granule name.
        '''
        try:
            start_index = '1'
            search_data = self.granule_search(
                dataset_id=dataset_id, start_index=start_index)
            root = ET.fromstring(search_data.encode('utf-8'))
            url = root[12][7].attrib['href']
            compressed_granule = ntpath.basename(url)
            granule_name = root[12][0].text
            if path == '':
                compressed_path = os.path.join(os.path.dirname(__file__), compressed_granule)
            else:
                compressed_path = path + '/' + compressed_granule
            urlretrieve(url, compressed_path)
            if compressed_granule.endswith('.gz'):
                compressed_granule = gzip.open(compressed_path, 'rb')
                with open(path + '/' + granule_name, 'wb') as uncompressed_granule:
                    uncompressed_granule.write(compressed_granule.read())
                    compressed_granule.close()
                    uncompressed_granule.close()
        except Exception as e:
            print(e)
            raise

        return granule_name
