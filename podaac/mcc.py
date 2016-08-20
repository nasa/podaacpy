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

import os
import requests


class MCC:

    def __init__(self):
        self.URL = 'http://podaac-uat.jpl.nasa.gov/mcc/check'

    def check_remote_file(self, checkers, url_upload, response='json'):
        '''GET a remote file e.g. from an OPeNDAP URL and compliance \
                check it against the endpoint at http://podaac-uat.jpl.nasa.gov/mcc/check.

        :param checkers: Must specify at least one test. Multiple tests are \
                delimited by commas. Possible values include 'ACDD-x.x', \
                'CF' and 'GDS2' which also requires 'GDS2-parameters:levelAvailable'. \
                Available levels are 'L2P', 'L3', and 'L4'.
        :type checkers: :mod:`string`

        :param url_upload: A valid url to a netCDF file; maximum 5.00 GB
        :type url_upload: :mod:`string`

        :param response: (Optional) Specify 'html', 'json', or 'pdf' result output.
        :type response: :mod:`string`

        :returns: one of 'html', 'json', or 'pdf'.

        :raises ValueError: If no dataset can be found for the supplied url_upload \
                or if the requested dataset is a multi-file dataset.

        '''

        try:
            url = self.URL + '?checkers=' + checkers + \
                '&url-upload=' + url_upload + '&response=' + response
            result = requests.get(url)
            if result.status_code == 404 or result.status_code == 400 or result.status_code == 503 or result.status_code == 408:
                result.raise_for_status()

        except requests.exceptions.HTTPError as error:
            print(error)
            raise

        return result.text

    def check_local_file(self, acdd_version, gds2_parameters, file_upload, response='json'):
        '''POST a local file to the metadata compliance checker \
                endpoint at http://podaac-uat.jpl.nasa.gov/mcc/check

        :param acdd_version: Must be present and and set to either 1.1 or 1.3. \
                'acdd' tag must also be present and must be set to 'on'.
        :type acdd_version: :mod:`string`

        :param gds2_parameters: Must be present and set to either 'L2P', 'L3', 'L4'.
        :type gds2_parameters: :mod:`string`

        :param file_upload: A valid location of a netCDF file; maximum 5.00 GB.
        :type file_upload: :mod:`string`

        :param response: Specify 'html', 'json', or 'pdf' result output. \
                Default is 'json'.
        :type response: :mod:`string`

        :returns: one of 'html', 'json', or 'pdf'.

        :raises ValueError: If no dataset can be found for the supplied url_upload \
                or if the requested dataset is a multi-file dataset.

        '''

        try:
            if not os.path.exists(file_upload):
                raise Exception(
                    "The file you are trying to upload does not exist in the local machine.")

            files = {'file-upload': open(file_upload, 'rb+')}
            data = {'CF': 'on', 'ACDD': 'on', 'ACDD-version': acdd_version,
                    'GDS2': 'on', 'GDS2-parameters': gds2_parameters, 'response': 'json'}
            result = requests.post(self.URL, files=files, data=data)
            if result.status_code == 404 or result.status_code == 400 or result.status_code == 503 or result.status_code == 408:
                result.raise_for_status()

        except requests.exceptions.HTTPError as error:
            print(error)
            raise

        except Exception:
            raise

        return result.text
