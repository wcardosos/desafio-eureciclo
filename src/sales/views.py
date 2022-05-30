# pylint: disable=no-member
'''
    Sales views.
'''
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
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

    def get(self, *args, **kwargs) -> HttpResponse:
        '''
            Save the sales and render the results.
        '''
        self.request.session.modified = True
        sales_info = self.request.session.get('sales_info')

        if not sales_info:
            return redirect('/sales')

        Sale.create_from_list(sales_info)

        total_imported_sales = Sale.get_total_imported_sales(sales_info)
        total_price_from_imported_sales = Sale.get_total_price_from_imported_sales(  # noqa: E501
            sales_info
        )

        results = {
            'total_imported_sales': total_imported_sales,
            'total_price': total_price_from_imported_sales
        }

        self.request.session['sales_info'] = None

        return render(self.request, 'result.html', results)
