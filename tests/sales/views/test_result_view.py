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

    def test_result_without_sales_info_session(self):
        '''
            Should to redirect to the homepage
            when the sales informations are not
            in the session request.
        '''
        response = self.client.get('/sales/import/processing/result')

        self.assertRedirects(response, '/sales/import', target_status_code=301)

    def test_results(self):
        '''
            Should render the import sales result.
        '''
        session = self.client.session
        session['sales_info'] = [{
            'buyer': "View Test",
            'description': "description",
            'price': 10.0,
            'quantity': 2,
            'address': "address",
            'provider': "provider"
        }]
        session.save()

        response = self.client.get('/sales/import/processing/result')

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context['total_imported_sales'])
        self.assertIsNotNone(response.context['total_price'])
