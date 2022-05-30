# pylint: disable=no-member
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

    def test_check_has_bytes_content_with_bytes_list(self):
        '''
            Should return true when the content list elements
            are bytes.
        '''
        content_mock = [b'content 1', b'content 2']

        result = self.file_handler.check_has_bytes_content(content_mock)

        self.assertTrue(result)

    def test_check_has_bytes_content_with_str_list(self):
        '''
            Should return false when the content list elements
            are strings.
        '''
        content_mock = ['content 1', 'content 2']

        result = self.file_handler.check_has_bytes_content(content_mock)

        self.assertFalse(result)

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

    def test_get_file_lines_content_with_file_content_as_bytes(self):
        '''
            Should return the file lines content converted to str.
        '''
        file_mock = MagicMock()
        file_mock.readlines = MagicMock()
        file_mock.readlines.return_value = [b'line 1', b'line 2', b'line 3']

        # pylint: disable=no-member
        result = self.file_handler.get_file_lines_content(file_mock)

        file_mock.readlines.assert_called_once()
        self.assertEqual(result, ['line 1', 'line 2', 'line 3'])


if __name__ == '__main__':
    main()
