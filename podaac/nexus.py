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

from nexuscli import nexuscli
from nexuscli import nexuscli_ow

class NEXUS:

    
    def __init__(self):
        self.set_target(target='https://oceanworks.jpl.nasa.gov/')

    def daily_difference_average(self, dataset, bounding_box, start_datetime, end_datetime):
        '''Generate an anomaly Time series for a given dataset, bounding box, and datetime range.

        :param dataset: Name of the dataset as a String
        :type target: :mod:`string`

        :param bounding_box: Bounding box for area of interest as a `shapely.geometry.polygon.Polygon`
        :type target: :mod:`string`

        :param start_datetime: Start time as a `datetime.datetime`
        :type target: :mod:`string`

        :param end_datetime: End time as a `datetime.datetime`
        :type target: :mod:`string`

        :returns: List of `nexuscli.nexuscli.TimeSeries` namedtuples

        '''
        return nexuscli.daily_difference_average(dataset, bounding_box, start_datetime, end_datetime)

    def dataset_list(self):
        '''Get a list of datasets and the start and end time for each.

        :returns: List of datasets

        '''

        return nexuscli.dataset_list()

    def set_target(self, target='https://oceanworks.jpl.nasa.gov/'):
        '''Enables flexible specification of the NEXUS endpoint. The \
        endpoint must be defined as follows http://host:port e.g. \
        https://oceanworks.jpl.nasa.gov/ which is set by default if no \
        argument is provided.

        :param target: HTTP(S) location of NEXUS endpoint
        :type target: :mod:`string`

        '''

        nexuscli.set_target(target)

    def subset(self, dataset, bounding_box, start_datetime, end_datetime, parameter, metadata_filter):
        '''Fetches point values for a given dataset and geographical area or metadata criteria and time range.

        :param dataset Name of the dataset as a String
        :type target: :mod:`string`

        :param bounding_box Bounding box for area of interest as a `shapely.geometry.polygon.Polygon`
        :type target: :mod:`string`

        :param start_datetime Start time as a `datetime.datetime`
        :type target: :mod:`string`

        :param end_datetime End time as a `datetime.datetime`
        :type target: :mod:`string`

        :param parameter The parameter of interest. One of 'sst', 'sss', 'wind' or None
        :type target: :mod:`string`

        :param metadata_filter List of key:value String metadata criteria
        :type target: :mod:`string`

        :returns: List of `nexuscli.nexuscli.Point` namedtuples

        '''

        return nexuscli.subset(dataset, bounding_box, start_datetime, end_datetime, parameter, metadata_filter)

    def time_series(self, datasets, bounding_box, start_datetime, end_datetime, spark=True):
        '''Send a request to NEXUS to calculate a time series.

        :param datasets Sequence (max length 2) of the name of the dataset(s)
        :type target: :mod:`string`

        :param bounding_box Bounding box for area of interest as a `shapely.geometry.polygon.Polygon`
        :type target: :mod:`string`

        :param start_datetime Start time as a `datetime.datetime`
        :type target: :mod:`string`

        :param end_datetime End time as a `datetime.datetime`
        :type target: :mod:`string`

        :param spark Optionally use spark. Default: `False`
        :type target: :mod:`string`

        :returns: List of `nexuscli.nexuscli.TimeSeries` namedtuples

        '''

        return nexuscli.time_series(datasets, bounding_box, start_datetime, end_datetime, spark)

class NEXUSOW:

    
    def __init__(self):
        self.set_target(target='https://oceanworks.jpl.nasa.gov/')

    def run_file(self, filename):
        '''The code in the file passed to run_file must be valid Pyspark code. \
        Furthermore, it must have a main function that takes exactly one \
        argument, the SparkContext. The code can make use of that SparkContext \
        variable, but should not create the SparkContext.

        :param filename: Local file containing valid Pyspark code
        :type filename: :mod:`string`

        '''

        return nexuscli_ow.run_file(filename)

    def run_string(self, code_string):
        '''The code passed to run_str can also be a multi-line string containing \
        valid Python code. It can also be a multi-line string containing \
        valid pyspark code.  For pyspark code the variable sc may be used to \
        access the SparkContext,  but it should not create the SparkContext.

        :param code_string: String specifying valid Pyspark code
        :type code_string: :mod:`string`

        '''

        return nexuscli_ow.run_str(code)

    def set_target(self, target='https://oceanworks.jpl.nasa.gov/'):
        '''Enables flexible specification of the NEXUSOW endpoint. The \
        endpoint must be defined as follows http://host:port e.g. \
        https://oceanworks.jpl.nasa.gov/ which is set by default if no \
        argument is provided.

        :param target: HTTP(S) location of NEXUSOW endpoint
        :type target: :mod:`string`

        '''

        nexuscli_ow.set_target(target)

