from django.contrib import admin
from django.urls import path, include
from storeappapi.views import *
from storeapp.viewset_api import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('customerList', CustomerViewSet)
router.register('productList', ProductViewSet)
router.register('OrderList', OrderViewSet)

urlpatterns = [
    path('routerapi/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/', include('storeappapi.urls')),

]