from django.urls import path

from app.views import index, ShopPage, contact

urlpatterns = [
    path('', index, name='index'),
    path('shop/', ShopPage.as_view(), name='shop'),
    path('contact/', contact, name='contact')
]
