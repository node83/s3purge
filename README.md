# s3purge
A CLI tool for deleting old files from an AWS.S3 bucket.

## Requirements
* python 3.x

## Installation
~~~
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
~~~

## Usage
~~~
venv/bin/python s3purge.py [--days DAYS] [--prefix PREFIX] bucket
~~~
Will delete files in the specified s3 bucket older than DAYS and starting with
PREFIX.

* DAYS defaults to 14
* PREFIX defaults to ""

## Configuration
Like the [AWS Command Line Tool](https://aws.amazon.com/cli/), s3purge uses the
executing user's ~/.aws folder to store the two files:
* config
* credentials

### ~/.aws/config
~~~
[default]
region = eu-west-1
~~~
### ~/.aws/credentials
~~~
[default]
aws_access_key_id = XXXXXXXXXX
aws_secret_access_key = XXXXXXXXXXXXXXXXXXXX
~~~
You will need to correctly populate both of these files in order for s3purge
to operate. 
