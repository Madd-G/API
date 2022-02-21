from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

from .models import *

# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List product': '/productlist/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
        }

    return Response(api_urls)


@api_view(['GET', 'DELETE', 'PUT'])
def customerList(request):
    customer = Customer.objects.all()
    return Response(request)

@api_view(['GET'])
def productList(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)

def orderList(request):
    # order = Order.objects.all()
    return Response(request)
