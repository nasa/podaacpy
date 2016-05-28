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
   
podaacpy webservices API
************************

*author*: Lewis John McGibbney (lewismc@apache.org)

-============
-Introduction
-============
-podaacpy is a python utility library for interacting with `NASA JPL's PO.DAAC <http://podaac.jpl.nasa.gov>`_
-
-============
-What is PO.DAAC?
-============
-The Physical Oceanography Distributed Active Archive Center (PO.DAAC) is an element of the Earth Observing System Data and Information System (`EOSDIS <https://earthdata.nasa.gov/>`_). The EOSDIS provides science data to a wide community of users for NASA's Science Mission Directorate.
-What does podaacpy offer?
-
-The library provides a Python toolkit for interacting with all of PO.DAACs API's, namely
-
-    `PO.DAAC Web Services <https://podaac.jpl.nasa.gov/ws/>`_: services include
-        `Dataset Metadata <http://podaac.jpl.nasa.gov/ws/search/dataset/index.html>`_ - retrieves the metadata of a dataset
-        `Granule Metadata <http://podaac.jpl.nasa.gov/ws/metadata/granule/index.html>`_ - retrieves the metadata of a granule
-        `Search Dataset <http://podaac.jpl.nasa.gov/ws/search/dataset/index.html>`_ - searches PO.DAAC's dataset catalog, over Level 2, Level 3, and Level 4 datasets
-        `Search Granule <http://podaac.jpl.nasa.gov/ws/search/granule/index.html>`_ - does granule searching on PO.DAAC level 2 swath datasets (individual orbits of a satellite), and level 3 & 4 gridded datasets (time averaged to span the globe)
-        `Image Granule <http://podaac.jpl.nasa.gov/ws/image/granule/index.html>`_ - renders granules in the PO.DAAC's catalog to images such as jpeg and/or png
-        `Extract Granule <http://podaac.jpl.nasa.gov/ws/extract/granule/index.html>`_ - subsets a granule in PO.DAAC catalog and produces either netcdf3 or hdf4 files
-
-    `Metadata Compliance Checker <http://podaac-uat.jpl.nasa.gov/mcc>`_: an online tool and web service designed to check and validate the contents of netCDF and HDF granules for the Climate and Forecast (CF) and Attribute Convention for Dataset Discovery (ACDD) metadata conventions.
-
-
-================================
-Task Specifications/Requirements
-================================
-
-The following is a list of requirements levied by the architecture for any CDR/ECV code 
-funded through LSRD.  
-
-- The operating system is 64 bit Linux only.
-
-- The source code must be delivered. A binary is nice but all system deployments 
-  are built from source maintained at EROS. No binaries built by outside entities 
-  may be deployed to the LSRD systems.
-
-- The acceptable languages for use are C/C++ or Python.
-
-- I strongly urge you to explore NVidia CUDA with C/C++/python.  
-  We are shifting to GPU computing in order to provide adequate compute resources.
-
-- All code must be single threaded.  No multiprocess or multithreading code will 
-  fit into our architecture as it uses a many-at-once approach.  The only 
-  deviation from this is CUDA code.
-
-- No hard-coded paths. Any resources necessary should be referenced via environment variables.  
-
-- All path variables you need must be defined with the prefix $TMSCAG_  
-  Example: $TMSCAG_BIN, $TMSCAG_ETC.
-
-- Any dependent libraries must either be open-source or government off the shelf.  
-  Commercial software packages are not supported.
-
-- The TMSCAG implementation, once built, must result in a binary or set of 
-  binaries that can be executed from the Linux command prompt.  Keep it simple.
-
-=======================
-Project Execution Plan
-=======================
-
-A project execution plan (PEP) detailing how the project was to be managed accompanies this documentation. It provides context on 
-planning and excution of the task based upon various criteria, namely
-* organization and responsibilities
-* resource requirements
-* project baselines
-* project management control and reporting
-* risk management
-* technical analyses, and
-* transition to operations
-
-The PEP can be found at :download:`Project Execution Plan NASA Jet Propulsion Laboratory delivery of Snow Coverage and Grain Size Implementation for Landsat 7 Enhanced Thematic Mapper (TMSCAG) to the United States Geological Survey <../publications/tmscag_project_execution_plan_v0.2_XXXX2015.docx>`.
-
-a Gantt chart (included within the project execution plan) listing sub tasks and thier anticipated duration is provided below for reference.
-
-.. image:: ../publications/tmscag_gantt_chart.png
-
-.. [0] Thomas H. Painter, Karl Rittger, Ceretha McKenzie, Peter Slaughter, Robert E. Davis, Jeff Dozier, Retrieval of subpixel snow covered area, grain size, and albedo from MODIS, Remote Sensing of Environment, Volume 113, Issue 4, 15 April 2009, Pages 868-879, ISSN 0034-4257, http://dx.doi.org/10.1016/j.rse.2009.01.001.
-
-.. [1] Rosenthal, W. and Dozier, J., 1996, Automated mapping of montane snow cover at subpixel resolution from the Landsat Thematic Mapper. Water Resources Research, 32, pp. 115-130.
.. automodule:: podaac
    :members:
