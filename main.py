import boto3
from botocore.handlers import disable_signing
import ntpath
import sys

# Setup the default configuration
format = '.json'
area = ''

# Read the arguments
i = 1
while len(sys.argv) > i:
    if sys.argv[i] == "--format":
        if sys.argv[i + 1] == "CityJSON":
            format = ".json"
        elif sys.argv[i + 1] == "CityGML":
            format = ".zip"
        else:
            print("The format provided is not supported (available options are CityJSON/CityGML)")
        i = i + 2
    elif sys.argv[i] == "--area-name":
        area = sys.argv[i + 1]
        i = i + 2
    else:
        print("Option " + sys.argv[i] + " not supported")
        i = i + 1


resource = boto3.resource('s3')
resource.meta.client.meta.events.register('choose-signer.s3.*', disable_signing)

bucket = resource.Bucket('opencitymodel')

for file in bucket.objects.all():
    if file.key.endswith(format):
        if area in file.key or area == '':
            local_filename = './' + ntpath.basename(file.key)
            bucket.download_file(file.key, local_filename)
            print('Downloaded ' + file.key)
