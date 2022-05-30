# pylint: disable=no-member
'''
    Sales views.
'''
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse

from lib.file_handler import FileHandler
from lib.txt_parser import TxtParser
from .models import Sale


class HomeView(TemplateView):
    '''
        Homepage view.
    '''
    template_name = 'index.html'

    def get(self, *args, **kwargs) -> HttpResponse:
        last_sale = Sale.get_last()
        sales_count = Sale.get_count()
        sales_total_price = Sale.get_total_price()

        data = {
            'last_sale': last_sale,
            'sales_count': sales_count,
            'sales_total_price': sales_total_price
        }

        return render(self.request, 'index.html', data)


class ProcessingView(TemplateView):
    '''
        Processing sale view.
    '''
    template_name = 'processing.html'

    def post(self, *args, **kwargs) -> HttpResponse:
        '''
            Process the import sales file.
        '''
        file_handler = FileHandler()
        txt_parser = TxtParser()

        sales_info = Sale.compose_from_file(
            self.request.FILES['sales'],
            file_handler,
            txt_parser
        )

        self.request.session['sales_info'] = sales_info

        return render(self.request, 'processing.html', {'sales': sales_info})


class ResultView(TemplateView):
    '''
        Import result view.
    '''
    template_name = 'result.html'

    def post(self, *args, **kwargs) -> HttpResponse:
        return render(self.request, 'result.html')
