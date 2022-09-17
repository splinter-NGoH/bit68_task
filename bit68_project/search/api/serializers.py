from drf_haystack.serializers import HaystackSerializer

from bit68_project.search.api.search_indexes import ProductIndex


class ProductSearchSerializer(HaystackSerializer):
    class Meta:
        index_classes = [ProductIndex]

        fields = ["author", "product_name", "description", "autocomplete", "created_at", "updated_at"]
        ignore_fields = ["autocomplete"]
        field_aliases = {"q": "autocomplete"}
