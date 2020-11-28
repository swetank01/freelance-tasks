from selenium import webdriver
from time import sleep
import boto3
import logging
from botocore.exceptions import ClientError
from botocore.client import Config

Selenium-url = "http://localhost:4444/wd/hub"
mybucket = "lambdatest-bucket-main"
filename = "screenshot.png"

print(mybucket)
print(filename)

driver = webdriver.Remote(command_executor = Selenium-url, desired_capabilities = {'browserName':'chrome'})
driver.get('https://www.lambdatest.com/')
sleep(1)
driver.get_screenshot_as_file(filename)
driver.quit()
print("end...")

s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))
for bucket in s3.buckets.all():
  print(bucket.name)


def upload_file(file_name, bucket, object_name=None):
    print("upload_file started")

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name, ExtraArgs={'ACL': 'public-read'})
    except ClientError as e:
        logging.error(e)
        return False
    return True

def create_presigned_url(bucket_name, object_name, expiration=3600):
    # Generate a presigned URL for the S3 object
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    return print(response)

upload_file(filename, mybucket)
print("upload_file End")
create_presigned_url(mybucket, filename)
print("URL generated")