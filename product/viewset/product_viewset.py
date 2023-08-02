from rest_framework.viewsets import ModelViewSet

from product.models import Product
from product.serializers.product_serializers import ProductSerializers


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializers

    def get_queryset(self):
        return Product.objects.all()
