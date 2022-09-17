import django_filters as filters

from bit68_project.products.models import Product


class ProductFilter(filters.FilterSet):
    author = filters.CharFilter(
        field_name="author__first_name", lookup_expr="icontains"
    )
    product_name = filters.CharFilter(field_name="product_name", lookup_expr="icontains")

    created_at = filters.IsoDateTimeFilter(field_name="created_at")
    updated_at = filters.IsoDateTimeFilter(field_name="updated_at")

    class Meta:
        model = Product
        fields = ["author", "product_name", "created_at", "updated_at"]

