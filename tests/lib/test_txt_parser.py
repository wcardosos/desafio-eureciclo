# pylint: disable=no-member,import-error
'''
    TxtParser tests
'''
from unittest import TestCase, main
from lib.txt_parser import TxtParser
from errors.lib.txt_parser.invalid_line_content_exception import (
    InvalidLineContentException
)
from errors.lib.txt_parser.invalid_file_content_exception import (
    InvalidFileContentException
)


class TestTxtParser(TestCase):
    '''
        TxtParser test cases
    '''
    def setUp(self):
        self.txt_parser = TxtParser()

    def test_get_sale_content_from_line(self):
        '''
            Should get the sale content from line.
        '''
        line_mock = 'João Silva	R$10 off R$20 of food	10.0	2	987 Fake St	Bob\'s Pizza'  # noqa: E501

        result = self.txt_parser.get_sale_content_from_line(line_mock)

        self.assertAlmostEqual(result, [
            'João Silva',
            'R$10 off R$20 of food',
            '10.0',
            '2',
            '987 Fake St',
            'Bob\'s Pizza'
        ])

    def test_raises_expection_when_the_content_is_not_str(self):
        '''
            Should raises a exception when the sale content is
            not a string.
        '''
        line_mock = None

        with self.assertRaises(InvalidLineContentException):
            self.txt_parser.get_sale_content_from_line(line_mock)

    def test_compose_sale(self):
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

        result = self.txt_parser.compose_sale(sales_data_mock)

        self.assertDictEqual(result, {
            'buyer': "João Silva",
            'description': "R$10 off R$20 of food",
            'price': "10.0",
            'quantity': "2",
            'address': "987 Fake St",
            'provider': "Bob's Pizza"
        })

    def test_get_get_composed_sales(self):
        '''
            Should get the data composed.
        '''
        sales_from_file_mock = [
            "Comprador	Descrição	Preço Unitário	Quantidade	Endereço	Fornecedor",  # noqa: E501
            "João Silva	R$10 off R$20 of food	10.0	2	987 Fake St	Bob's Pizza",
            "Amy Pond	R$30 of awesome for R$10	10.0	5	456 Unreal Rd	Tom's Awesome Shop"  # noqa: E501
        ]

        result = self.txt_parser.get_composed_sales(
            sales_from_file_mock
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

    def test_raise_error_when_the_file_content_is_not_list(self):
        '''
            Should raises when the file content is not a list
        '''
        sales_from_file_mock = None

        with self.assertRaises(InvalidFileContentException):
            self.txt_parser.get_composed_sales(sales_from_file_mock)


if __name__ == '__main__':
    main()
