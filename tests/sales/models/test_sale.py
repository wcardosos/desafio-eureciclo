# pylint: disable=no-member,import-error
'''
    Sale model tests.
'''
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

        result = Sale.get_all_sales_price()

        self.assertEqual(result, 40.0)
