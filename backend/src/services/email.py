import logging
from pathlib import Path

from fastapi import HTTPException, status
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from fastapi_mail.errors import ConnectionErrors
from pydantic import EmailStr

from src.services.auth import auth_service
from src.conf.config import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ConfigMessage:
    try:
        conf = ConnectionConfig(
            MAIL_USERNAME=config.MAIL_USERNAME,
            MAIL_PASSWORD=config.MAIL_PASSWORD,
            MAIL_FROM=config.MAIL_FROM,
            MAIL_PORT=config.MAIL_PORT,
            MAIL_SERVER=config.MAIL_SERVER,
            MAIL_FROM_NAME="PoopOK - System",
            MAIL_STARTTLS=False,
            MAIL_SSL_TLS=True,
            USE_CREDENTIALS=True,
            VALIDATE_CERTS=True,
            TEMPLATE_FOLDER=Path(__file__).parent / 'templates',
        )
    except Exception as e:
        logger.error("Error initializing mail configuration: %s", e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Mail configuration error")


async def send_email(email: EmailStr, username: str, host: str):
    try:
        token_verification = auth_service.create_email_token({"sub": email})
        message = MessageSchema(
            subject="Confirm your email ",
            recipients=[email],
            template_body={"host": host, "username": username, "token": token_verification},
            subtype=MessageType.html
        )

        fm = FastMail(ConfigMessage.conf)
        await fm.send_message(message, template_name="verify_email.html")
    except ConnectionErrors as e:
        logger.error("Email sending failed: %s", e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to send email")


async def send_reset_password_email(email: EmailStr, username: str, reset_url: str):  # test
    try:
        message = MessageSchema(
            subject="Reset Your Password",
            recipients=[email],
            template_body={"username": username, "reset_url": reset_url},
            subtype=MessageType.html
        )
        fm = FastMail(ConfigMessage.conf)
        await fm.send_message(message, template_name="reset_password.html")
    except ConnectionErrors as err:
        print(err)
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Error sending email")
