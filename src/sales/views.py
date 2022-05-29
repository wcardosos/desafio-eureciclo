'''
    Sales views.
'''
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Sale


class HomeView(TemplateView):
    '''
        Homepage view.
    '''
    template_name = 'index.html'

    def get(self, *args, **kwargs) -> HttpResponse:
        last_sale = Sale.get_last()

        data = {
            'last_sale': last_sale
        }

        return render(self.request, 'index.html', data, last_sale)
