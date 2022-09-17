from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from bit68_project.common.models import TimeStampedUUIDModel
from bit68_project.products.mangers import ProductManger
User = get_user_model()




class Product(TimeStampedUUIDModel):
    product_name    = models.CharField(verbose_name=_("product name"),max_length=200, unique=True)
    slug            = AutoSlugField(populate_from="product_name", always_update=True, unique=True)
    description     = models.TextField(verbose_name=_("description"),max_length=500, blank=True)
    price           = models.IntegerField(verbose_name=_("price"),)
    image = models.ImageField(
        verbose_name=_("image"), default="/default_product.png"
    )    
    stock           = models.IntegerField(verbose_name=_("stock"))
    is_available    = models.BooleanField(verbose_name=_("is available"), default=True)

    objects = ProductManger()

    def __str__(self):
        return self.product_name
