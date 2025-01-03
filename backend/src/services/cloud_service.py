from typing import Dict, Any
import cloudinary
from fastapi import HTTPException, UploadFile, status, Request
from cloudinary import CloudinaryImage
from cloudinary.uploader import upload
from cloudinary.exceptions import Error as CloudinaryError
from requests.exceptions import RequestException, Timeout, HTTPError, TooManyRedirects

from src.i18n.translations import get_translator
from src.conf.config import config

cloudinary.config(
    cloud_name=config.CLOUD_NAME,
    api_key=config.API_KEY,
    api_secret=config.API_SECRET
)


class CloudService:
    """Service for handling cloud storage operations for user avatars."""

    MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB
    ALLOWED_TYPES = ['image/jpeg', 'image/png', 'image/gif']

    @staticmethod
    def handle_exceptions(err: Exception, request: Request) -> None:
        """Handle various exceptions that might occur during upload."""
        t = get_translator(request)
        error_mappings = {
            CloudinaryError: (500, "cloud.errors.cloudinary_error"),
            RequestException: (500, "cloud.errors.operation_failed"),
            Timeout: (500, "cloud.errors.timeout"),
            TooManyRedirects: (500, "cloud.errors.too_many_redirects"),
            HTTPError: (500, "cloud.errors.http_error"),
            IOError: (500, "cloud.errors.io_error"),
            FileNotFoundError: (404, "cloud.errors.file_not_found")
        }

        for error_type, (status_code, message) in error_mappings.items():
            if isinstance(err, error_type):
                if isinstance(err, HTTPError) and err.response is not None:
                    if err.response.status_code == 401:
                        raise HTTPException(status_code=401, detail=t("cloud.errors.unauthorized", {"error": str(err)}))
                    elif err.response.status_code == 400:
                        raise HTTPException(status_code=400, detail=t("cloud.errors.bad_request", {"error": str(err)}))
                raise HTTPException(status_code=status_code, detail=f"{message}: {err}")

        raise HTTPException(status_code=500, detail=t("cloud.errors.unexpected", {"error": str(err)}))

    @classmethod
    def validate_image(cls, file: UploadFile, request: Request) -> None:
        """Validate image file type and size."""
        t = get_translator(request)

        if file.content_type not in cls.ALLOWED_TYPES:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=t("cloud.errors.invalid_type")
            )

        file_size = 0
        chunk_size = 4096

        for chunk in iter(lambda: file.file.read(chunk_size), b''):
            file_size += len(chunk)
            if file_size > cls.MAX_FILE_SIZE:
                raise HTTPException(
                    status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
                    detail=t("cloud.errors.file_too_large", {
                        "size": cls.MAX_FILE_SIZE / (1024 * 1024)
                    })
                )

        file.file.seek(0)  # Reset file pointer

    @classmethod
    async def upload_avatar(cls, file: UploadFile, email: str, request: Request) -> Dict[str, Any]:
        """Upload avatar to Cloudinary with optimizations."""
        try:
            cls.validate_image(file, request)

            public_id = f"PoopOK-avatar/{email}"

            # Upload with transformations
            upload_result = upload(
                file.file,
                public_id=public_id,
                overwrite=True,
                max_file_size=cls.MAX_FILE_SIZE,
                transformation=[
                    {'width': 250, 'height': 250, 'crop': 'fill'},
                    {'quality': 'auto:low'}
                ]
            )

            # Generate optimized URL
            avatar_url = CloudinaryImage(public_id).build_url(
                width=250,
                height=250,
                crop="fill",
                version=upload_result.get("version")
            )

            return {
                "public_id": public_id,
                "url": avatar_url,
                "cloudinary_response": upload_result
            }

        except Exception as e:
            cls.handle_exceptions(e, request)
