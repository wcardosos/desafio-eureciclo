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

    def tearDown(self) -> None:
        Sale.objects.all().delete()

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
        self.assertContains(response, 'View Test - R$ 20.00')

    def test_sales_count(self):
        '''
            Should send the sales count in the
            context.
        '''
        create_sale()
        create_sale()
        create_sale()

        response = self.client.get('/sales/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['sales_count'], 3)

    def test_sales_total_price(self):
        '''
            Should render the sales total price.
        '''
        create_sale()
        create_sale()

        response = self.client.get('/sales/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['sales_total_price'], 40.0)
        self.assertContains(response, 'R$ 40.00')
