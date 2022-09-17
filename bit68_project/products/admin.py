from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("pkid",'product_name', 'price', 'stock', 'is_available')
    list_display_links = ["pkid",]


admin.site.register(Product, ProductAdmin)
