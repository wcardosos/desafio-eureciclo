# pylint: disable=no-member,import-error
'''
    Home view tests.
'''
from django.test import TestCase, Client
from sales.models import Sale


def create_sale() -> None:
    '''
        Create sale in test's database
    '''
    new_sale = {
        'buyer': "View Test",
        'description': "description",
        'price': 10.0,
        'quantity': 2,
        'address': "address",
        'provider': "provider"
    }
    Sale.create(new_sale)


class TestHomeView(TestCase):
    '''
        Home view test cases.
    '''
    def setUp(self):
        self.client = Client()

    def test_last_sale_none(self):
        '''
            Should render a message when the last sale
            is None.
        '''
        response = self.client.get('/sales/')

        self.assertEqual(response.status_code, 200)
        self.assertIsNone(response.context['last_sale'])
        self.assertContains(response, 'Sem vendas cadastradas')
    
    def test_show_last_sale_data(self):
        '''
            Should render sale's buyer, price and
            quantity.
        '''
        create_sale()

        response = self.client.get('/sales/')

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context['last_sale'])
        self.assertContains(response, 'Nome: View Test')
        self.assertContains(response, 'Preço: 10.0')
        self.assertContains(response, 'Quantidade: 2')