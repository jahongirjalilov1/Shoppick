from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView

from app.forms import ProductModelForm
from app.models import Product


def index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'app/index.html', context)

# def shop(request):
#     products = Product.objects.all().order_by()
#     context = {
#         'products': products
#     }
#     return  render(request, 'app/shop.html', context)

class ShopPage(ListView):
    template_name = 'app/shop.html'
    model = Product
    queryset = Product.objects.all().order_by()
    context_object_name = 'product'

def contact(request):
    products = Product.objects.all()
    if request == 'POST':
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    context = {
        'products': products
    }
    return render(request, 'app/contact.html', context)





