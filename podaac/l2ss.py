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

import requests


class L2SS:

    def __init__(self):
        self.URL = 'http://podaac-tools.jpl.nasa.gov/'

    def dataset_search(self, dataset_id=''):
        try:
            url = self.URL + 'l2ss/dataset/search?'
            if(dataset_id != ''):
                url = url + 'datasetId=' + dataset_id
            else:
                raise Exception("Dataset Id is required")
            datasets = requests.get(url)
            if datasets.status_code == 404 or datasets.status_code == 400 or datasets.status_code == 503 or datasets.status_code == 408:
                datasets.raise_for_status()

        except requests.exceptions.HTTPError as error:
            print(error)
            raise

        return datasets.text
