from rest_framework import serializers
from storeapp.models import *

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"
