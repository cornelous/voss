"""
Currency Converter API Exceptions
"""

class CurrencyConverterError(Exception):
    '''Base Currency Converter error.'''
    status_code = 500

class CurrencyConverterRequestError(CurrencyConverterError):
    '''Currency Converter request error.'''


class CurrencyConverterAPIError(CurrencyConverterError):
    '''Currency Converter API error.'''


