""" Custom exceptions """

class BaseHTTPException(Exception):
    """ Universal exception for all custom errors """
    status = 400


class EmptyRequestBodyError(BaseHTTPException):
    """ Empty request body when it's required """
    @staticmethod
    def __str__() -> str:
        return 'Empty request body'


class UsernameIsAlreadyExists(BaseHTTPException):
    """ Specified username already registered """
    @staticmethod
    def __str__() -> str:
        return "Username already registered"


class WrongAuthCredentials(BaseHTTPException):
    """ Wrong username or password """
    @staticmethod
    def __str__() -> str:
        return "Wrong username or password"
