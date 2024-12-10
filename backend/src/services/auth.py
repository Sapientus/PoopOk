from typing import Optional
from datetime import datetime, timedelta, timezone
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import get_db
from src.repository import users as repository_users
from src.conf.config import config
from src.services.exceptions.exceptions import AuthExceptions


class PasswordService:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password: str) -> str:
        return self.pwd_context.hash(password)


class TokenService:
    def __init__(self, secret_key: str, algorithm: str):
        self.secret_key = secret_key
        self.algorithm = algorithm

    def create_token(self, data: dict, expires_delta: Optional[float], scope: str) -> str:
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(
            seconds=expires_delta) if expires_delta else datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"iat": datetime.now(timezone.utc), "exp": expire, "scope": scope, "type": scope})
        return jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)

    def decode_token(self, token: str, expected_scope: str) -> dict:
        """
        Decode and verify JWT token
        """
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])

            if not payload:
                raise AuthExceptions.empty_payload()

            token_scope = payload.get("scope")
            if not token_scope:
                raise AuthExceptions.missing_scope()

            if token_scope != expected_scope:
                raise AuthExceptions.invalid_token_type(expected_scope, token_scope)

            return payload

        except ExpiredSignatureError:
            raise AuthExceptions.expired_token()
        except InvalidTokenError:
            raise AuthExceptions.invalid_token_format()
        except Exception as e:
            raise AuthExceptions.token_validation_error(str(e))


class AuthService:
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")

    def __init__(self, password_service: PasswordService, token_service: TokenService):
        self.password_service = password_service
        self.token_service = token_service

    async def create_access_token(self, data: dict, expires_delta: Optional[float] = None) -> str:
        return self.token_service.create_token(data, expires_delta or 900, "access_token")

    async def create_refresh_token(self, data: dict, expires_delta: Optional[float] = None) -> str:
        return self.token_service.create_token(data, expires_delta or 604800, "refresh_token")

    async def get_current_user(self, token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)):
        try:
            payload = self.token_service.decode_token(token, "access_token")
            email = payload["sub"]
        except HTTPException:
            raise AuthExceptions.invalid_credentials()

        user = await repository_users.get_user_by_email(email, db)
        if not user:
            raise AuthExceptions.user_not_found()
        return user

    def create_email_token(self, data: dict) -> str:
        return self.token_service.create_token(data, 86400, "email_verification")

    async def get_email_from_token(self, token: str) -> str:
        payload = self.token_service.decode_token(token, "email_verification")
        return payload["sub"]

    def create_password_reset_token(self, email: str) -> str:
        return self.token_service.create_token({"sub": email}, 1800, "password_reset")

    async def verify_password_reset_token(self, token: str) -> str:
        payload = self.token_service.decode_token(token, "password_reset")
        return payload["sub"]

    async def decode_refresh_token(self, token: str) -> str:
        """
        Decode refresh token and return user email
        """
        try:
            payload = self.token_service.decode_token(token, "refresh_token")
            if not payload.get("sub"):
                raise AuthExceptions.invalid_token_payload()
            return payload["sub"]
        except HTTPException as e:
            raise e
        except Exception as e:
            raise AuthExceptions.invalid_refresh_token(str(e))


password_service = PasswordService()
token_service = TokenService(config.SECRET_KEY_JWT, config.ALGORITHM)
auth_service = AuthService(password_service, token_service)
