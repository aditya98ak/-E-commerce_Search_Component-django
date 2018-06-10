from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Product
import random

# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    # queryset = Product.objects.all()

    # Note that I haven't provided the template name overhere. Django automaticlly searches for that

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #
    #     return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        items = sorted(Product.objects.all(), key=lambda x: random.random())
        return  items #Then we can get rid of the queryset call at the beginning of this class which is now commented.