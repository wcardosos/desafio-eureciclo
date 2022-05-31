'''
    Exception: Parse
'''


class ParseException(Exception):
    '''
        Exception that should be raises when an error
        occurred while the parsing have been doing.
    '''
    def __init__(self, message: str):
        Exception.__init__(self, message)
