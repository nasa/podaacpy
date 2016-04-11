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
   
Introduction to podaacpy
************************

*author*: Lewis John McGibbney (lewismc@apache.org)

============
Introduction
============
podaacpy is a python utility library for interacting with `NASA JPL's PO.DAAC <http://podaac.jpl.nasa.gov>`_

================
What is PO.DAAC?
================
The Physical Oceanography Distributed Active Archive Center (PO.DAAC) is an element of the Earth Observing System Data and Information System (`EOSDIS <https://earthdata.nasa.gov/>`_). The EOSDIS provides science data to a wide community of users for NASA's Science Mission Directorate.

=========================
What does podaacpy offer?
=========================
The library provides a Python toolkit for interacting with all of PO.DAACs API's, namely

* `PO.DAAC Web Services <https://podaac.jpl.nasa.gov/ws/>`_: services include
 * `Dataset Metadata <http://podaac.jpl.nasa.gov/ws/search/dataset/index.html>`_ - retrieves the metadata of a dataset
 * `Granule Metadata <http://podaac.jpl.nasa.gov/ws/metadata/granule/index.html>`_ - retrieves the metadata of a granule
 * `Search Dataset <http://podaac.jpl.nasa.gov/ws/search/dataset/index.html>`_ - searches PO.DAAC's dataset catalog, over Level 2, Level 3, and Level 4 datasets
 * `Search Granule <http://podaac.jpl.nasa.gov/ws/search/granule/index.html>`_ - does granule searching on PO.DAAC level 2 swath datasets (individual orbits of a satellite), and level 3 & 4 gridded datasets (time averaged to span the globe)
 * `Image Granule <http://podaac.jpl.nasa.gov/ws/image/granule/index.html>`_ - renders granules in the PO.DAAC's catalog to images such as jpeg and/or png
 * `Extract Granule <http://podaac.jpl.nasa.gov/ws/extract/granule/index.html>`_ - subsets a granule in PO.DAAC catalog and produces either netcdf3 or hdf4 files

* `Metadata Compliance Checker <http://podaac-uat.jpl.nasa.gov/mcc>`_: an online tool and web service designed to check and validate the contents of netCDF and HDF granules for the Climate and Forecast (CF) and Attribute Convention for Dataset Discovery (ACDD) metadata conventions.