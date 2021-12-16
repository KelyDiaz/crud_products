
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from products.models import ProductModel
from products.serializers import ProductSerializer


class ProductView(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [OrderingFilter]
    filterset_fields = ['name', 'category', 'serie']
    ordering_fields = ['name', 'category']
