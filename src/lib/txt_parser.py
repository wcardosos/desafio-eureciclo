# pylint: disable=import-error,too-many-function-args
'''
    Lib: TxtParser
'''
from typing import List
from errors.lib.txt_parser.invalid_line_content_exception import (
    InvalidLineContentException
)
from errors.lib.txt_parser.invalid_file_content_exception import (
    InvalidFileContentException
)
from errors.lib.txt_parser.parse_exception import ParseException


class TxtParser:
    '''
        Class to parse .txt files to extract sales data.
    '''
    def get_sale_content_from_line(self, line: str) -> List[str]:
        '''
            Return the line content separated by TAB
        '''
        if not isinstance(line, str):
            raise InvalidLineContentException('Dados de venda inválidos')

        sale_content = line.split('\t')

        if len(sale_content) != 6:
            raise InvalidLineContentException('Informações da venda incorretas. As informações necessárias são: comprador, descrição, preço unitário, quantidade, endereço e fornecedor')  # noqa: E501

        return sale_content

    def compose_sale(self, sale_content_from_line: List[str]) -> dict:
        '''
            Return the composed sale.

            The line's content should be linked with the
            following informations:
                - buyer
                - description
                - price
                - quantity
                - address
                - provider
        '''
        sale_keys = [
            "buyer",
            "description",
            "price",
            "quantity",
            "address",
            "provider",
        ]
        data_dict = {}
        try:
            for index, sale_content in enumerate(sale_content_from_line):
                sale_info = sale_keys[index]
                data_dict[sale_info] = sale_content
        except Exception as error:
            raise ParseException(error) from error

        return data_dict

    def check_is_valid_header(self, header_line: str) -> bool:
        '''
            Check is a header is valid.
        '''
        valid_header_accepted_values = [
            'Comprador',
            'Descrição',
            'Preço Unitário',
            'Quantidade',
            'Endereço',
            'Fornecedor',
        ]

        for valid_header_value in valid_header_accepted_values:
            if valid_header_value not in header_line:
                return False

        return True

    def get_composed_sales(
        self,
        sales_from_file: List[str]
    ) -> List[dict]:
        '''
            Return the composed sales from file.
        '''
        if not isinstance(sales_from_file, list):
            raise InvalidFileContentException('Dados inconsistentes')

        if not self.check_is_valid_header(sales_from_file[0]):
            raise InvalidFileContentException('Estrutura de arquivo inválida')

        sales_from_line_without_header = sales_from_file[1:]
        sales_data = list(map(
            self.get_sale_content_from_line,
            sales_from_line_without_header
        ))
        sales_data_composed = list(map(self.compose_sale, sales_data))

        return sales_data_composed
