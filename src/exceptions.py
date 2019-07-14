"""Custom exceptions."""


class BaseHTTPException(Exception):
    """Universal exception for all custom errors."""

    status = 400


class EmptyRequestBodyError(BaseHTTPException):
    """Empty request body when it's required."""

    def __str__(self) -> str:
        """Return exception text."""
        return 'Empty request body'


class UsernameIsAlreadyExists(BaseHTTPException):
    """Specified username already registered."""

    def __str__(self) -> str:
        """Return exception text."""
        return 'Username already registered'


class WrongAuthCredentials(BaseHTTPException):
    """Wrong username or password."""

    def __str__(self) -> str:
        """Return exception text."""
        return 'Wrong username or password'
