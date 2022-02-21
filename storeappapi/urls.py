from django.urls import path
from . views import *

urlpatterns = [
    path('', apiOverview, name="api-overview"),
    path('productlist/', productList, name='productlist'),
    path('customer/', customerList, name='customertlist'),
    path('order/', orderList, name='orderlist'),
]