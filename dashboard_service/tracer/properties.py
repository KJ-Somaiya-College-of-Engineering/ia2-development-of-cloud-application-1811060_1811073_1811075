import os
from dotenv import load_dotenv
import boto3

try:
    load_dotenv()
    print("Loaded Environment from .env file")
except:
    print("Error Loading Env. Using default keys")

_SECRET_KEY = os.getenv("SECRET_KEY", default='testenv')
_DB_URL = os.getenv("DB_URL", default='http://localhost:8000')

_DB_INSTANCE = boto3.resource('dynamodb')
_EMAIL_CLIENT = boto3.client('ses', region_name="ap-south-1")

__S3__ = boto3.resource('s3')
__BUCKET_NAME__ = "trcr-image-store"
__BUCKET_INSTANCE__ = __S3__.Bucket(__BUCKET_NAME__)

def get_site_secret_key():
    return _SECRET_KEY

def get_db_instance():
    return _DB_INSTANCE

def get_email_client():
    return _EMAIL_CLIENT

def get_s3_instance():
    return __BUCKET_INSTANCE__

def get_bucked_name():
    return __BUCKET_NAME__

def get_aws_region():
    return "ap-south-1"
