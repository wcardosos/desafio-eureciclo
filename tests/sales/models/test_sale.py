# pylint: disable=no-member,import-error
'''
    Sale model tests.
'''
from django.test import TestCase
from sales.models import Sale


class TestSale(TestCase):
    '''
        Sales test cases.
    '''
    def test_create(self):
        '''
            Should create a sale.
        '''
        new_sale_mock = {
            'buyer': "João Silva",
            'description': "R$10 off R$20 of food",
            'price': "10.0",
            'quantity': "2",
            'address': "987 Fake St",
            'provider': "Bob's Pizza"
        }

        Sale.create(new_sale_mock)

        sale_created = Sale.objects.last()

        self.assertEqual(sale_created.buyer, 'João Silva')

    def test_last_sale(self):
        '''
            Should return the last sale.
        '''
        Sale.objects.create(
            buyer="João Silva",
            description="R$10 off R$20 of food",
            price="10.0",
            quantity="2",
            address="987 Fake St",
            provider="Bob's Pizza"
        )

        last_sale = Sale.get_last()

        self.assertEqual(last_sale.buyer, "João Silva")
        self.assertEqual(last_sale.price, 10.0)
        self.assertEqual(last_sale.quantity, 2)
