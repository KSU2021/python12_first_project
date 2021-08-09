from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from product.models import Product

# class ProductSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     description = serializers.CharField()
#     price = serializers.DecimalField()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'price')






