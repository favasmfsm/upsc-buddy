from django.conf import settings
from django.core.files.storage import FileSystemStorage


def branding_storage():
    """Use public S3 when configured; otherwise local MEDIA_ROOT."""
    if getattr(settings, "AWS_STORAGE_BUCKET_NAME", None):
        from core.custom_storages import PublicMediaStorage

        return PublicMediaStorage()
    return FileSystemStorage()
