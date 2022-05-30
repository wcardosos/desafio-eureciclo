'''
    Lib: FileHandler
'''
from typing import List, Union
from io import TextIOWrapper


class FileHandler:
    '''
        Class to handling files.
    '''
    @classmethod
    def check_has_bytes_content(
        cls,
        content: Union[List[str], List[bytes]]
    ) -> bool:
        '''
            Check if the file was readed as bytes.
        '''
        return all(isinstance(data, bytes) for data in content)

    def get_file_lines_content(self, file: TextIOWrapper) -> List[str]:
        '''
            Return the file lines content.
        '''
        content = file.readlines()

        if self.check_has_bytes_content(content):
            content = list(map(lambda data: data.decode(), content))

        return content
