# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import requests
import urllib
import os
import xml.etree.ElementTree as ET

URL = 'http://podaac.jpl.nasa.gov/ws/'


class Podaac:

    def __init__(self):
        self.URL = 'http://podaac.jpl.nasa.gov/ws/'

    def load_dataset_md(self, dataset_id='', short_name='', format='iso'):
        '''Dataset metadata service retrieves the metadata of a \
                dataset on PO.DAACs dataset catalog using the following \
                parameters: dataset_id, short_name, and format.

        :param dataset_id: dataset persistent ID. dataset_id or short_name \
                is required for this metadata service.
        :type dataset_id: :mod:`string`

        :param short_name: dataset short_name. dataset_id or short_name \
                is required for this metadata service.
        :type short_name: :mod:`string`

        :param format: metadata format. Default format is iso.
        :type format: :mod:`string`

        :returns: an xml response based on the requested 'format'. Options \
        are 'iso' and 'gcmd'.

        '''
        try:
            url = self.URL + 'metadata/dataset/?datasetId=' + \
                dataset_id + '&shortName=' + short_name + '&format=' + format
            metadata = requests.get(url)
            if metadata.status_code == 404 or metadata.status_code == 400 or metadata.status_code == 503 or metadata.status_code == 408:
                metadata.raise_for_status()

        except requests.exceptions.HTTPError as error:
            print(error)
            raise

        return metadata.text

    def load_granule_md(self, dataset_id='', short_name='', granule_name='', format='iso'):
        '''Granule metadata service retrieves the metadata of a granule \
                on PO.DAACs catalog in ISO-19115.

        :param dataset_id: dataset persistent ID. dataset_id or short_name \
                is required for this metadata service.
        :type dataset_id: :mod:`string`

        :param short_name: dataset short_name. dataset_id or short_name \
                is required for this metadata service.
        :type short_name: :mod:`string`

        :param granule_name: granule name. granule name is required \
                for this metadata service.
        :type granule_name: :mod:`string`

        :param format: metadata format. Default format is iso.
        :type format: :mod:`string`

        :returns: an xml response based on the requested 'format'.

        '''

        try:
            url = self.URL + 'metadata/granule?datasetId=' + dataset_id + '&shortName=' + \
                short_name + '&granuleName=' + granule_name + '&format=' + format
            granule_md = requests.get(url)
            if granule_md.status_code == 404 or granule_md.status_code == 400 or granule_md.status_code == 503 or granule_md.status_code == 408:
                granule_md.raise_for_status()

        except requests.exceptions.HTTPError as error:
            print(error)
            raise

        return granule_md.text

    def load_last24hours_datacasting_granule_md(self, dataset_id='', short_name='', format='datacasting', items_per_page=7):
        '''Granule metadata service retrieves metadata for a list \
                of granules archived within the last 24 hours in Datacasting \
                format.

        :param dataset_id: dataset persistent ID. dataset_id or short_name \
                is required for this metadata service.
        :type dataset_id: :mod:`string`

        :param short_name: dataset short_name. dataset_id or short_name \
                is required for this metadata service.
        :type short_name: :mod:`string`

        :param format: metadata format. Must set to 'datacasting'.
        :type format: :mod:`string`

        :param items_per_page: number of results per page. Default value is 7. \
                The value range is from 0 to 5000.
        :type items_per_page: :mod:`int`

        :returns: an xml response based on the requested 'format'. Options \
                are 'iso' and 'gcmd'.

        '''

        try:
            url = self.URL + 'metadata/granule?datasetId=' + dataset_id + '&shortName=' + \
                short_name + '&itemsPerPage=' + \
                str(items_per_page) + '&format=' + format
            granule_md = requests.get(url)
            if granule_md.status_code == 404 or granule_md.status_code == 400 or granule_md.status_code == 503 or granule_md.status_code == 408:
                granule_md.raise_for_status()

        except requests.exceptions.HTTPError as error:
            print(error)
            raise

        return granule_md.text

    def search_dataset(self, keyword='', start_time='', end_time='', start_index='', dataset_id='', short_name='', instrument='', satellite='', file_format='', status='', process_level='', sort_by='', bbox='', items_per_page='7', pretty='True', format='atom', full='False'):
        '''Dataset Search service searches PO.DAAC's dataset catalog, over \
                Level 2, Level 3, and Level 4 datasets, using the following parameters: \
                dataset_id, short_name, start_time, end_time, bbox, and others.

        :param keyword: keyword specifies search text to search for datasets. \
                Example: 'modis'
        :type keyword: :mod:`string`

        :param start_time: start time in the format of YYYY-MM-DDTHH:mm:ssZ. \
                'Z' is the time-offset, where 'Z' signifies UTC or an actual \
                offset can be used. Example: 2012-01-22T01:21:21Z
        :type start_time: :mod:`time`

        :param end_time: stop time in the format of YYYY-MM-DDTHH:mm:ssZ. \
                'Z' is the time-offset, where 'Z' signifies UTC or an actual \
                offset can be used. Example: 2012-01-22T01:21:21Z
        :type end_time: :mod:`time`

        :param start_index: start index of entries found for search. Example: 1
        :type start_index: :mod:`int`

        :param items_per_page: number of results per page for \
                opensearch result. If format is not specified, format is set \
                to 7. The value range is from 0 to 400
        :type items_per_page: :mod:`int`

        :param dataset_id: dataset persistent ID. \
                Example: PODAAC-MODSA-T8D9N
        :type dataset_id: :mod:`string`

        :param short_name: dataset short_name. \
                Example: MODIS_AQUA_L3_SST_THERMAL_8DAY_9KM_NIGHTTIME
        :type short_name: :mod:`string`

        :param instrument: dataset instrument. Example: MODIS
        :type instrument: :mod:`string`

        :param satellite: dataset satellite. Example: AQUA
        :type satellite: :mod:`string`

        :param file_format: dataset data format. \
                Possible values: HDF, NetCDF
        :type file_format: :mod:`string`

        :param status: dataset status. \
                Possible values: OPEN, PREVIEW, SIMULATED, RETIRED
        :type status: :mod:`string`

        :param processLevel: dataset processing level. \
                Possible values: 1B, 2, 2P, 3, 4
        :type processLevel: :mod:`string`

        :param pretty: "true" to enable pretty output for xml. \
                If pretty is not specified, pretty is set to true.
        :type pretty: :mod:`boolean`

        :param format: response format. If format is not specified, \
                format is set to atom. Possible values: atom, html.
        :type format: :mod:`string`

        :param sort_by: determines ordering of response. If sort_by \
                is not specified, sort order is by score (most relevant \
                dataset first). Possible values: timeAsc, timeDesc, \
                popularityAsc, popularityDesc.
        :type sort_by: :mod:`string`

        :param bbox: bounding box for spatial search. format \
                should look like "bbox=0.0,-45.0,180.0,40.0" which is \
                in order of west, south, east, north. Longitude values needs \
                to be in range of [-180.0,180.0]. Example: 0.0,-45.0,180.0,40.0
        :type bbox: :mod:`string`

        :param full: "true" to return response with complete PO.DAAC \
                metadata per entry. If full is not specified, full is set to false. \
                Possible values: true, false
        :type full: :mod:`string`

        :returns: the specified response format. If format is not specified, \
                format is set to atom. Possible values: atom, html

        '''
        try:
            url = self.URL + 'search/dataset/?keyword=' + keyword + '&start_time=' + start_time + '&end_time=' + end_time + '&start_index=' + start_index + '&dataset_id=' + dataset_id + '&short_name=' + short_name + '&instrument=' + instrument + '&satellite=' + \
                satellite + '&fileFormat=' + file_format + '&status=' + status + '&processLevel=' + process_level + '&sort_by=' + sort_by + \
                '&bbox=' + bbox + '&itemsPerPage=' + items_per_page + \
                '&pretty=' + pretty + '&format=' + format + '&full=' + full
            datasets = requests.get(url)
            if datasets.status_code == 404 or datasets.status_code == 400 or datasets.status_code == 503 or datasets.status_code == 408:
                datasets.raise_for_status()

        except requests.exceptions.HTTPError as error:
            print(error)
            raise

        return datasets.text

    def search_granule(self, dataset_id='', short_name='', start_time='', end_time='', bbox='', start_index='', sort_by='timeAsc', items_per_page='7', format='atom', pretty='True'):
        '''Search Granule does granule searching on PO.DAAC level 2 swath \
                datasets (individual orbits of a satellite), and level 3 & 4 \
                gridded datasets (time averaged to span the globe). Coverage \
                footpritnt polygons are used to enable spatial search on level 2 \
                swath dataset. Currently, our footprints can contain no data and \
                also gaps in the swath data. Spatial search on level 2 data can \
                return granules where actual data does not intersect the selected \
                bounding box but its footprint intersects the selected bounding \
                box. The following parameters are supported: dataset_id, \
                short_name, start_time, end_time, bbox, and others.

        :param dataset_id: dataset persistent ID. dataset_id or short_name \
                is required for a granule search. Example: PODAAC-ASOP2-25X01
        :type dataset_id: :mod:`string`

        :param short_name: dataset short_name. dataset_id or short_name is \
                required for a granule search. Example: ASCATA-L2-25km
        :type short_name: :mod:`string`

        :param start_time: start time in the format of YYYY-MM-DDTHH:mm:ssZ. \
                'Z' is the time-offset, where 'Z' signifies UTC or an actual offset \
                can be used. Example: 2013-01-01T01:30:00Z
        :type start_time: :mod:`time`

        :param end_time: stop time in the format of YYYY-MM-DDTHH:mm:ssZ. \
                'Z' is the time-offset, where 'Z' signifies UTC or an actual \
                offset can be used. Example: 2014-01-01T00:00:00Z
        :type end_time: :mod:`time`

        :param bbox: bounding box for spatial search. format should look \
                like "bbox=0,0,180,90" which is in order of west, south, east, \
                north. Longitude values needs to be in range of [-180, 180]. \
                Latitude values needs to be in range of [-90, 90]. For level \
                2 datasets, spatial search is available for a subset. Call the \
                list_available_Level2_dataset_ids and \
                list_available_level2_datasetShortNames functions to see the \
                subset. BBox example: 0,0,180,90
        :type bbox: :mod:`string`

        :param start_index: start index of entries found for search. \
                Example: 1
        :type start_index: :mod:`int`

        :param items_per_page: number of results per page for opensearch \
                result. If format is not specified, format is set to 7. The \
                value range is from 0 to 400
        :type items_per_page: :mod:`int`

        :param sort_by: determines ordering of response. Possible \
                values: timeAsc, timeDesc.
        :type sort_by: :mod:`string`

        :param format: response format. If format is not specified, \
                format is set to atom. Possible values: atom, html.
        :type format: :mod:`string`

        :param pretty: "true" to enable pretty output for xml. \
                If pretty is not specified, pretty is set to true. Possible \
                values: true, false.
        :type pretty: :mod:`boolean`

        :returns: an xml response based on the requested 'format'. Options \
                are 'atom' and 'html'.

        '''

        try:
            if(bbox == ''):
                url = self.URL + 'search/granule/?datasetId=' + dataset_id + '&shortName=' + short_name + '&startTime=' + start_time + '&endTime=' + \
                    end_time + '&startIndex=' + start_index + '&sortBy=' + sort_by + \
                    '&itemsPerPage=' + items_per_page + '&format=' + format + '&pretty=' + pretty
            else:
                url = self.URL + 'search/granule/?datasetId=' + dataset_id + '&shortName=' + short_name + '&startTime=' + start_time + '&endTime=' + end_time + \
                    '&bbox=' + bbox + '&startIndex=' + start_index + '&sortBy=' + sort_by + \
                    '&itemsPerPage=' + items_per_page + '&format=' + format + '&pretty=' + pretty
            granules = requests.get(url)
            if granules.status_code == 404 or granules.status_code == 400 or granules.status_code == 503 or granules.status_code == 408:
                granules.raise_for_status()

        except requests.exceptions.HTTPError as error:
            print(error)
            raise

        return granules.text

    def load_image_granule(self, dataset_id='', short_name='', granule_name='', bbox='', height='', width='', style='', srs='', request='GetMap', service='WMS', version='1.3.0', format='image/png', layers='', path=''):
        '''The PODAAC Image service renders granules in the \
                PO.DAACs catalog to images such as jpeg and/or png. \
                This image service also utilizes OGC WMS protocol. \
                (http://www.opengeospatial.org/standards/wms). If the \
                granule does not have any data in the given selected \
                bounding box, HTTP 500 will be thrown since there is \
                no data to be imaged. Granule Search service can be used \
                to find level 2 swath data. However, the level 2 \
                spatial search uses coverage footprint polygons \
                generated for each granule, and this footprint can \
                contain no data or gaps. If the selected bounding box \
                resides on no data or gaps, HTTP 500 will be thrown. \
                There are three request methods in this service. They \
                are GetCapabilities, GetLegendGraphic, and GetMap.

        :param dataset_id: dataset persistent ID. dataset_id or \
                short_name is required for a granule search. Example: \
                PODAAC-ASOP2-25X01 :mod:`string`
        :type dataset_id: :mod:`string`

        :param short_name: the shorter name for a dataset. \
                Either short_name or dataset_id is required for a \
                granule search. Example: ASCATA-L2-25km
        :type short_name: :mod:`string`

        :param granule_name: name of the granule. \
                Specifying granule_name insures only that granule \
                is returned. Example: \
                ascat_20130719_230600_metopa_35024_eps_o_250_2200_ovw.l2.nc
        :type granule_name: :mod:`string`

        :param request: The service response requested. Valid \
                entries for WMS 1.3.0 are GetCapabilities, GetMap, \
                GetLegendGraphic. Example: request=GetMap
        :type request: :mod:`string`

        :param service: service should be set to WMS. \
                Example: service=WMS
        :type service: :mod:`string`

        :param version: The WMS version of the client, accepts \
                values of 1.3.0 Example: version=1.3.0
        :type version: :mod:`string`

        :param format: Image format. Format is required for \
                GetMap and GetLegendGraphic. Possible value : image/png
        :type format: :mod:`string`

        :param bbox: bounding box for spatial search. format should \
                look like "bbox=45,0,180,90" which is in order of \
                west, south, east, north. Longitude values needs to \
                be in range of [-180, 180]. Latitude values needs to \
                be in range of [-90, 90]. bbox is used for getMap \
                request. Example: 45,0,180,90
        :type bbox: :mod:`string`

        :param height: Maximum height in pixels of the image. \
                Height is required for getMap request. Example: 300
        :type height: :mod:`int`

        :param width: Maximum width in pixels of the image. \
                width is used for getMap request. Example: 200
        :type width: :mod:`int`

        :param layers: A variable to image. This can be \
                left blank, which then selects the default layer. \
                layer is required for GetMap and GetLegendGraphic request. \
                Example: wind_speed
        :type layers: :mod:`string`

        :param style: A colorbar to use when creating \
                the image. This can be left blank, which then \
                selects the default style. style is required in \
                GetMap and GetLegendGraphic request. Example: \
                paletteMedspirationIndexed
        :type style: :mod:`string`

        :param srs: The spatial reference system to project \
                the data to. Currently only supports EPSG:4326. \
                srs is used for getMap request. Leave blank for \
                default projection. Example: EPSG:4326
        :type srs: :mod:`string`

        :param path: Destination directory into which the image\
                needs to be downloaded.
        :type format: :mod:`string`

        :returns: a png image file.

        '''

        try:
            url = self.URL + 'image/granule/?datasetId=' + dataset_id + '&shortName=' + short_name + '&granuleName=' + granule_name + '&request=' + request + '&bbox=' + bbox + \
                '&height=' + height + '&width=' + width + '&style=' + style + '&srs=' + srs + \
                '&service=' + service + '&version=' + version + \
                '&format=' + format + '&layers=' + layers
            if path == '':
                path = os.path.join(os.path.dirname(
                    __file__), dataset_id + '.png')
            else:
                path = path + '/' + dataset_id + '.png'
            image = urllib.urlretrieve(url, path)
            if image[1].getheader('Content-Type') == 'text/plain':
                raise Exception(
                    "Service type image not availalble for this dataset : " + dataset_id)

        except Exception:
            raise

        return image

    def extract_granule(self, dataset_id='', short_name='', granule_name='', bbox='', format='', path=''):
        '''Extract service subsets a granule in PO.DAAC catalog \
        and produces either netcdf3 or hdf4 files. If the granule \
        does not have any data in the given selected bounding box, \
        HTTP 500 will be thrown since there is no data to be \
        subsetted. Granule Search service can be used to find \
        level 2 swath data. However, the level 2 spatial search \
        uses coverage footprint polygons generated for each \
        granule, and this footprint can contain no data or gaps. \
        If the selected bounding box resides on no data or gaps, \
        HTTP 500 will be thrown.

        :param dataset_id: dataset persistent ID. dataset_id or \
                short_name is required for a granule search. Example: \
                PODAAC-ASOP2-25X01
        :type dataset_id: :mod:`string`

        :param short_name: the shorter name for a dataset. \
                Either short_name or dataset_id is required for a \
                granule search. Example: ASCATA-L2-25km
        :type short_name: :mod:`string`

        :param granule_name: name of the granule. Specifying \
                granule_name insures only that granule is returned. Example: \
                ascat_20130719_230600_metopa_35024_eps_o_250_2200_ovw.l2.nc
        :type granule_name: :mod:`string`

        :param bbox: bounding box for spatial search. format \
                should look like "bbox=0.0,-45.0,180.0,40.0" which is \
                in order of west, south, east, north. Longitude values \
                needs to be in range of [-180, 180]. Latitude values \
                needs to be in range of [-90, 90]. Example: 45,0,180,90
        :type bbox: :mod:`string`

        :param format: Required. Saved file format. Possible \
                values: netcdf, hdf
        :type format: :mod:`string`

        :param path: Destination directory into which the granule\
                needs to be downloaded.
        :type format: :mod:`string`

        :returns: a netcdf file or hdf file

        '''
        try:
            url = self.URL + 'extract/granule/?datasetId=' + dataset_id + '&shortName=' + \
                short_name + '&granuleName=' + granule_name + \
                '&bbox=' + bbox + '&format=' + format
            if path == '':
                path = os.path.join(os.path.dirname(__file__), granule_name)
            else:
                path = path + '/' + granule_name
            granule = urllib.urlretrieve(url, path)
            if granule[1].getheader('Content-Type') == 'text/plain':
                raise Exception("Unexpected Error Occured")

        except Exception:
            raise

        return granule

    def extract_l4_granule(self, dataset_id='', short_name='', path=''):
        '''This is an additional fucntion that we have provided apart \
        from the availalble webservices. The extract_l4_granule helps \
        retrieve the level 4 datasets from openDap server directly, \
        accompanied by the search granule for retrieving granule name \
        related to the specific dataset_id and short_name

        :param dataset_id: dataset persistent ID. dataset_id or \
                short_name is required for a granule search. Example: \
                PODAAC-ASOP2-25X01
        :type dataset_id: :mod:`string`

        :param short_name: the shorter name for a dataset. \
                Either short_name or dataset_id is required for a \
                granule search. Example: ASCATA-L2-25km
        :type short_name: :mod:`string`

        :param path: Destination directory into which the granule\
                needs to be downloaded.
        :type format: :mod:`string`
        '''
        try:
            start_index = '1'
            search_data = self.search_granule(
                dataset_id=dataset_id, short_name=short_name, start_index=start_index)
            root = ET.fromstring(search_data.encode('utf-8'))
            url = root[12][6].attrib['href']
            url = url[:-5]
            granule_name = root[12][0].text
            granule_name = granule_name.split('\t')[3][:-1]
            if path == '':
                path = os.path.join(os.path.dirname(__file__), granule_name)
            else:
                path = path + '/' + granule_name
            granule = urllib.urlretrieve(url, path)
            if granule[1].getheader('Content-Type') == 'text/plain':
                raise Exception("Unexpected Error Occured")

        except Exception:
            raise

        return granule_name
