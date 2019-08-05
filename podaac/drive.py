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

import configparser
import gzip
import os
import requests
from requests.auth import HTTPBasicAuth


class Drive:

    def __init__(self, file, username, password, webdav_url='https://podaac-tools.jpl.nasa.gov/drive/files'):
        ''' In order to access PODAAC Drive, all users are required to be registered \
           with NASA Earthdata system. User can login to the PODAAC Drive using the \
           following link https://podaac-tools.jpl.nasa.gov/drive/. \
           Once you have authenticated, you will be able to view, retrieve and change \
           your encrypted password. N.B. The encrypted password must then either be entered \
           into `podaac.ini` and passes as an argument to `file`, or alternatively provided \
           via the `username` parameter.
        '''
        config = configparser.ConfigParser()
        if file:
            config_file_path = os.path.join(os.path.dirname(__file__), "tests", file)
            config.read_file(open(config_file_path, 'r'))
            self.USERNAME = config['drive']['urs_username']
            self.PASSWORD = config['drive']['urs_password']
            self.URL = config['drive']['webdav_url']
        if username:
            self.USERNAME = username
        if password:
            self.PASSWORD = password
        if webdav_url:
            self.URL = webdav_url

    def mine_drive_urls_from_granule_search(self, granule_search_response=''):
        ''' Convenience function which extracts the PO.DAAC Drive URLs from \
           a given granule search obtained using podaac.granule_search(). \
           The response of this function is an array of strings denoting the \
           PO.DAAC Drive URLs to the granules.

           :param granule_search_response: the output response of a podaac.granule_search()
            :type path: :mod:`string`

            :returns: prints an array of PO.DAAC Drive URLs.
        '''
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(granule_search_response, 'html.parser')
        drive_list = []
        for drive_link in soup.find_all('link'):
            href = drive_link.get('href')
            if self.URL in href:
                drive_list.append(href)
        return drive_list

    def download_granules(self, granule_collection=None, path=''):
        ''' Granule download service downloads a granule collection \
            from PO.DAAC Drive to the users' local machine at the given path. Note, as \
            of https://github.com/nasa/podaacpy/issues/131 we now maintain the PO.DAAC \
            Drive directory structure. This is to say, if the Drive URL was \
            https://podaac-tools.jpl.nasa.gov/drive/files/allData/ghrsst/data/GDS2/L2P/AVHRR19_L/NAVO/v1/2019/088/20190329001403-NAVO-L2P_GHRSST-SST1m-AVHRR19_L-v02.0-fv01.0.nc \
            then a directory structure would be created as follows \
            allData/ghrsst/data/GDS2/L2P/AVHRR19_L/NAVO/v1/2019/088/20190329001403-NAVO-L2P_GHRSST-SST1m-AVHRR19_L-v02.0-fv01.0.nc

            :param granule_collection: a populated collection of PO.DAAC Drive Granule URLs. \
                These can be obtained by using the drive.mine_drive_urls_from_granule_search() \
                function which itself merely wraps a podaac.granule_search() request.
            :type granule_collection: :mod:`string`

            :param path: path to a directory where you want the data to be stored.
            :type path: :mod:`string`

            :returns: a zip file downloaded and extracted in the destination \
                directory path provided.
        '''
        if granule_collection is None:
            granule_collection = []

        for granule_url in granule_collection:
            directory_structure, granule = os.path.split(granule_url[46:])
            granule_name = os.path.splitext(granule)[0]
            if path == '':
                granule_path = os.path.join(os.path.dirname(__file__), directory_structure)
            else:
                granule_path = path + '/' + directory_structure
            r = requests.get(granule_url, auth=HTTPBasicAuth(self.USERNAME, self.PASSWORD), stream=True)
            if r.status_code != 200:
                raise PermissionError("Granule: '%s' not downloaded. Please check authentication configuration and try again." % (granule))
            try:
                from pathlib import Path
            except ImportError:
                from pathlib2 import Path  # python 2 backport
            Path(granule_path).mkdir(parents=True, exist_ok=True)
            with open(granule_path + "/" + granule, 'wb') as f:
                for chunk in r:
                    f.write(chunk)

            if granule.endswith('.gz'):
                gzip_granule = gzip.open(granule_path + "/" + granule, 'rb')
                with open(granule_path + "/" + granule_name, 'wb') as uncompressed_granule:
                    uncompressed_granule.write(gzip_granule.read())
                    gzip_granule.close()
                    uncompressed_granule.close()
                    os.remove(granule_path + "/" + granule)
