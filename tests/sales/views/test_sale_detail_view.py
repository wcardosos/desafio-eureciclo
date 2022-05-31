# pylint: disable=no-member,import-error
'''
    Sales list view tests.
'''
from django.test import TestCase, Client
from sales.models import Sale


def create_sale() -> None:
    '''
        Create sale in test's database
    '''
    new_sale = {
        'buyer': "Detail View Test",
        'description': "description",
        'price': 10.0,
        'quantity': 2,
        'address': "address",
        'provider': "provider"
    }
    Sale.create(new_sale)


class TestSalesListView(TestCase):
    '''
        Sales list view test cases.
    '''
    def setUp(self):
        self.client = Client()

    def test_sale_list(self):
        '''
            Should sales list is passed to the page.
        '''
        create_sale()

        response = self.client.get('/sales/', pk=1)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Detail View Test')
