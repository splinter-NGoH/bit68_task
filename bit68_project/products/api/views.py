import logging

from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from bit68_project.products.models import Product

from .filters import ProductFilter
from .pagination import ProductPagination

from .serializers import (
    ProductSerializer,
)

User = get_user_model()



class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Product.objects.all().order_by("-price")
    pagination_class = ProductPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = ProductFilter
    ordering_fields = ["created_at", "username"]