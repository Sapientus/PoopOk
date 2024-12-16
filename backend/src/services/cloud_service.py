from typing import Dict, Any
from fastapi import HTTPException, UploadFile, status
import cloudinary
from cloudinary import CloudinaryImage
from cloudinary.uploader import upload
from cloudinary.exceptions import Error as CloudinaryError
from requests.exceptions import RequestException, Timeout, HTTPError, TooManyRedirects

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
    def handle_exceptions(err: Exception) -> None:
        """Handle various exceptions that might occur during upload."""
        error_mappings = {
            CloudinaryError: (500, "Cloudinary API error"),
            RequestException: (500, "Operation failed"),
            Timeout: (500, "Request timed out"),
            TooManyRedirects: (500, "Too many redirects"),
            HTTPError: (500, "HTTP error"),
            IOError: (500, "I/O error"),
            FileNotFoundError: (404, "File not found")
        }

        for error_type, (status_code, message) in error_mappings.items():
            if isinstance(err, error_type):
                if isinstance(err, HTTPError) and err.response is not None:
                    if err.response.status_code == 401:
                        raise HTTPException(status_code=401, detail=f"Unauthorized: {err}")
                    elif err.response.status_code == 400:
                        raise HTTPException(status_code=400, detail=f"Bad request: {err}")
                raise HTTPException(status_code=status_code, detail=f"{message}: {err}")

        raise HTTPException(status_code=500, detail=f"Unexpected error: {err}")

    @classmethod
    def validate_image(cls, file: UploadFile) -> None:
        """Validate image file type and size."""
        if file.content_type not in cls.ALLOWED_TYPES:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid file type. Only JPEG, PNG, and GIF are allowed."
            )

        file_size = 0
        chunk_size = 4096

        for chunk in iter(lambda: file.file.read(chunk_size), b''):
            file_size += len(chunk)
            if file_size > cls.MAX_FILE_SIZE:
                raise HTTPException(
                    status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
                    detail=f"File too large. Maximum size is {cls.MAX_FILE_SIZE / (1024 * 1024)} MB"
                )

        file.file.seek(0)  # Reset file pointer

    @classmethod
    async def upload_avatar(cls, file: UploadFile, email: str) -> Dict[str, Any]:
        """Upload avatar to Cloudinary with optimizations."""
        try:
            cls.validate_image(file)

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
            cls.handle_exceptions(e)
