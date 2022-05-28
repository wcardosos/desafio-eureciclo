# pylint: disable=no-member
'''
    Sale app models.
'''
from django.db import models


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
