# pylint: disable=no-member,import-error
'''
    Sale model tests.
'''
from unittest.mock import MagicMock
from django.test import TestCase
from sales.models import Sale


def create_sale(sale_mock: dict):
    '''
        Create sale in the test's database.
    '''
    Sale.create(sale_mock)


class TestSale(TestCase):
    '''
        Sales test cases.
    '''
    def tearDown(self):
        Sale.objects.all().delete()

    def test_create(self):
        '''
            Should create a sale.
        '''
        Sale.create({
            'buyer': "João Silva",
            'description': "R$10 off R$20 of food",
            'price': "10.0",
            'quantity': "2",
            'address': "987 Fake St",
            'provider': "Bob's Pizza"
        })

        sale_created = Sale.objects.last()

        self.assertEqual(sale_created.buyer, 'João Silva')
    
    def test_create_from_list(self):
        '''
            Should create sales from a list.
        '''
        list_mock = [
            {
                'buyer': "Test 1",
                'description': "description",
                'price': 10.0,
                'quantity': 2,
                'address': "address",
                'provider': "provider"
            },
            {
                'buyer': "Test 2",
                'description': "description",
                'price': 10.0,
                'quantity': 2,
                'address': "address",
                'provider': "provider"
            }
        ]

        Sale.create_from_list(list_mock)

        self.assertEqual(Sale.objects.count(), 2)

    def test_last_sale(self):
        '''
            Should return the last sale.
        '''
        create_sale({
            'buyer': "João Silva",
            'description': "R$10 off R$20 of food",
            'price': "10.0",
            'quantity': "2",
            'address': "987 Fake St",
            'provider': "Bob's Pizza"
        })

        last_sale = Sale.get_last()

        self.assertEqual(last_sale.buyer, "João Silva")
        self.assertEqual(last_sale.price, 10.0)
        self.assertEqual(last_sale.quantity, 2)

    def test_sales_count(self):
        '''
            Should return the sales count.
        '''
        create_sale({
            'buyer': "Test 1",
            'description': "description",
            'price': 10.0,
            'quantity': 2,
            'address': "address",
            'provider': "provider"
        })
        create_sale({
            'buyer': "Test 2",
            'description': "description",
            'price': 10.0,
            'quantity': 2,
            'address': "address",
            'provider': "provider"
        })

        count = Sale.get_count()

        self.assertEqual(count, 2)

    def test_get_all_sales_price(self):
        '''
            Should return the price of all sales.
        '''
        new_sale_mock = {
            'buyer': "Test",
            'description': "description",
            'price': 10.0,
            'quantity': 2,
            'address': "address",
            'provider': "provider"
        }
        create_sale(new_sale_mock)
        create_sale(new_sale_mock)
        create_sale(new_sale_mock)
        create_sale(new_sale_mock)

        result = Sale.get_total_price()

        self.assertEqual(result, 40.0)

    def test_compose_from_file(self):
        '''
            Should return the composed sales.
        '''
        file_handler_mock = MagicMock()
        file_handler_mock.get_file_lines_content = MagicMock()
        file_handler_mock.get_file_lines_content.return_value = 'lines content'

        txt_parser_mock = MagicMock()
        txt_parser_mock.get_composed_sales = MagicMock()
        txt_parser_mock.get_composed_sales.return_value = 'composed sales'

        result = Sale.compose_from_file(
            'file',
            file_handler_mock,
            txt_parser_mock
        )

        file_handler_mock.get_file_lines_content.assert_called_once_with('file')  # noqa: E501
        txt_parser_mock.get_composed_sales.assert_called_once_with('lines content')  # noqa: E501
        self.assertEqual(result, 'composed sales')
