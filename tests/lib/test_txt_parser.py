'''
    TxtParser tests
'''
from unittest import TestCase, main
from src.lib.txt_parser import TxtParser


class TestTxtParser(TestCase):
    '''
        TxtParser test cases
    '''
    def setUp(self):
        self.txt_parser = TxtParser()

    def test_get_line_data(self):
        '''
            Should get the sale data by a string that is a file line.
        '''
        line_mock = 'João Silva	R$10 off R$20 of food	10.0	2	987 Fake St	Bob\'s Pizza'  # noqa: E501

        # pylint: disable=no-member
        result = self.txt_parser.get_line_data(line_mock)

        self.assertAlmostEqual(result, [
            'João Silva',
            'R$10 off R$20 of food',
            '10.0',
            '2',
            '987 Fake St',
            'Bob\'s Pizza'
        ])

    def test_compose_sale_data(self):
        '''
            Should return the sale data composed,
            ready to save in the database.
        '''
        sales_data_mock = [
            'João Silva',
            'R$10 off R$20 of food',
            '10.0',
            '2',
            '987 Fake St',
            'Bob\'s Pizza'
        ]

        result = self.txt_parser.compose_sales_data(sales_data_mock)

        self.assertDictEqual(result, {
            'buyer': "João Silva",
            'description': "R$10 off R$20 of food",
            'price': "10.0",
            'quantity': "2",
            'address': "987 Fake St",
            'provider': "Bob's Pizza"
        })

    def test_get_sales_data_composed(self):
        '''
            Should get the data composed.
        '''
        sales_informations_mock = [
            "Comprador	Descrição	Preço Unitário	Quantidade	Endereço	Fornecedor",  # noqa: E501
            "João Silva	R$10 off R$20 of food	10.0	2	987 Fake St	Bob's Pizza",
            "Amy Pond	R$30 of awesome for R$10	10.0	5	456 Unreal Rd	Tom's Awesome Shop"  # noqa: E501
        ]

        # pylint: disable=no-member
        result = self.txt_parser.get_sales_data_composed(
            sales_informations_mock
        )

        self.assertEqual(result, [
            {
                'buyer': "João Silva",
                'description': "R$10 off R$20 of food",
                'price': "10.0",
                'quantity': "2",
                'address': "987 Fake St",
                'provider': "Bob's Pizza"
            },
            {
                'buyer': "Amy Pond",
                'description': "R$30 of awesome for R$10",
                'price': "10.0",
                'quantity': "5",
                'address': "456 Unreal Rd",
                'provider': "Tom's Awesome Shop"
            }
        ])


if __name__ == '__main__':
    main()
