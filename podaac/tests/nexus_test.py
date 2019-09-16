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

from ..nexus import NEXUS
from ..nexus import NEXUSOW
import json
from datetime import datetime
from shapely.geometry import box
import unittest

class TestNEXUS(unittest.TestCase):

    def setUp(self):
        self.nexus = NEXUS()

    def test_daily_difference_average(self):
        self.nexus.set_target(target='https://oceanworks.jpl.nasa.gov/')
        data = self.nexus.daily_difference_average("AQUARIUS_L3_SSS_v5_7day", box(-180, -90, 180, 90), datetime(1970, 1, 16), datetime(1970, 1, 17))
        data_json = json.loads(data)
        assert data is not None

    def test_dataset_list(self):
        data = self.nexus.dataset_list()
        data_json = json.loads(data)
        assert data is not None
        assert len(data) > 10
        assert data_json[0].get('shortName') is not None

    def test_subset(self):
        data = self.nexus.subset(dataset, bounding_box, start_datetime, end_datetime, parameter, metadata_filter)
        data_json = json.loads(data)
        assert data != None

    def test_time_series(self):
        data = self.nexus.time_series(datasets, bounding_box, start_datetime, end_datetime)
        data = self.nexus.time_series(("AVHRR_OI_L4_GHRSST_NCEI", "MEASURES_SLA_JPL_1603"), box(-150, 45, -120, 60),
datetime(2016, 1, 1), datetime(2016, 12, 31))
        data_json = json.loads(data)
        assert data != None

class TestNEXUSOW(unittest.TestCase):

    def setUp(self):
        self.nexusow = NEXUSOW()

    def test_run_file(self):
        data = self.nexusow.run_file(filename)
        data_json = json.loads(data)
        assert data != None

    def test_run_string(self):
        data = self.nexusow.run_string(code_string)
        data_json = json.loads(data)
        assert data != None
