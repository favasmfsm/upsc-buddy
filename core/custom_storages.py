from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


def _aws(name: str, default=None):
    return getattr(settings, name, default)


class MediaStorage(S3Boto3Storage):
    bucket_name = _aws("AWS_STORAGE_BUCKET_NAME")
    region_name = _aws("AWS_S3_REGION_NAME")
    access_key = _aws("AWS_ACCESS_KEY_ID")
    secret_key = _aws("AWS_SECRET_ACCESS_KEY")
    default_acl = "private"  # Make sure files are private by default
    custom_domain = False  # Disable public URLs

    def url(self, name, expire=3600):
        """
        Override the url method to return a pre-signed URL for accessing media files.
        """
        import boto3

        s3_client = boto3.client(
            "s3",
            region_name=self.region_name,
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
        )

        try:
            url = s3_client.generate_presigned_url(
                "get_object",
                Params={"Bucket": self.bucket_name, "Key": name},
                ExpiresIn=expire,
            )
        except Exception as e:
            print(f"Error generating pre-signed URL: {e}")
            return None

        return url


class PublicMediaStorage(S3Boto3Storage):
    """Public assets (logos, favicons) with stable non-presigned URLs."""

    bucket_name = _aws("AWS_STORAGE_BUCKET_NAME")
    region_name = _aws("AWS_S3_REGION_NAME")
    access_key = _aws("AWS_ACCESS_KEY_ID")
    secret_key = _aws("AWS_SECRET_ACCESS_KEY")
    default_acl = "public-read"
    querystring_auth = False
    custom_domain = False
    file_overwrite = False
