'''
    Lib: TxtParser
'''
from typing import List


class TxtParser:
    '''
        Class to parse .txt files to extract sales data.
    '''
    def get_line_data(self, line: str) -> List[str]:
        '''
            Return the data separated by TAB
        '''
        return line.split('\t')

    def compose_sales_data(self, sales_data: List[str]) -> dict:
        '''
            Compose the sales data linking the list's position
            with the dict key.
        '''
        sales_data_keys = [
            "buyer",
            "description",
            "price",
            "quantity",
            "address",
            "provider",
        ]
        data_dict = {}

        for index, info in enumerate(sales_data):
            data_dict[sales_data_keys[index]] = info

        return data_dict

    def get_sales_data_composed(
        self,
        sales_informations: List[str]
    ) -> List[dict]:
        '''
            Extract sales data.

            The first item is the first line of the .txt file with the
            following schema:
                - buyer
                - description
                - price
                - quantity
                - address
                - provider

            This informations are separated by TAB on the string;

            The goal is return a dict's list with the information's values.
        '''
        sales_data = list(map(
            self.get_line_data,
            sales_informations[1:]
        ))
        sales_data_composed = list(map(self.compose_sales_data, sales_data))

        # for data in sales_data:
        #     data_dict = {}
        #     for index, info in enumerate(data):
        #         data_dict[sales_data_keys[index]] = info
        #     sales_data_composed.append(data_dict)

        return sales_data_composed
