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
The following document explains how to quickly get up and running with podaacpy. It explains how to execute the key commands and explains (at a high level) what those commands are doing e.g. what input and output we can expect. More detail on expressive use of the various API's including function level API documentation can be found in subsequent pages of this documentation guide.

.. _data:

Working with Data Webservices
-----------------------------

Importing podaacpy
^^^^^^^^^^^^^^^^^^
This is very simple... ::
  
  import podaacpy

Convenience Functions
^^^^^^^^^^^^^^^^^^^^^
There are a number of convenience functions which aid various types of search. These help decypher the cryptic dataset id's, dataset short names, etc. The functions are; ::


   result = podaacpy.list_available_granule_search__datasetIds()

   result = podaacpy.list_available_granule_search_datasetShortNames()

   result = podaacpy.list_available_granule_search_level2_datasetIds()

   result = podaacpy.list_available_granule_search_level2_datasetShortNames()

   result = podaacpy.list_available_image_granule_datasetIds()

   result = podaacpy.list_available_image_granule_datasetShortNames()

   result = podaacpy.list_available_extract_granule_datasetIds():
  
   result = podaacpy.list_available_extract_granule_datasetShortNames():

For all of the above, the variable **result** now contains a Python List containing comma-separated values which can be processed appropriately.
For more information on these functions, see A, B, C, D, E, F, G, H

Retrieving Dataset Metadata
^^^^^^^^^^^^^^^^^^^^^^^^^^^
`Dataset Metadata <http://podaac.jpl.nasa.gov/ws/search/dataset/index.html>`_ - retrieves the metadata of a dataset. In the following code snippet lets retrieve dataset metadata for GHRSST Level 2P Atlantic Regional Skin Sea Surface Temperature from the Spinning Enhanced Visible and InfraRed Imager (SEVIRI) on the Meteosat Second Generation (MSG-2) satellite e.g. dataset id **PODAAC-GHMG2-2PO01** ::

  result = podaacpy.load_dataset_md(datasetId='PODAAC-GHMG2-2PO01')

The variable **result** now contains an XML response which can be processed appropriately.
For more information on this function, see X

Retrieving Granule Metadata
^^^^^^^^^^^^^^^^^^^^^^^^^^^
`Granule Metadata <http://podaac.jpl.nasa.gov/ws/metadata/granule/index.html>`_ - retrieves the metadata of a granule. In the following code snippet we retrieve granule metadata for the above dataset e.g. granuleName **20120912-MSG02-OSDPD-L2P-MSG02_0200Z-v01.nc** ::

  result = podaacpy.load_granule_md(datasetId='PODAAC-GHMG2-2PO01', granuleName='20120912-MSG02-OSDPD-L2P-MSG02_0200Z-v01.nc')

The variable **result** now contains an XML response which can be processed appropriately.
For more information on this function, see X

Additionally, we can search metadata for list of granules archived within the last 24 hours in `Datacasting <http://datacasting.jpl.nasa.gov/xml_specification/>`_ format. ::

  result = load_last24hours_datacasting_granule_md(datasetId='PODAAC-GHMG2-2PO01')

The variable **result** now contains an XML response containing a list of data granules which can be processed appropriately.
For more information on this function, see X

Searching for Datasets
^^^^^^^^^^^^^^^^^^^^^^
`Search Dataset <http://podaac.jpl.nasa.gov/ws/search/dataset/index.html>`_ - searches PO.DAAC's dataset catalog, over Level 2, Level 3, and Level 4 datasets. In the following code snippet we will search using a keyword e.g. **modis** ::

   result = podaacpy.search_dataset(keyword='modis')

The variable **result** now contains an XML response containing a list of datasets which can be processed appropriately.
For more information on this function, see X

Searching for Granules
^^^^^^^^^^^^^^^^^^^^^^^
`Search Granule <http://podaac.jpl.nasa.gov/ws/search/granule/index.html>`_ - does granule searching on PO.DAAC level 2 swath datasets (individual orbits of a satellite), and level 3 & 4 gridded datasets (time averaged to span the globe). In the following code snippet we will search for granules within a specific dataset e.g. **PODAAC-ASOP2-25X01** ::

   result = podaacpy.search_granule(datasetId='PODAAC-ASOP2-25X01')

The variable **result** now contains an XML response containing a list of granules for the given dataset which can be processed appropriately.
For more information on this function, see X

Retrieve granule images
^^^^^^^^^^^^^^^^^^^^^^^
`Image Granule <http://podaac.jpl.nasa.gov/ws/image/granule/index.html>`_ - renders granules in the PO.DAAC's catalog to images such as jpeg and/or png. In the following code snippet we display a GetMap request ::

   result = podaacpy.load_image_granule(shortName='ASCATB-L2-25km', granuleName='ascat_20121114_035403_metopb_00817_eps_o_250_2101_ovw.l2.nc', request='GetMap', layers='wind_speed_selection', styles='', version='1.3.0', format='image/png', srs='', bbox='-180,-66.43,180,79.91', height='300', width='600', service='WMS', transparent='True')

The above request returns us a nice image shown below

.. image:: granule.png

Exract a granule
^^^^^^^^^^^^^^^^
`Extract Granule <http://podaac.jpl.nasa.gov/ws/extract/granule/index.html>`_ - subsets a granule in PO.DAAC catalog and produces either netcdf3 or hdf4 files. In the following code snippet we extract a granule with Dataset ID = **PODAAC-QSX25-L2B02**, shortName of **QSCAT_LEVEL_2B_V2**, granuleName **QS_S2B54295.20093261514**, offset the region contained within **-135.0 W, 30.0 N, -120.0 W, 40.0 N** and have it saved as **netcdf** ::

   result = podaacpy.extract_granule(shortName='ASCATA-L2-25km', granuleName='ascat_20130719_230600_metopa_35024_eps_o_250_2200_ovw.l2.nc', bbox='-180,-90,180,90', format='netcdf')

The above request returns the relevant .netcdf file.

.. _mcc:

Working with Metadata Compliance Webservices (mcc)
--------------------------------------------------

Importing mcc
^^^^^^^^^^^^^^^^^^
This is very simple... ::
  
  import mcc

.. _concl:

Conclusion
----------
