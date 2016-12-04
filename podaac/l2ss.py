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
from future.moves.urllib.error import HTTPError


class L2SS:

    def __init__(self):
        self.URL = 'http://podaac-tools.jpl.nasa.gov/l2ss-services/l2ss/'

    def dataset_search(self, dataset_id='', variable=[], sensor='', provider='', startTime='', endTime='', startIndex='', itemsPerPage=''):
        try:
            url = self.URL + 'dataset/search?'
            if(dataset_id):
                url = url + 'datasetId=' + dataset_id
            if(variable):
                for var in variable:
                    url = url + '&variable=' + var
            if(sensor):
                url = url + '&sensor=' + sensor
            if(provider):
                url = url + '&provider=' + provider
            if(startTime):
                url = url + '&startTime=' + startTime
            if(endTime):
                url = url + '&endTime=' + endTime
            if(startIndex):
                url = url + '&startIndex=' + startIndex
            if(itemsPerPage):
                url = url + '&itemsPerPage=' + itemsPerPage

            datasets = requests.get(url)
            status_codes = [404, 400, 503, 408]
            if datasets.status_code in status_codes:
                datasets.raise_for_status()

        except requests.exceptions.HTTPError as error:
            print(error)
            raise

        return datasets.text