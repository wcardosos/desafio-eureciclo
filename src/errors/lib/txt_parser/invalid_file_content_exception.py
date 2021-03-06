'''
    Exception: InvalidFileContent
'''


class InvalidFileContentException(Exception):
    '''
        Exception that should be raises when the
        file content is not a list.
    '''
    def __init__(self, message):
        Exception.__init__(self, message)
