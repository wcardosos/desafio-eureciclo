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

    def test_extract_lines(self):
        '''
            Test the method that extract file lines
        '''
        file_mock = MagicMock()
        file_mock.readlines = MagicMock()
        file_mock.readlines.return_value = ['line 1', 'line 2', 'line 3']

        # pylint: disable=no-member
        result = self.file_handler.extract_lines(file_mock)

        file_mock.readlines.assert_called_once()
        self.assertEqual(result, ['line 1', 'line 2', 'line 3'])


if __name__ == '__main__':
    main()
