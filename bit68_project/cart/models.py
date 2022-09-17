from django.contrib.auth import get_user_model
from django.db import models
from .managers import CartItemManagers
from bit68_project.common.models import TimeStampedUUIDModel
from bit68_project.products.models import Product
User = get_user_model()


class Cart(TimeStampedUUIDModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cart_id = models.CharField(max_length=250, blank=True)
    total_price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.cart_id} "

class CartItem(TimeStampedUUIDModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart    = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, related_name="items_in_cart")
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    objects = CartItemManagers()

    def __str__(self):
        return self.product.product_name
