# pylint: disable=no-member
'''
    Sale app models.
'''
from typing import Any, List
from django.db import models
from django.core.files.uploadedfile import UploadedFile
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
        buyer = sale_data['buyer']
        description = sale_data['description']
        price = sale_data['price']
        quantity = sale_data['quantity']
        address = sale_data['address']
        provider = sale_data['provider']

        cls.objects.create(
            buyer=buyer,
            description=description,
            price=price,
            quantity=quantity,
            address=address,
            provider=provider,
        )

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
        return Sale.objects.aggregate(models.Sum('price'))['price__sum']

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
