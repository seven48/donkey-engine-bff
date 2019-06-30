""" Custom exceptions """

class BaseHTTPException(Exception):
    """ Universal exception for all custom errors """
    status = 400


class EmptyRequestBodyError(BaseHTTPException):
    """ Empty request body when it's required """
    @staticmethod
    def __str__():
        return 'Empty request body'


class UsernameIsAlreadyExists(BaseHTTPException):
    """ Specified username already registered """
    @staticmethod
    def __str__():
        return "Username already registered"
