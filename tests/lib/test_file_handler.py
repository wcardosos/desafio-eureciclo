'''
    FileHandler tests
'''
from unittest import TestCase, main
from unittest.mock import MagicMock
from src.lib.file_handler import FileHandler


class TestFileHandler(TestCase):
    '''
        FileHandler test cases
    '''
    def setUp(self):
        self.file_handler = FileHandler()

    def test_get_file_lines_content(self):
        '''
            Should return the file lines content.
        '''
        file_mock = MagicMock()
        file_mock.readlines = MagicMock()
        file_mock.readlines.return_value = ['line 1', 'line 2', 'line 3']

        # pylint: disable=no-member
        result = self.file_handler.get_file_lines_content(file_mock)

        file_mock.readlines.assert_called_once()
        self.assertEqual(result, ['line 1', 'line 2', 'line 3'])


if __name__ == '__main__':
    main()
