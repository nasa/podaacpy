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
import os
import json
import time
import zipfile
from future.moves.urllib.error import HTTPError
from future.moves.urllib.request import urlopen, urlretrieve
from future.moves.urllib.parse import urlencode
from future.moves.http.client import HTTPConnection


class L2SS:

    def __init__(self):
        self.URL = 'http://podaac-tools.jpl.nasa.gov/l2ss-services/l2ss/'

    def dataset_search(self, dataset_id='', variable=[], sensor=[], provider=[], start_time='', end_time='', start_index='', items_per_page=''):
        ''' Dataset search service lists available datasets and returns them.

            :param dataset_id: Search dataset belong to given PODAAC Dataset persistent ID.
            :type dataset_id: :mod:`string`

            :param variable: Search for datasets with variable name. For multi-value input, \
                this input is taken as a list. Example: [ 'Sea Surface Temperature', 'Surface Wind']
            :type short_name: :mod:`list`

            :param sensor: Search for datasets with sensor. For multi-value input, \
                this input is taken as a list.
            :type format: :mod:`string`

            :param provider: Search for datasets with provider. For multi-value input, \
                this input is taken as a list.
            :type format: :mod:`string`

            :param start_time: Lower time bound. If not specified, lower time bound of \
                the dataset will be used. Example: '2011-12-31T23:59:59-06:00Z'
            :type format: :mod:`string`

            :param end_time: Upper time bound. If not specified, upper time bound of \
                the dataset will be used. Example: 2019-12-31T23:59:59-06:00Z
            :type format: :mod:`string`

            :param items_per_page: number of results to return.
            :type format: :mod:`string`

            :param start_index: start index of result.
            :type format: :mod:`string`

            :returns: a json response containing the datasets.
        '''
        try:
            url = self.URL + 'dataset/search?'
            if(dataset_id):
                url = url + 'datasetId=' + dataset_id
            if(variable):
                for var in variable:
                    url = url + '&variable=' + var
            if(sensor):
                for item in sensor:
                    url = url + '&sensor=' + item
            if(provider):
                for item in provider:
                    url = url + '&provider=' + item
            if(start_time):
                url = url + '&startTime=' + start_time
            if(end_time):
                url = url + '&endTime=' + end_time
            if(start_index):
                url = url + '&startIndex=' + start_index
            if(items_per_page):
                url = url + '&itemsPerPage=' + items_per_page

            datasets = requests.get(url)
            status_codes = [404, 400, 503, 408]
            if datasets.status_code in status_codes:
                datasets.raise_for_status()

        except requests.exceptions.HTTPError as error:
            print(error)
            raise

        return datasets.text

    def dataset_variables(self, dataset_id):
        try:
            url = self.URL + '/dataset/variable?datasetId=' + dataset_id
            variables = requests.get(url)
            status_codes = [404, 400, 503, 408]
            if variables.status_code in status_codes:
                variables.raise_for_status()

        except requests.exceptions.HTTPError as error:
            print(error)
            raise

        return variables.text

    def granule_search(self, dataset_id='', bbox='', start_time='', end_time='', name='', sort='', start_index='', items_per_page=''):
        try:
            url = self.URL + 'granule/search?'
            if(dataset_id):
                url = url + 'datasetId=' + dataset_id
            if(bbox):
                url = url + '&bbox=' + bbox
            if(start_time):
                url = url + '&startTime=' + start_time
            if(end_time):
                url = url + '&endTime=' + end_time
            if(start_index):
                url = url + '&startIndex=' + start_index
            if(items_per_page):
                url = url + '&itemsPerPage=' + items_per_page
            if(name):
                url = url + '&name=' + name
            if(sort):
                url = url + '&sort=' + sort

            granules = requests.get(url)
            status_codes = [404, 400, 503, 408]
            if granules.status_code in status_codes:
                granules.raise_for_status()

        except requests.exceptions.HTTPError as error:
            print(error)
            raise

        return granules.text

    def granules_availability(self, dataset_id='', start_time='', end_time='', gap='', bbox=''):
        try:
            url = self.URL + 'granule/availability?'
            url = url + 'datasetId=' + dataset_id + '&startTime=' + \
                start_time + '&endTime=' + end_time + '&gap=' + gap
            if(bbox):
                url = url + '&bbox=' + bbox

            granule_availability = requests.get(url)
            status_codes = [404, 400, 503, 408]
            if granule_availability.status_code in status_codes:
                granule_availability.raise_for_status()

        except requests.exceptions.HTTPError as error:
            print(error)
            raise

        return granule_availability.text

    def granule_preview_image(self, dataset_id, granule, year, day, variable, path=''):
        try:
            url = self.URL + 'preview/' + dataset_id + '/' + year + \
                '/' + day + '/' + granule + '/' + variable + '.png'
            if(path):
                path = path + '/' + dataset_id + '.png'
            else:
                path = os.path.join(os.path.dirname(
                    __file__), dataset_id + '.png')
            image_file = open(path, 'wb')
            image = urlopen(url)
            image_file.write(image.read())

        except Exception:
            raise

        return image

    def image_palette(self, palette_name):
        try:
            url = self.URL + 'palettes/' + palette_name + '.json'
            image_palette = requests.get(url)
            status_codes = [404, 400, 503, 408]
            if image_palette.status_code in status_codes:
                image_palette.raise_for_status()

        except requests.exceptions.HTTPError as error:
            print(error)
            raise

        return image_palette.text

    def granule_download(self, query_string, path=''):
        params = urlencode({'query': query_string})
        headers = {
            "Content-type": "application/x-www-form-urlencoded", "Accept": "*"}
        connection = HTTPConnection("podaac-tools.jpl.nasa.gov")
        connection.request("POST", "/l2ss-services/l2ss/subset/submit",
                           params, headers)
        response = connection.getresponse()
        data = response.read().decode('utf-8')
        result = json.loads(data)
        token = result['token']
        connection.close()

        flag = 0
        while(flag == 0):
            url = url = self.URL + "subset/status?token=" + token
            subset_response = requests.get(url).text
            subset_response_json = json.loads(subset_response)
            status = subset_response_json['status']
            if (status == "done"):
                flag = 1
            if (status == "error"):
                raise Exception(
                    "Unexpected error occured for the subset job you have requested")
            if (status == 'partial error'):
                raise Exception(
                    "The job was done but with some errors, please submit the job again")
            time.sleep(1)

        print("Done! downloading the dataset zip .....")
        download_url = subset_response_json['resultURLs'][0]
        split = download_url.split('/')
        length = len(split)
        zip_file_name = split[length - 1]
        if path == '':
            path = os.path.join(os.path.dirname(__file__), zip_file_name)
        else:
            path = path + zip_file_name
        response = urlretrieve(download_url, path)
        zip_content = zipfile.ZipFile(path)
        zip_content.extractall()
        os.remove(path)

    def subset_status(self, token):
        try:
            url = self.URL + 'subset/status?token=' + token
            response = requests.get(url)
            response_json = json.loads(response.text)
            status = response_json['status']
            if(status == 'unknown'):
                raise Exception("Invalid Token : Please check your token")

        except Exception:
            raise
