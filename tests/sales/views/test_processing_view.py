# pylint: disable=no-member,import-error
'''
    Home view tests.
'''
from pathlib import Path
from django.test import TestCase, Client


class TestProcessingView(TestCase):
    '''
            Home view test cases.
    '''
    def setUp(self):
        self.client = Client()
        self.sales_mock_file_path = f'{Path(__file__).parent}/__mocks__/sales.txt'  # noqa: E501

    def test_file_upload(self):
        '''
            Should render the sales data.
        '''

        with open(self.sales_mock_file_path, 'rb') as uploaded_file:
            response = self.client.post(
                '/sales/processing/',
                {'sales': uploaded_file}
            )

            self.assertEqual(response.status_code, 200)
            self.assertIsNotNone(response.context['sales'])
            self.assertIsNotNone(self.client.session.get('sales_info'))
