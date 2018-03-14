# Copyright 2016-2018 California Institute of Technology.
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

import requests
from future.moves.urllib.request import urlretrieve
from future.moves.urllib.parse import urlparse
import os

SEARCH_URL = 'https://oceandata.sci.gsfc.nasa.gov/api/file_search?'
#GET_URL = 'https://oceandata.sci.gsfc.nasa.gov/cgi/getfile/'
HEADERS = {
    'User-Agent': 'Podaacpy Python Library'
}

class OceanColor:

    def __init__(self):
        self.SEARCH_URL = 'https://oceandata.sci.gsfc.nasa.gov/api/file_search?'
        #self.GET_URL = 'https://oceandata.sci.gsfc.nasa.gov/cgi/getfile/'

    def file_search(self, sensor='', sdate='', edate='', dtype='', add_url='1', results_as_file='1',
                       search='', sub_id='', std_only='1', cksum='', output_format='json'):
        '''File search service retrieves publically available files within the \
                NASA Ocean Data Processing System.

        :param sensor: mission name. valid options include: aquarius, seawifs, \
                aqua, terra, meris, octs, czcs, hico, viirs
        :type sensor: :mod:`string`

        :param sdate: start date for a search
        :type sdate: :mod:`string`

        :param edate: end date for a search
        :type edate: :mod:`string`

        :param dtype: data type (i.e. level). valid options: L0, L1, L2, L3b \
                (for binned data), L3m (for mapped data), MET (for ancillary \
                data), misc (for sundry products)
        :type dtype: :mod:`string`

        :param add_url: include full url in search result (boolean, \
                1=yes, 0=no)
        :type add_url: :mod:`string`

        :param results_as_file: return results as a test file \
                listing (boolean, 1=yes, 0=no, thus returns and HTML page)
        :type results_as_file: :mod:`string`

        :param search: text string search
        :type search: :mod:`string`

        :param sub_id: non-extracted subscription ID to search
        :type sub_id: :mod:`string`

        :param std_only: restrict results to standard products \
                (i.e. ignore extracts, regional processings, etc.; boolean)
        :type std_only: :mod:`string`

        :param cksum: return a checksum file for search results \
                (boolean; sha1sums except for Aquarius soil moisture \
                products which are md5sums; forces results_as_file; ignores addurl)
        :type cksum: :mod:`string`

        :param output_format: valid options are: 'json', 'txt' and 'html'
        :type output_format: :mod:`string`

        :returns: by default a json response based on the requested 'output_format'. Options \
        are 'json, 'txt' and 'html'.

        '''
        try:
            url = SEARCH_URL
            if sensor:
                url = url + 'sensor=' + sensor
            else:
                raise Exception("'sensor' parameter is required!")
            if sdate:
                url = url + '&sdate=' + sdate
            if edate:
                url = url + '&edate=' + edate
            if dtype:
                url = url + '&dtype=' + dtype
            url = url + '&addurl=' + str(add_url)
            url = url + '&results_as_file=' + str(results_as_file)
            if search:
                url = url + '&search=' + search
            elif sub_id:
                url = url + '&subID=' + sub_id
            else:
                raise Exception("Either 'search' or 'sub_id' parameter is required!")
            url = url + '&std_only=' + str(std_only)
            if cksum:
                url = url + '&cksum=' + cksum
            url = url + '&format=' + output_format

            response = requests.post(url, headers=HEADERS)
            status_codes = [404, 400, 503, 408]
            if response.status_code in status_codes:
                response.raise_for_status()

        except requests.exceptions.HTTPError as error:
            print(error)
            raise

        return response.text

    def get_file(self, url='', path=''):
        '''It is possible to mimic FTP bulk data downloads using the \
                HTTP-based data distribution server at https://oceandata.sci.gsfc.nasa.gov.

        :param url: a single file name which can be obtained by calling #file_search() \
                an example would be \
                https://oceandata.sci.gsfc.nasa.gov/cgi/getfile/O1997001.L3b_DAY_CHL.nc
        :type url: :mod:`string`

        :param path: Destination directory into which the granule \
                needs to be downloaded.
        :type path: :mod:`string`

        :returns: a file object downloaded from the \
                HTTP-based data distribution server at https://oceandata.sci.gsfc.nasa.gov.

        '''
        try:
            #url = GET_URL
            if url:
                url = url
            else:
                raise Exception("'file' parameter is required!")
            file = os.path.basename(urlparse(url).path)
            if path == '':
            	path = os.path.join(os.path.dirname(__file__), file)
            else:
                path = path + '/' + file
            urlretrieve(url, path)
            print("Downloaded '%s' to '%s'" % (file, path))
            return file

        except Exception:
            raise
