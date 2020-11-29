# Task Description 

We need a system where we provide a website link and want to capture the screenshot on chrome & Firefox in Ubuntu. Create a script which asks for a website link and spawns 2 containers parallely  and opens that link in chrome  and Firefox, capture the screenshot, push them to s3 and provide 2 signed s3 links. Links should expire after 30 mins

# Setup
1. Spin up the selenium hub, chrome and firefox container using the command given below 
`docker-compose up -d`

2. Setup AWS config 
```
vi ~/.aws/credentials
[default]
aws_access_key_id = 
aws_secret_access_key = 
```

## Doubts and Queries

## Hints
- Use Selenium Grid
- https://github.com/SeleniumHQ/docker-selenium/tree/selenium-3
- https://robotninja.com/blog/introduction-using-selenium-docker-containers-end-end-testing/

## Ref 
- https://dev.to/nazliander/using-selenium-within-a-docker-container-ghp // NO
- https://www.the-lazy-dev.com/en/python-selenium-grid-and-docker/ // YES
- https://nander.cc/using-selenium-within-a-docker-container  

## Chrome Headless

https://developers.google.com/web/updates/2017/04/headless-chrome

https://bitsofco.de/using-a-headless-browser-to-capture-page-screenshots/



## ENV Setup Up

### Getting Started

```
python3.6 -m venv env
source env/bin/activate
pip install selenium
deactivate
```
## Boto to s3
https://realpython.com/python-boto3-aws-s3/


--- > REMEBER boto3 s3 pre-signed url is not work on every region 
## Tutorials & Blogs 

- https://blog.testproject.io/2019/07/16/web-test-using-selenium-webdriver-python-chrome/