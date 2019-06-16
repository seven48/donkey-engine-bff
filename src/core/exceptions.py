""" Custom exceptions """

class BaseHTTPException(Exception):
    """ Universal exception for all custom errors """
    status = 400
