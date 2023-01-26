from _winapi import PROCESS_DUP_HANDLE

from django.shortcuts import render

# Create your views here.
from app.models import Product


def index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'app/index.html', context)