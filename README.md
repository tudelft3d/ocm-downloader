# opencitymodel downloader

This is a script to download datasets of [opencitymode](https://github.com/opencitymodel/opencitymodel) stored in its AWS S3 bucket.

### Requirements
Requires Python3 and the boto3 library (``pip install boto3``).

### Usage
Run ``python main.py [options]``

#### Options
- ``--format``: can be ``CityJSON`` or ``CityGML``
- ``--area-name``: the name of the area (effectively, just a string filter in the URL)

