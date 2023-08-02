from rest_framework import serializers

from product.models.product import Product
from product.serializers.category_serializers import CategorySerializers


class ProductSerializers(serializers.ModelSerializer):
    category = CategorySerializers(required=True, many=True)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'active',
            'category'
        ]
