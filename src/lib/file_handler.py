'''
    Lib: FileHandler
'''
from typing import List
from io import TextIOWrapper


class FileHandler:
    '''
        Class to handling files.
    '''
    def extract_lines(self, file: TextIOWrapper) -> List[str]:
        '''
            Extract file lines.
        '''
        return file.readlines()
