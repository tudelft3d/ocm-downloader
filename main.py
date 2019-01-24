import boto3
from botocore.handlers import disable_signing
import ntpath

resource = boto3.resource('s3')
resource.meta.client.meta.events.register('choose-signer.s3.*', disable_signing)

bucket = resource.Bucket('opencitymodel')

for file in bucket.objects.all():
    if file.key.endswith('.json'):
        local_filename = './' + ntpath.basename(file.key)
        bucket.download_file(file.key, local_filename)
        print('Downloaded ' + file.key)
