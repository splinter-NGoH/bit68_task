from django.contrib.auth import get_user_model
from rest_framework import serializers

from bit68_project.cart.models import CartItem

User = get_user_model()


class CartSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_created_at(self, obj):
        now = obj.created_at
        formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
        return formatted_date

    def get_updated_at(self, obj):
        then = obj.updated_at
        formatted_date = then.strftime("%m/%d/%Y, %H:%M:%S")
        return formatted_date

    class Meta:
        model = CartItem
        fields = ["id", "product","quantity","is_active", "created_at", "updated_at"]


class CartItemListSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    product = serializers.ReadOnlyField(source="product.product_name")
    cart = serializers.ReadOnlyField(source="cart.cart_id")
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_created_at(self, obj):
        now = obj.created_at
        formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
        return formatted_date

    def get_updated_at(self, obj):
        then = obj.updated_at
        formatted_date = then.strftime("%m/%d/%Y, %H:%M:%S")
        return formatted_date

    class Meta:
        model = CartItem
        fields = ["id", "author", "product", "cart","quantity","is_active", "created_at", "updated_at"]
