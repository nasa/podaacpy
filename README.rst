podaacpy
========

podaacpy has been retired please use https://github.com/podaac/data-subscriber 
------------------------------------------------------------------------------

|DOI| |license| |PyPI| |documentation| |Travis| |Coveralls| |Requirements Status| |Anaconda-Server Version| |Anaconda-Server Downloads| 

|DeepSource|

|image7|

A python utility library for interacting with NASA JPL's
`PO.DAAC <https://podaac.jpl.nasa.gov>`__


Software DOI
------------

If you are using Podaacpy in your research, please consider citing the software |DOI|. This DOI represents all versions, and will always resolve to the latest one. If you wish to reference actual versions, then please find the appropriate DOI's over at Zenodo.


What is PO.DAAC?
----------------

| The Physical Oceanography Distributed Active Archive Center (PO.DAAC)
  is an element of the
| Earth Observing System Data and Information System
  (`EOSDIS <https://earthdata.nasa.gov/>`__).
| The EOSDIS provides science data to a wide community of users for
  NASA's Science Mission Directorate.

What does podaacpy offer?
-------------------------

The library provides a Python toolkit for interacting with all
`PO.DAAC Web Services v3.2.2 APIs <https://podaac.jpl.nasa.gov/ws>`__, namely

-  `PO.DAAC Web Services <https://podaac.jpl.nasa.gov/ws/>`__: services
   include
-  `Dataset
   Metadata <https://podaac.jpl.nasa.gov/ws/search/dataset/index.html>`__
   - retrieves the metadata of a dataset
-  `Granule
   Metadata <https://podaac.jpl.nasa.gov/ws/metadata/granule/index.html>`__
   - retrieves the metadata of a granule
-  `Search
   Dataset <https://podaac.jpl.nasa.gov/ws/search/dataset/index.html>`__
   - searches PO.DAAC's dataset catalog, over Level 2, Level 3, and
   Level 4 datasets
-  `Search
   Granule <https://podaac.jpl.nasa.gov/ws/search/granule/index.html>`__
   - does granule searching on PO.DAAC level 2 swath datasets
   (individual orbits of a satellite), and level 3 & 4 gridded datasets
   (time averaged to span the globe)
-  `Image
   Granule <https://podaac.jpl.nasa.gov/ws/image/granule/index.html>`__ -
   renders granules in the PO.DAAC's catalog to images such as jpeg
   and/or png
-  `Extract
   Granule <https://podaac.jpl.nasa.gov/ws/extract/granule/index.html>`__
   - subsets a granule in PO.DAAC catalog and produces either netcdf3 or
   hdf4 files

-  | `Metadata Compliance
     Checker <https://podaac-uat.jpl.nasa.gov/mcc>`__: an online tool and
     web
   | service designed to check and validate the contents of netCDF and
     HDF granules for the
   | Climate and Forecast (CF) and Attribute Convention for Dataset
     Discovery (ACDD) metadata conventions.

-  | `Level 2 Subsetting 
      <https://podaac-tools.jpl.nasa.gov/hitide/>`__: allows users to subset 
      and download popular PO.DAAC level 2 (swath) datasets.

-  | `PO.DAAC Drive <https://podaac-tools.jpl.nasa.gov/drive/>`__: an HTTP based 
      data access service. PO.DAAC Drive replicates much of the functionality 
      of FTP while addressing many of its issues.

Additionally, Podaacpy provides the following ocean-related data services 

- `NASA OceanColor Web <https://oceancolor.gsfc.nasa.gov>`_:

- `File Search <https://oceandata.sci.gsfc.nasa.gov/api/file_search>`_ -  locate publically available files within the NASA Ocean Data Processing System (ODPS)
- `Bulk data downloads via HTTP <https://oceancolor.gsfc.nasa.gov/forum/oceancolor/topic_show.pl?pid=12520>`_ - mimic FTP bulk data downloads using the `HTTP-based data distribution server <https://oceandata.sci.gsfc.nasa.gov>`_.

Installation
------------

From the cheeseshop

::

    pip3 install podaacpy
    
or from conda

::

    conda install -c conda-forge podaacpy    

or from source

::

    git clone https://github.com/nasa/podaacpy.git && cd podaacpy
    python3 setup.py install

Quickstart
----------
Check out the **examples** directory for our Jupyter notebook examples.

Tests
-----

| podaacpy uses the popular
  `nose <http://nose.readthedocs.org/en/latest/>`__ testing suite for
  unit tests.
| You can run the podaacpy tests simply by running

::

    nosetests

Additonally, click on the build sticker at the top of this readme to be
directed to the most recent build on
`travis-ci <https://travis-ci.org/nasa/podaacpy>`__.

Documentation
-------------

You can view the documentation online at

http://podaacpy.readthedocs.org/en/latest/

Alternatively, you can build the documentation manually as follows

::

    cd docs && make html

Documentation is then available in docs/build/html/

Community, Support and Development
----------------------------------

| Please open a ticket in the `issue
  tracker <https://github.com/nasa/podaacpy/issues>`__.
| Please use
  `labels <https://help.github.com/articles/applying-labels-to-issues-and-pull-requests/>`__
  to
| classify your issue.

License
-------

| podaacpy is licensed permissively under the `Apache License
  v2.0 <http://www.apache.org/licenses/LICENSE-2.0>`__.
| A copy of that license is distributed with this software.

Copyright and Export Classification
-----------------------------------

::

    Copyright 2016-2019, by the California Institute of Technology. ALL RIGHTS RESERVED. 
    United States Government Sponsorship acknowledged. Any commercial use must be 
    negotiated with the Office of Technology Transfer at the California Institute 
    of Technology.
    This software may be subject to U.S. export control laws. By accepting this software, 
    the user agrees to comply with all applicable U.S. export laws and regulations. 
    User has the responsibility to obtain export licenses, or other export authority 
    as may be required before exporting such information to foreign countries or 
    providing access to foreign persons.

.. |DOI| image:: https://zenodo.org/badge/DOI/10.5281/zenodo.1751972.svg
   :target: https://doi.org/10.5281/zenodo.1751972
.. |license| image:: https://img.shields.io/github/license/nasa/podaacpy.svg?maxAge=2592000
   :target: http://www.apache.org/licenses/LICENSE-2.0
.. |PyPI| image:: https://img.shields.io/pypi/v/podaacpy.svg?maxAge=2592000?style=plastic
   :target: https://pypi.python.org/pypi/podaacpy
.. |documentation| image:: https://readthedocs.org/projects/podaacpy/badge/?version=latest
   :target: http://podaacpy.readthedocs.org/en/latest/
.. |Travis| image:: https://img.shields.io/travis/nasa/podaacpy.svg?maxAge=2592000?style=plastic
   :target: https://travis-ci.org/nasa/podaacpy
.. |Coveralls| image:: https://coveralls.io/repos/github/nasa/podaacpy/badge.svg?branch=master
   :target: https://coveralls.io/github/nasa/podaacpy?branch=master
.. |Requirements Status| image:: https://requires.io/github/nasa/podaacpy/requirements.svg?branch=master
   :target: https://requires.io/github/nasa/podaacpy/requirements/?branch=master
.. |Anaconda-Server Version| image:: https://anaconda.org/conda-forge/podaacpy/badges/version.svg
   :target: https://anaconda.org/conda-forge/podaacpy
.. |Anaconda-Server Downloads| image:: https://anaconda.org/conda-forge/podaacpy/badges/downloads.svg
   :target: https://anaconda.org/conda-forge/podaacpy
.. |image7| image:: https://podaac.jpl.nasa.gov/sites/default/files/image/custom_thumbs/podaac_logo.png
.. |DeepSource| image:: https://static.deepsource.io/deepsource-badge-light.svg
    :target: https://deepsource.io/gh/nasa/podaacpy/?ref=repository-badge

