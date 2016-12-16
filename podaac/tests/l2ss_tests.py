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
import os
from future.moves.urllib.error import HTTPError
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
        sensor = ['Advanced Scatterometer']
        provider = ['KNMI']
        start_time = '2016-12-4T22:39:52Z'
        start_index = '0'
        items_per_page = '7'
        dataset = self.l2ss.dataset_search(dataset_id=dataset_id, variable=variable, start_time=start_time, sensor=sensor,
                                           provider=provider, start_index=start_index, items_per_page=items_per_page)
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
        start_time = '2016-07-16T04:18:00Z'
        end_time = '2016-07-16T05:56:56Z'
        items_per_page = '7'
        start_index = '0'
        name = 'ascat_20160716_041800_metopa_50541_eps_o_250_2401_ovw.l2.nc'
        sort = 'Granule-Name asc'
        granules = self.l2ss.granule_search(dataset_id=dataset_id, bbox=bbox, start_time=start_time, end_time=end_time,
                                            items_per_page=items_per_page, start_index=start_index, name=name, sort=sort)
        granules_json = json.loads(granules)

        assert granules_json['response']['docs'][0][
            'Granule-DatasetId'] == dataset_id

    # test case for the function granules_availability
    def test_granules_availability(self):
        dataset_id = 'PODAAC-ASOP2-25X01'
        bbox = '-180,-90,180,90'
        start_time = '2014-10-12T11:42:00Z'
        end_time = '2016-10-12T11:42:00Z'
        gap = 'DAY'
        granule_availability = json.loads(self.l2ss.granules_availability(
            dataset_id=dataset_id, start_time=start_time, end_time=end_time, bbox=bbox, gap=gap))
        availability_data = granule_availability[
            'facet_counts']['facet_dates']['Granule-StartTime']

        assert len(availability_data) != 0
        assert_raises(requests.exceptions.HTTPError,
                      self.l2ss.granules_availability, dataset_id=dataset_id)

    # test case for the function granule_preview_image
    def test_granule_preview_image(self):
        dataset_id = 'PODAAC-ASOP2-25X01'
        granule = 'ascat_20140520_005700_metopa_39344_eps_o_250_2300_ovw.l2.nc'
        year = '2014'
        day = '140'
        variable = 'wind_speed'
        path = os.path.join(os.path.dirname(__file__))
        image = self.l2ss.granule_preview_image(
            dataset_id=dataset_id, granule=granule, year=year, day=day, variable=variable, path=path)

        assert image != None
        path = os.path.join(os.path.dirname(__file__),
                            dataset_id + '.png')
        os.remove(path)
        assert_raises(HTTPError,
                      self.l2ss.granule_preview_image, dataset_id=dataset_id, granule=granule, year=year, day=day, variable='wind_spee')

    # test case for the function image_palette
    def test_image_palette(self):
        palette_name = 'paletteMedspirationIndexed'
        test_palette_name = 'medspiration'
        palette = json.loads(
            self.l2ss.image_palette(palette_name=palette_name))
        palette_name = palette['Palette'][
            'attributes']['attribute'][0]['value']

        assert palette_name == test_palette_name
        assert_raises(requests.exceptions.HTTPError,
                      self.l2ss.image_palette, palette_name='SomeUnknownPalette')

    # test case for the function granule_download
    def test_granule_download(self):
        query = {
            "email": "unknown@unknown.com",
            "query":
            [
                {
                    "compact": "true",
                    "datasetId": "PODAAC-ASOP2-25X01",
                    "bbox": "-180,-90,180,90",
                    "variables": ["lat", "lon", "time", "wind_speed"],
                    "granuleIds": ["ascat_20140520_005700_metopa_39344_eps_o_250_2300_ovw.l2.nc"]
                }
            ]
        }
        self.l2ss.granule_download(query_string=query)
        assert os.path.isfile(
            './subsetted-ascat_20140520_005700_metopa_39344_eps_o_250_2300_ovw.l2.nc') == True
        os.remove(
            './subsetted-ascat_20140520_005700_metopa_39344_eps_o_250_2300_ovw.l2.nc')

    # test case for the function subset_status
    def test_subset_status(self):
        test_token_status = "unknown"
        token = 'FakeToken'

        assert_raises(Exception, self.l2ss.subset_status, token=token)
