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

import unittest
import json
import requests
from ..l2ss import L2SS
from nose.tools import assert_raises


class test_podaac(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.l2ss = L2SS()

    # test case for the fucntion dataset_search()
    def test_dataset_search(self):
        dataset_id = 'PODAAC-ASOP2-25X01'
        variable = ['Surface Winds']
        sensor = 'Advanced Scatterometer'
        provider = 'KNMI'
        startTime = '2016-12-4T22:39:52Z'
        startIndex = '0'
        itemsPerPage = '7'
        dataset = self.l2ss.dataset_search(dataset_id=dataset_id, variable=variable, startTime=startTime,sensor=sensor,
                                           provider=provider, startIndex=startIndex, itemsPerPage=itemsPerPage)
        dataset_json = json.loads(dataset)

        assert dataset_json['response']['docs'][0][
            'Dataset-PersistentId'] == dataset_id

    # test case for the function dataset_variables()
    def test_dataset_variables(self):
        dataset_id = 'PODAAC-ASOP2-25X01'
        variables = json.loads(
            self.l2ss.dataset_variables(dataset_id=dataset_id))
        variables_data = variables['imgVariables']

        assert len(variables_data) != 0
        assert_raises(requests.exceptions.HTTPError,
                      self.l2ss.dataset_variables, dataset_id='PODAAC')

    # test case for the function granule_search
    def test_granule_search(self):
        dataset_id = 'PODAAC-ASOP2-25X01'
        bbox = '-180,-90,180,90'
        startTime = '2016-07-16T04:18:00Z'
        endTime = '2016-07-16T05:56:56Z'
        itemsPerPage = '7'
        startIndex = '0'
        name = 'ascat_20160716_041800_metopa_50541_eps_o_250_2401_ovw.l2.nc'
        sort = 'Granule-Name asc'
        granules = self.l2ss.granule_search(dataset_id=dataset_id, bbox=bbox, startTime=startTime, endTime=endTime,
                                            itemsPerPage=itemsPerPage, startIndex=startIndex, name=name, sort=sort)
        granules_json = json.loads(granules)

        assert granules_json['response']['docs'][0][
            'Granule-DatasetId'] == dataset_id
