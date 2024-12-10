from fastapi import HTTPException, status


class AuthExceptions:
    @staticmethod
    def token_validation_error(detail: str) -> HTTPException:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail
        )

    @staticmethod
    def empty_payload() -> HTTPException:
        return AuthExceptions.token_validation_error("Empty token payload")

    @staticmethod
    def missing_scope() -> HTTPException:
        return AuthExceptions.token_validation_error("Token missing scope claim")

    @staticmethod
    def invalid_token_type(expected: str, received: str) -> HTTPException:
        return AuthExceptions.token_validation_error(
            f"Invalid token type. Expected {expected} token, got {received} token"
        )

    @staticmethod
    def expired_token() -> HTTPException:
        return AuthExceptions.token_validation_error("Token has expired")

    @staticmethod
    def invalid_token_format() -> HTTPException:
        return AuthExceptions.token_validation_error("Invalid token format")

    @staticmethod
    def invalid_credentials() -> HTTPException:
        return AuthExceptions.token_validation_error("Could not validate credentials")

    @staticmethod
    def user_not_found() -> HTTPException:
        return AuthExceptions.token_validation_error("User not found")

    @staticmethod
    def invalid_refresh_token(error: str) -> HTTPException:
        return AuthExceptions.token_validation_error(f"Invalid refresh token: {error}")

    @staticmethod
    def invalid_token_payload() -> HTTPException:
        return AuthExceptions.token_validation_error("Invalid token payload")
