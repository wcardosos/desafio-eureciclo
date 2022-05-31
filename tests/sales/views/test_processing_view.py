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
        self.sales_mock_files_path = f'{Path(__file__).parent}/__mocks__'

    def test_file_upload(self):
        '''
            Should render the sales data.
        '''
        uploaded_file_path = f'{self.sales_mock_files_path}/sales.txt'
        with open(uploaded_file_path, 'rb') as uploaded_file:
            response = self.client.post(
                '/sales/import/processing/',
                {'sales': uploaded_file}
            )

            self.assertEqual(response.status_code, 200)
            self.assertIsNotNone(response.context['sales'])
            self.assertIsNotNone(self.client.session.get('sales_info'))

    def test_file_upload_incorrect(self):
        '''
            Should redirect to the import page with
            invalid file error.
        '''
        invalid_file = f'{self.sales_mock_files_path}/invalid.txt'
        with open(invalid_file, 'rb') as uploaded_file:
            response = self.client.post(
                '/sales/import/processing/',
                {'sales': uploaded_file}
            )

            self.assertRedirects(
                response,
                '/sales/import',
                target_status_code=301
            )
            self.assertEqual(
                self.client.session.get('import_sales_error'),
                'Estrutura de arquivo inválida'
            )

    def test_file_upload_sales_incorrect(self):
        '''
            Should redirect to the import page with
            invalid file error.
        '''
        invalid_file = f'{self.sales_mock_files_path}/sales-invalid.txt'
        with open(invalid_file, 'rb') as uploaded_file:
            response = self.client.post(
                '/sales/import/processing/',
                {'sales': uploaded_file}
            )

            self.assertRedirects(
                response,
                '/sales/import',
                target_status_code=301
            )
            self.assertEqual(
                self.client.session.get('import_sales_error'),
                'Informações da venda incorretas. As informações necessárias são: comprador, descrição, preço unitário, quantidade, endereço e fornecedor'  # noqa: E501
            )
