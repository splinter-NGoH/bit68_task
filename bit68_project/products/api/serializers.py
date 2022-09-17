from rest_framework import serializers

from bit68_project.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    banner_image = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_banner_image(self, obj):
        return obj.image.url

    def get_created_at(self, obj):
        now = obj.created_at
        formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
        return formatted_date

    def get_updated_at(self, obj):
        then = obj.updated_at
        formatted_date = then.strftime("%m/%d/%Y, %H:%M:%S")
        return formatted_date



    class Meta:
        model = Product
        fields = [
            "id",
            "product_name",
            "slug",
            "description",
            "price",
            "banner_image",
            "stock",
            "is_available",
            "created_at",
            "updated_at",
        ]
