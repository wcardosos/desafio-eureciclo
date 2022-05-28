'''
    Lib: FileHandler
'''
from typing import List
from io import TextIOWrapper


class FileHandler:
    '''
        Class to handling files.
    '''
    def get_file_lines_content(self, file: TextIOWrapper) -> List[str]:
        '''
            Return the file lines content.
        '''
        return file.readlines()
