'''
    Exception: InvalidLineContent
'''


class InvalidLineContentException(Exception):
    '''
        Exception that should be raises when the
        line content is not a string.
    '''
    def __init__(self, message):
        Exception.__init__(self, message)
