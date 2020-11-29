from selenium import webdriver
from time import sleep
import boto3
import logging
from botocore.exceptions import ClientError
from botocore.client import Config
import datetime

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

def create_presigned_url(bucket_name, object_name, expiration=1800):
    # Generate a presigned URL for the S3 object
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url('get_object',
            Params={'Bucket': bucket_name, 'Key': object_name}, ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    return print(response)

def create_screenshoot(browser_node, seleniumurl, mybucket):
    for Browser in browser_node:
        timestamp = str(datetime.datetime.now())
        filename = "screenshot_"+Browser+"_"+timestamp+".png"
        driver = webdriver.Remote(command_executor = seleniumurl, desired_capabilities = {'browserName': Browser})
        driver.get('https://www.lambdatest.com/')
        sleep(1)
        driver.get_screenshot_as_file(filename)
        driver.quit()
        print(filename+" Generated Successfully!")
        upload_file(filename, mybucket)
        print("upload_file End")
        create_presigned_url(mybucket, filename)
        print("URL generated")

def main():
    #seleniumurl = input("Enter Selenium-Grid-Hub URL :")
    seleniumurl = "http://localhost:4444/wd/hub"
    #mybucket = input("Enter Bucket Name :")
    mybucket = "lambdatest-bucket-main"
    browserList = ['chrome', 'firefox']

    print("started")
    create_screenshoot(browserList, seleniumurl, mybucket)
    print("selenium automation is done!!")

if __name__=="__main__":
    main()