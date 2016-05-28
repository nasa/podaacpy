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


from .. import mcc
import os 
import json 

def test_check_remote_file():
	data = mcc.check_remote_file('CF', 'https://github.com/ioos/compliance-checker/raw/master/compliance_checker/tests/data/2dim-grid.nc')

	assert data != None

	data_json = json.loads(data)

	assert data_json["model"] == "NETCDF4"

	assert data_json["fn"] == "https://github.com/ioos/compliance-checker/raw/master/compliance_checker/tests/data/2dim-grid.nc"




def test_check_local_file(): 
	path = os.path.join(os.path.dirname(__file__), 'ascat_20130719_230600_metopa_35024_eps_o_250_2200_ovw.l2_subsetted_.nc')
	data = mcc.check_local_file(1.1, 'L2P', path)

	assert data != None 

	data_json = json.loads(data)

	assert data_json["model"] == "NETCDF3_CLASSIC"

	assert data_json["fn"] == "ascat_20130719_230600_metopa_35024_eps_o_250_2200_ovw.l2_subsetted_.nc"

