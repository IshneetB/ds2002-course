import boto3
import sys
import os

s3 = boto3.client('s3', region_name='us-east-1')

bucket = sys.argv[1]
file = sys.argv[2]

filename = os.path.basename(file)

with open(file, "rb") as f:
    s3.put_object(Bucket=bucket, Key=filename, Body=f)

print("Uploaded successfully")
