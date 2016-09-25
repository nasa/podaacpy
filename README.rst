podaacpy
========

| |license| |PyPI| |Python3| |Python2| |documentation| |Travis| |Coveralls| |Requirements Status| |Code Health| |Pypi Downloads|

|image7|

A python utility library for interacting with NASA JPL's
`PO.DAAC <http://podaac.jpl.nasa.gov>`__

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
[PO.DAAC Web Services v3.2.2 API's](http://podaac.jpl.nasa.gov/ws), namely

-  `PO.DAAC Web Services <https://podaac.jpl.nasa.gov/ws/>`__: services
   include
-  `Dataset
   Metadata <http://podaac.jpl.nasa.gov/ws/search/dataset/index.html>`__
   - retrieves the metadata of a dataset
-  `Granule
   Metadata <http://podaac.jpl.nasa.gov/ws/metadata/granule/index.html>`__
   - retrieves the metadata of a granule
-  `Search
   Dataset <http://podaac.jpl.nasa.gov/ws/search/dataset/index.html>`__
   - searches PO.DAAC's dataset catalog, over Level 2, Level 3, and
   Level 4 datasets
-  `Search
   Granule <http://podaac.jpl.nasa.gov/ws/search/granule/index.html>`__
   - does granule searching on PO.DAAC level 2 swath datasets
   (individual orbits of a satellite), and level 3 & 4 gridded datasets
   (time averaged to span the globe)
-  `Image
   Granule <http://podaac.jpl.nasa.gov/ws/image/granule/index.html>`__ -
   renders granules in the PO.DAAC's catalog to images such as jpeg
   and/or png
-  `Extract
   Granule <http://podaac.jpl.nasa.gov/ws/extract/granule/index.html>`__
   - subsets a granule in PO.DAAC catalog and produces either netcdf3 or
   hdf4 files

-  | `Metadata Compliance
     Checker <http://podaac-uat.jpl.nasa.gov/mcc>`__: an online tool and
     web
   | service designed to check and validate the contents of netCDF and
     HDF granules for the
   | Climate and Forecast (CF) and Attribute Convention for Dataset
     Discovery (ACDD) metadata conventions.

Installation
------------

From the cheeseshop

::

    pip install podaacpy

or from source

::

    git clone https://github.com/lewismc/podaacpy.git && cd podaacpy
    python setup.py install

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
`travis-ci <https://travis-ci.org/lewismc/podaacpy>`__.

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
  tracker <https://github.com/lewismc/podaacpy/issues>`__.
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

    Copyright 2016, by the California Institute of Technology. ALL RIGHTS RESERVED. 
    United States Government Sponsorship acknowledged. Any commercial use must be 
    negotiated with the Office of Technology Transfer at the California Institute 
    of Technology.
    This software may be subject to U.S. export control laws. By accepting this software, 
    the user agrees to comply with all applicable U.S. export laws and regulations. 
    User has the responsibility to obtain export licenses, or other export authority 
    as may be required before exporting such information to foreign countries or 
    providing access to foreign persons.

.. |license| image:: https://img.shields.io/github/license/lewismc/podaacpy.svg?maxAge=2592000
   :target: http://www.apache.org/licenses/LICENSE-2.0
.. |Python3| image:: https://img.shields.io/badge/python-3-blue.svg
   :target: https://www.python.org/downloads/
.. |Python2| image:: https://img.shields.io/badge/python-2-blue.svg
   :target: https://www.python.org/downloads/
.. |PyPI| image:: https://img.shields.io/pypi/v/podaacpy.svg?maxAge=2592000?style=plastic
   :target: https://pypi.python.org/pypi/podaacpy
.. |documentation| image:: https://readthedocs.org/projects/podaacpy/badge/?version=latest
   :target: http://podaacpy.readthedocs.org/en/latest/
.. |Travis| image:: https://img.shields.io/travis/lewismc/podaacpy.svg?maxAge=2592000?style=plastic
   :target: https://travis-ci.org/lewismc/podaacpy
.. |Coveralls| image:: https://img.shields.io/coveralls/lewismc/podaacpy.svg?maxAge=2592000?style=plastic
   :target: https://coveralls.io/github/lewismc/podaacpy?branch=master
.. |Requirements Status| image:: https://requires.io/github/lewismc/podaacpy/requirements.svg?branch=master
   :target: https://requires.io/github/lewismc/podaacpy/requirements/?branch=master
.. |Code Health| image:: https://landscape.io/github/lewismc/podaacpy/master/landscape.svg?style=flat-square
   :target: https://landscape.io/github/lewismc/podaacpy/master
.. |Pypi Downloads| image:: https://img.shields.io/pypi/dm/podaacpy.svg?maxAge=2592000?style=plastic
   :target: https://pypi.python.org/pypi/podaacpy/
.. |image7| image:: https://podaac.jpl.nasa.gov/sites/default/files/image/custom_thumbs/podaac_logo.png

