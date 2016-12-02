#
#  Licensed to the Apache Software Foundation (ASF) under one or more
#  contributor license agreements.  See the NOTICE file distributed with
#  this work for additional information regarding copyright ownership.
#  The ASF licenses this file to You under the Apache License, Version 2.0
#  (the "License"); you may not use this file except in compliance with
#  the License.  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

import unittest
from ..l2ss import L2SS


class test_podaac(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.l2ss = L2SS()

    def test_dataset_search(self):
        dataset_id = 'PODAAC-ASOP2-25X01'
        dataset = self.l2ss.dataset_search(dataset_id=dataset_id)
