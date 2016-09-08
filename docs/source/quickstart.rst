.. # encoding: utf-8
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
   
Quickstart
**********

*author*: Lewis John McGibbney (lewismc@apache.org)

Purpose
-------
The following document explains how to quickly get up and running with podaac. It explains how to execute the key commands and explains (at a high level) what those commands are doing e.g. what input and output we can expect. More detail on expressive use of the various API's including function level API documentation can be found in subsequent pages of this documentation guide.

.. _data:

Working with Data Webservices
-----------------------------

Importing podaac
^^^^^^^^^^^^^^^^^^
This is very simple... ::
  
  # import the podaac package
  import podaac.podaac as podaac

  # then create an instance of the Podaac class
  p = podaac.Podaac()

More on using Podaac functions later... first lets look at some convenience functionality.

Convenience Functions
^^^^^^^^^^^^^^^^^^^^^
There are a number of convenience functions which aid various types of search. These help decypher the rather cryptic dataset id's, dataset short names, etc. present within PO.DAAC.  These functions accept no parameters. They do however account for the fact that availaility of certain datasets within PO.DAAC is not constant. Additionally some services are only available for certain datasets. The functions encapsulate those underlying variables and always return current, available results which can be interpreted and used within the other functions in this file. 

First lets define the relevant import ::
  
  # import the podaac_utils package
  import podaac.podaac_utils as utils

  # then create an instance of the PodaacUtils class
  u = utils.PodaacUtils()

The convenience functions are; ::

   result = u.list_available_granule_search_level2_dataset_ids()

   result = u.list_available_granule_search_level2_dataset_short_names()

   result = u.list_available_granule_search_dataset_ids()

   result = u.list_available_granule_search_dataset_short_names()

   result = u.list_available_extract_granule_dataset_ids():
  
   result = u.list_available_extract_granule_datasetShortNames():

For all of the above, the variable **result** now contains a Python List containing comma-separated values which can be processed appropriately.
For more information on these functions, see :doc:`utilities`

Retrieving Dataset Metadata
^^^^^^^^^^^^^^^^^^^^^^^^^^^
`Dataset Metadata <http://podaac.jpl.nasa.gov/ws/search/dataset/index.html>`_ - retrieves the metadata of a dataset. In the following code snippet lets retrieve dataset metadata for GHRSST Level 2P Atlantic Regional Skin Sea Surface Temperature from the Spinning Enhanced Visible and InfraRed Imager (SEVIRI) on the Meteosat Second Generation (MSG-2) satellite e.g. dataset id **PODAAC-GHMG2-2PO01** ::

  result = p.dataset_metadata(dataset_id='PODAAC-GHMG2-2PO01')

The variable **result** now contains an XML response which can be processed appropriately.
For more information on this function, see :doc:`webservices`

Retrieving Granule Metadata
^^^^^^^^^^^^^^^^^^^^^^^^^^^
`Granule Metadata <http://podaac.jpl.nasa.gov/ws/metadata/granule/index.html>`_ - retrieves the metadata of a granule. In the following code snippet we retrieve granule metadata for the above dataset e.g. granule_name **20120912-MSG02-OSDPD-L2P-MSG02_0200Z-v01.nc** ::

  result = p.granule_metadata(dataset_id='PODAAC-GHMG2-2PO01', granule_name='20120912-MSG02-OSDPD-L2P-MSG02_0200Z-v01.nc')

The variable **result** now contains an XML response which can be processed appropriately.
For more information on this function, see :doc:`webservices`

Additionally, we can search metadata for list of granules archived within the last 24 hours in `Datacasting <http://datacasting.jpl.nasa.gov/xml_specification/>`_ format. ::

  result = p.load_last24hours_datacasting_granule_md(dataset_id='PODAAC-GHMG2-2PO01')

The variable **result** now contains an XML response containing a list of data granules which can be processed appropriately.
For more information on this function, see :doc:`webservices`

Retrieving Dataset Variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`Dataset Variables <http://podaac.jpl.nasa.gov/ws/dataset/variables/index.html>`_ - provides a list of variable for the datset. In the following code snippet we retrieve the dataset variables for the dataset id **PODAAC-ASOP2-25X01** ::

  result = p..dataset_variables(dataset_id='PODAAC-ASOP2-25X01')

The variable **result** now contains a dictionary of variables of the respective dataset.
For more information on this function, see :doc:`webservices`

Searching for Datasets
^^^^^^^^^^^^^^^^^^^^^^
`Search Dataset <http://podaac.jpl.nasa.gov/ws/search/dataset/index.html>`_ - searches PO.DAAC's dataset catalog, over Level 2, Level 3, and Level 4 datasets. In the following code snippet we will search using a keyword e.g. **modis** ::

   result = p.dataset_search(keyword='modis')

The variable **result** now contains an XML response containing a list of datasets which can be processed appropriately.
For more information on this function, see :doc:`webservices`

Searching for Granules
^^^^^^^^^^^^^^^^^^^^^^^
`Search Granule <http://podaac.jpl.nasa.gov/ws/search/granule/index.html>`_ - does granule searching on PO.DAAC level 2 swath datasets (individual orbits of a satellite), and level 3 & 4 gridded datasets (time averaged to span the globe). In the following code snippet we will search for granules within a specific dataset e.g. **PODAAC-ASOP2-25X01** ::

   result = p.granule_search(dataset_id='PODAAC-ASOP2-25X01', bbox='0,0,180,90',start_time='2013-01-01T01:30:00Z',end_time='2014-01-01T00:00:00Z',start_index='1'))

The variable **result** now contains an XML response containing a list of granules for the given dataset which can be processed appropriately.
For more information on this function, see :doc:`webservices`

Retrieve granule images
^^^^^^^^^^^^^^^^^^^^^^^
`Granule Preview <http://podaac.jpl.nasa.gov/ws/image/granule/index.html>`_ - renders granules in the PO.DAAC's catalog to images such as jpeg and/or png. In the following code snippet we display a request using the dataset id **PODAAC-ASOP2-25X01** and image variable of the dataset **wind_speed** ::

   result = p.granule_preview(dataset_id='PODAAC-ASOP2-25X01', image_variable='wind_speed')

The above request downloads us a nice image shown below

.. image:: granule.png

For more information on this function, see :doc:`webservices`

Subsetting Granules
^^^^^^^^^^^^^^^^^^^
`Granule Subset <http://podaac.jpl.nasa.gov/ws/subset/granule/index.html>`_ - the Granule Subset web service sets up a granule subsetting job using HTTP POST request. Upon a successful request, a token is returned which can be used to check the status of the subsetting job. In the following code snippet we will subset a granule using an input.json file which contains ::

   query={ 
    "email":"abc@abcd.com",
    "query": [
        {
            "compact":false,   
            "datasetId":"PODAAC-ASOP2-25X01",
            "bbox":"-180,-90,0,90",
            "variables" : ["lat" , "lon","time","wind_speed" ],
            "granuleIds": ["ascat_20140520_005700_metopa_39344_eps_o_250_2300_ovw.l2.nc","ascat_20140411_175700_metopa_38800_eps_o_250_2300_ovw.l2.nc"]
        }
     ]
   }

   result = p.granule_subset(input_file_path='/path/to/input.json')

The variable **result** contains a token on successful request reception. This can be further used to check the status of the request.
For more information on this function, see :doc:`webservices`

Subset Status
^^^^^^^^^^^^^
`Subset Status <http://podaac.jpl.nasa.gov/ws/subset/status/index.html>`_ - the subset status checks the status on the existing job. In the following code snippet we check the status using the token received from PO.DAAC when we submitted a job for subsetting ::

   result = p.granule_preview(dataset_id='PODAAC-ASOP2-25X01', image_variable='wind_speed')

The variable **result** contains the status of the subset request.
For more information on this function, see :doc:`webservices`

Extract level4 granule
^^^^^^^^^^^^^^^^^^^^^^
Right now the `Extract Granule <http://podaac.jpl.nasa.gov/ws/extract/granule/index.html>` supports only level 2 granules. Extract l4 granule is an add-on over extract granule to extract level 4 gridded datasets from the PODAAC data source. In the following code snippet we extract a level4 granule with Dataset ID = **PODAAC-CCF30-01XXX**, short_name of **CCMP_MEASURES_ATLAS_L4_OW_L3_0_WIND_VECTORS_FLK** and provide a path to the directory you want to have it saved as **netcdf** ::

   result = p.extract_l4_granule(dataset_id='PODAAC-CCF30-01XXX', short_name='CCMP_MEASURES_ATLAS_L4_OW_L3_0_WIND_VECTORS_FLK', path='path/to/the/destination/directory')

The above request downloads the relevant .netcdf file. For more information on this function, see :doc:`webservices`

.. _mcc:

Working with Metadata Compliance Webservices (mcc)
--------------------------------------------------

Importing mcc
^^^^^^^^^^^^^
This is very simple... ::
  
  # import the mcc package
  import podaac.mcc as mcc

  # then create an instance of the MCC class
  m = mcc.MCC()

Compliance Check a Local File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The following example displays how to use the MCC to check and validate the contents of a local granule (netCDF or HDF) given the relevant input parameters. ::

    result = m.check_local_file(acdd_version='1.3', gds2_parameters='L4', file_upload='someLocalFile.nc', response='json')

The result variable contains a JSON encoded report response which can be used for compliance checking activities. For more information on this function, see :doc:`mcc`

Compliance Check a Remote File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The following example displays how to use the MCC to check and validate the contents of a remote granule (netCDF or HDF) given the relevant input parameters. ::

    result = m.check_remote_file(checkers='CF', url_upload='http://test.opendap.org/opendap/data/ncml/agg/dated/CG2006158_120000h_usfc.nc', response='json')

The result variable contains a JSON encoded report response which can be used for compliance checking activities. For more information on this function, see :doc:`mcc`

.. _concl:

Conclusion
----------
That concludes the quick start. Hopefully this has been helpful in providing an overview of the main podaacpy features. If you have any issues with this document then please register them at the `issue tracker <https://github.com/lewismc/podaacpy/issues>`_. Please use `labels <https://help.github.com/articles/applying-labels-to-issues-and-pull-requests/>`_ to classify your issue.
