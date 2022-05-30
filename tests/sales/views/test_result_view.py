# pylint: disable=no-member,import-error
'''
    Result view tests.
'''
from django.test import TestCase, Client


class TestProcessingView(TestCase):
    '''
            Result view test cases.
    '''
    def setUp(self):
        self.client = Client()

    def test_result(self):
        '''
            Should render the import results.
        '''
        response = self.client.get('/sales/processing/result')

        self.assertEqual(response.status_code, 200)
