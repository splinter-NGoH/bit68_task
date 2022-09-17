from drf_haystack import viewsets
from drf_haystack.filters import HaystackAutocompleteFilter
from rest_framework import permissions

from bit68_project.products.models import Product

from .serializers import ProductSearchSerializer


class SearchProductView(viewsets.HaystackViewSet):
    permission_classes = [permissions.AllowAny]
    index_models = [Product]
    serializer_class = ProductSearchSerializer
    filter_backends = [HaystackAutocompleteFilter]
