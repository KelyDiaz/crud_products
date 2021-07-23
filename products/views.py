from django_filters.rest_framework import DjangoFilterBackend
from polaris.common.views import ModelViewSet
from rest_framework.filters import OrderingFilter

from products.models import ProductModel
from products.serializers import ProductSerializer


class ProductView(ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'category', 'serie']
    ordering_fields = ['name', 'category']
