from rest_framework.viewsets import ModelViewSet

from order.models import Order
from order.serializers.order_serializers import OrderSerializers


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializers
    queryset = Order.objects.all()
