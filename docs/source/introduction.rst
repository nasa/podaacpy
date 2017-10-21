.. # encoding: utf-8
   # Copyright 2017 California Institute of Technology.
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
   
Introduction to podaacpy
************************

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

 * `Dataset Metadata <http://podaac.jpl.nasa.gov/ws/metadata/dataset/index.html>`_ - retrieves the metadata of a dataset
 * `Dataset Search <http://podaac.jpl.nasa.gov/ws/search/dataset/index.html>`_ - searches PO.DAAC's dataset catalog, over Level 2, Level 3, and Level 4 datasets
 * `Dataset Variables <http://podaac.jpl.nasa.gov/ws/dataset/variables/index.html>`_ - provides list of dataset variables for the dataset
 * `Granule Metadata <http://podaac.jpl.nasa.gov/ws/metadata/granule/index.html>`_ - retrieves the metadata of a granule
 * `Granule Search <http://podaac.jpl.nasa.gov/ws/search/granule/index.html>`_ - does granule searching on PO.DAAC level 2 swath datasets (individual orbits of a satellite), and level 3 & 4 gridded datasets (time averaged to span the globe)
 * `Granule Preview <http://podaac.jpl.nasa.gov/ws/image/granule/index.html>`_ - the PODAAC preview Image service retrieves pre-generated preview images for selected granules
 * `Granule Subset <http://podaac.jpl.nasa.gov/ws/subset/granule/index.html>`_ - Subset Granule service allows users to submit subset jobs
 * `Subset Status <http://podaac.jpl.nasa.gov/ws/subset/status/index.html>`_ - Subset Granule Status service allows users to check the status of submitted subset job

* `Metadata Compliance Checker <http://podaac-uat.jpl.nasa.gov/mcc>`_: an online tool and web service designed to check and validate the contents of netCDF and HDF granules for the Climate and Forecast (CF) and Attribute Convention for Dataset Discovery (ACDD) metadata conventions.

Additionally, Podaacpy provides the following ocean-related data services 
* `NASA OceanColor Web <https://oceancolor.gsfc.nasa.gov>`_:

 * `File Search <https://oceandata.sci.gsfc.nasa.gov/api/file_search>`_ -  locate publically available files within the NASA Ocean Data Processing System (ODPS)
 * `Bulk data downloads via HTTP <https://oceancolor.gsfc.nasa.gov/forum/oceancolor/topic_show.pl?pid=12520>`_ - mimic FTP bulk data downloads using the `HTTP-based data distribution server <https://oceandata.sci.gsfc.nasa.gov>`_.
