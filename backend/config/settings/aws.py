import os

from .base import *  # noqa: F403

MIDDLEWARE.append("api.middleware.RangesMiddleware")  # noqa: F405
CORS_ORIGIN_WHITELIST = ("http://127.0.0.1:3000", "http://0.0.0.0:3000", "http://localhost:3000")
CSRF_TRUSTED_ORIGINS = CORS_ORIGIN_WHITELIST

DJANGO_DRF_FILEPOND_STORAGES_BACKEND = "storages.backends.s3boto3.S3Boto3Storage"
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_S3_REGION_NAME = os.environ.get("REGION_NAME", "us-west-1")
AWS_STORAGE_BUCKET_NAME = os.environ.get("BUCKET_NAME", "filepond-uploads")
AWS_DEFAULT_ACL = "private"
AWS_BUCKET_ACL = "private"
AWS_AUTO_CREATE_BUCKET = True
