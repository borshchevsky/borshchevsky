from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Product


def index(request):
    turn_on_block = True
    greeting = 'Hello'
    return render(request, 'index.html', {
        'turn_on_block': turn_on_block,
        'greeting': greeting,
    })


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product
