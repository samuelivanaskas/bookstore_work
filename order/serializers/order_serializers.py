from rest_framework import serializers

from product.models import Product
from product.serializers.product_serializers import ProductSerializers


def get_total(instance):
    total = sum([product.price for product in instance.product.all()])
    return total


class OrderSerializers(serializers.ModelSerializer):
    product = ProductSerializers(required=True, many=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['product', 'total']
