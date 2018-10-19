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
import ntpath
import os
import requests
import shutil
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
            config.read_file(open(file, 'r'))
        else:
            config.read('podaac.ini')
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
        for ftp_link in soup.find_all('link'):
            href = ftp_link.get('href')
            if 'ftp://podaac-ftp.jpl.nasa.gov/' in href:
                drive_list.append(href.replace('ftp://podaac-ftp.jpl.nasa.gov', self.URL))
        return drive_list

    def download_granules(self, granule_collection=[], path=''):
        ''' Granule download service downloads a granule collection \
            from PO.DAAC Drive to the users' local machine at the given path.

            :param granule_collection: a populated collection of PO.DAAC Drive granules. \
                These can be obtained by using the drive.mine_drive_urls_from_granule_search() \
                function which itself merely wraps a podaac.granule_search() request.
            :type granule_collection: :mod:`string`

            :param path: path to a directory where you want the data to be stored.
            :type path: :mod:`string`

            :returns: a zip file downloaded and extracted in the destination\
                directory path provided.
        '''
        for granule in granule_collection:
            compressed_granule = ntpath.basename(granule)
            granule_name = os.path.splitext(compressed_granule)[0]
            if path == '':
                compressed_path = os.path.join(os.path.dirname(__file__), compressed_granule)
            else:
                compressed_path = path + '/' + compressed_granule
            r = requests.get(granule, auth=HTTPBasicAuth(self.USERNAME, self.PASSWORD), stream=True)
            if r.status_code != 200:
            	raise Error("Granule: '%s' not downloaded. Please check authentication configuration and try again." % (granule))
            with open(compressed_path, 'wb') as f:
                for chunk in r:
                    f.write(chunk)

            if compressed_granule.endswith('.gz'):
                compressed_granule = gzip.open(compressed_path, 'rb')
                uncompressed_granule = open(path + '/' + granule_name, 'wb')
                uncompressed_granule.write(compressed_granule.read())
                compressed_granule.close()
                uncompressed_granule.close()
            os.remove(compressed_path)
