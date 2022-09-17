from django.db import models

class CartItemManagers (models.Manager):
    def sub_total(self):
        return super(CartItemManagers, self).product.price * self.quantity
    def item_in_cart(self):
        return super(CartItemManagers, self).items_in_cart.all()