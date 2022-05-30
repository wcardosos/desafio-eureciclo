'''
    Config that is loaded in the settings INSTALLED_APPS.
'''
from django.apps import AppConfig


class SalesConfig(AppConfig):
    '''
        Sales app config.
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sales'
