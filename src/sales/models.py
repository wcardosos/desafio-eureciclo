# pylint: disable=no-member
'''
    Sale app models.
'''
from typing import Any, List
from django.db import models
from django.core.files.uploadedfile import UploadedFile
from errors.lib.txt_parser.invalid_file_content_exception import (
    InvalidFileContentException
)
from lib.file_handler import FileHandler
from lib.txt_parser import TxtParser


class Sale(models.Model):
    '''
        Model to represent a sale.
    '''
    buyer = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    address = models.CharField(max_length=255)
    provider = models.CharField(max_length=255)

    @classmethod
    def create(cls, sale_data: dict) -> None:
        '''
            Create a sale.
        '''
        try:
            buyer = sale_data['buyer']
            description = sale_data['description']
            price = float(sale_data['price'])
            quantity = int(sale_data['quantity'])
            address = sale_data['address']
            provider = sale_data['provider']
        except KeyError:
            raise InvalidFileContentException() from KeyError

        cls.objects.create(
            buyer=buyer,
            description=description,
            price=price,
            quantity=quantity,
            address=address,
            provider=provider,
        )

    @property
    def total_price(self) -> float:
        '''
            Return sale's total price.
        '''
        return self.price * self.quantity

    @staticmethod
    def get_last() -> Any:
        '''
            Return the last sale.
        '''
        return Sale.objects.last()

    @staticmethod
    def get_count() -> int:
        '''
            Return the sales count.
        '''
        return Sale.objects.count()

    @staticmethod
    def get_total_price() -> float:
        '''
            Return the sales total price.
        '''
        all_sales = Sale.objects.all()

        return sum(list(map(lambda sale: sale.total_price, all_sales)))

    @staticmethod
    def compose_from_file(
        file: UploadedFile,
        file_handler: FileHandler,
        txt_parser: TxtParser
    ) -> dict:
        '''
            Compose the sales data from the uploaded file.
        '''
        file_content = file_handler.get_file_lines_content(file)

        return txt_parser.get_composed_sales(file_content)

    @staticmethod
    def create_from_list(sales_list: List[dict]) -> None:
        '''
            Create sales from a list.
        '''
        for sale in sales_list:
            Sale.create(sale)

    @staticmethod
    def get_total_imported_sales(sales: list) -> int:
        '''
            Return the number of imported sales from a file.
        '''
        return len(sales)

    @staticmethod
    def get_total_price_from_imported_sales(sales: list) -> float:
        '''
            Return the imported sales total price.
        '''
        total_price = 0.0

        for sale in sales:
            total_price += float(sale['price']) * int(sale['quantity'])

        return total_price
