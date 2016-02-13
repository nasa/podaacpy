# podaac-python
<img src="http://podaac.jpl.nasa.gov/sites/default/files/image/custom_thumbs/podaac_logo.png" align="right" width="300" />
A python utility library for interacting with NASA JPL's [PO.DAAC](http://podaac.jpl.nasa.gov)

## What is PO.DAAC?
The Physical Oceanography Distributed Active Archive Center (PO.DAAC) is an element of the 
Earth Observing System Data and Information System ([EOSDIS](https://earthdata.nasa.gov/)). 
The EOSDIS provides science  data to a wide community of users for NASA's Science Mission Directorate.

## What does podaac-python offer?
The library provides a Python toolkit for interacting with all of PO.DAACs API's, namely
 * [PO.DAAC Web Services](https://podaac.jpl.nasa.gov/ws/): services include 
 [Dataset Metadata](http://podaac.jpl.nasa.gov/ws/search/dataset/index.html)
 [Granule Metadata](http://podaac.jpl.nasa.gov/ws/metadata/granule/index.html)
 [Search Dataset](http://podaac.jpl.nasa.gov/ws/search/dataset/index.html)
 [Search Granule](http://podaac.jpl.nasa.gov/ws/search/granule/index.html)
 [Image Granule](http://podaac.jpl.nasa.gov/ws/image/granule/index.html)
 [Extract Granule](http://podaac.jpl.nasa.gov/ws/extract/granule/index.html)
 * [Metadata Compliance Checker](http://podaac-uat.jpl.nasa.gov/mcc): an online tool and web 
 service designed to check and validate the contents of netCDF and HDF granules for the 
 Climate and Forecast (CF) and Attribute Convention for Dataset Discovery (ACDD) metadata conventions.

## Installation
From the cheeseshop
```
pip install
```
or from source
```
git clone ... && cd podaac-python
python setup.py install
```

## Community, Support and Development
Please open a ticket in the issue tracker. 
Please use [labels](https://help.github.com/articles/applying-labels-to-issues-and-pull-requests/) to
classify your issue. 

## License
podaac-python is licensed permissively under the [Apache License v2.0](http://www.apache.org/licenses/LICENSE-2.0).
A copy of that license is distributed with this software.
