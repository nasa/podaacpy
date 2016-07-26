# podaacpy

<img src="https://img.shields.io/badge/license-Apache%202-4EB1BA.svg" />
<img src="https://readthedocs.org/projects/podaacpy/badge/?version=latest" />
<img src="https://travis-ci.org/lewismc/podaacpy.svg?branch=master" />
<a href='https://coveralls.io/github/lewismc/podaacpy?branch=master'>
  <img src='https://coveralls.io/repos/github/lewismc/podaacpy/badge.svg?branch=master' alt='Coverage Status' />
</a> 
<a href="https://requires.io/github/lewismc/podaacpy/requirements/?branch=master">
  <img src="https://requires.io/github/lewismc/podaacpy/requirements.svg?branch=master" alt="Requirements Status" />
</a>
<a href="https://landscape.io/github/lewismc/podaacpy/master">
  <img alt="Code Health" src="https://landscape.io/github/lewismc/podaacpy/master/landscape.svg?style=flat"/>
</a>

<img src="https://podaac.jpl.nasa.gov/sites/default/files/image/custom_thumbs/podaac_logo.png" align="right" width="300" />
A python utility library for interacting with NASA JPL's [PO.DAAC](http://podaac.jpl.nasa.gov)

## What is PO.DAAC?
The Physical Oceanography Distributed Active Archive Center (PO.DAAC) is an element of the 
Earth Observing System Data and Information System ([EOSDIS](https://earthdata.nasa.gov/)). 
The EOSDIS provides science  data to a wide community of users for NASA's Science Mission Directorate.

## What does podaacpy offer?
The library provides a Python toolkit for interacting with all of PO.DAACs API's, namely
 * [PO.DAAC Web Services](https://podaac.jpl.nasa.gov/ws/): services include 
   * [Dataset Metadata](http://podaac.jpl.nasa.gov/ws/search/dataset/index.html) - retrieves the metadata of a dataset
   * [Granule Metadata](http://podaac.jpl.nasa.gov/ws/metadata/granule/index.html) - retrieves the metadata of a granule
   * [Search Dataset](http://podaac.jpl.nasa.gov/ws/search/dataset/index.html) - searches PO.DAAC's dataset catalog, over Level 2, Level 3, and Level 4 datasets
   * [Search Granule](http://podaac.jpl.nasa.gov/ws/search/granule/index.html) - does granule searching on PO.DAAC level 2 swath datasets (individual orbits of a satellite), and level 3 & 4 gridded datasets (time averaged to span the globe)
   * [Image Granule](http://podaac.jpl.nasa.gov/ws/image/granule/index.html) - renders granules in the PO.DAAC's catalog to images such as jpeg and/or png
   * [Extract Granule](http://podaac.jpl.nasa.gov/ws/extract/granule/index.html) - subsets a granule in PO.DAAC catalog and produces either netcdf3 or hdf4 files

* [Metadata Compliance Checker](http://podaac-uat.jpl.nasa.gov/mcc): an online tool and web 
 service designed to check and validate the contents of netCDF and HDF granules for the 
 Climate and Forecast (CF) and Attribute Convention for Dataset Discovery (ACDD) metadata conventions.

## Installation
From the cheeseshop
```
pip install podaacpy
```
or from source
```
git clone https://github.com/lewismc/podaacpy.git && cd podaacpy
python setup.py install
```

## Tests
podaacpy uses the popular [nose](http://nose.readthedocs.org/en/latest/) testing suite for unit tests. 
You can run the podaacpy tests simply by running
```
nosetests
```
Additonally, click on the build sticker at the top of this readme to be directed to the most recent build on [travis-ci](https://travis-ci.org/lewismc/podaacpy).

## Documentation
You can view the documentation online at 

http://podaacpy.readthedocs.org/en/latest/

Alternatively, you can build the documentation manually as follows
```
cd docs && make html
```
Documentation is then available in docs/build/html/

## Community, Support and Development
Please open a ticket in the [issue tracker](https://github.com/lewismc/podaacpy/issues). 
Please use [labels](https://help.github.com/articles/applying-labels-to-issues-and-pull-requests/) to
classify your issue. 

## License
podaacpy is licensed permissively under the [Apache License v2.0](http://www.apache.org/licenses/LICENSE-2.0).
A copy of that license is distributed with this software.

## Copyright and Export Classification
```
Copyright 2016, by the California Institute of Technology. ALL RIGHTS RESERVED. 
United States Government Sponsorship acknowledged. Any commercial use must be 
negotiated with the Office of Technology Transfer at the California Institute 
of Technology.
This software may be subject to U.S. export control laws. By accepting this software, 
the user agrees to comply with all applicable U.S. export laws and regulations. 
User has the responsibility to obtain export licenses, or other export authority 
as may be required before exporting such information to foreign countries or 
providing access to foreign persons.
```
