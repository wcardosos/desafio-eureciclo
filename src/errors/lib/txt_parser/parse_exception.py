'''
    Exception: Parse
'''


class ParseException(Exception):
    '''
        Exception that should be raises when an error
        occurred while the parsing is doing.
    '''
    def __init__(self, error_message: str):
        Exception.__init__(
            self,
            f'An error occurred while parsing the file content. Error: {error_message}'  # noqa: E501
        )
