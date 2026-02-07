from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]

    filterset_class = ProductFilter

    ordering_fields = [
        'price',
        'created_at',
    ]

    ordering = ['-created_at']  
