from django.utils import timezone
from haystack import indexes

from bit68_project.products.models import Product


class ProductIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True)
    author = indexes.CharField(model_attr="author")
    product_name = indexes.CharField(model_attr="product_name")
    description = indexes.CharField(model_attr="description")
    created_at = indexes.CharField(model_attr="created_at")
    updated_at = indexes.CharField(model_attr="updated_at")

    @staticmethod
    def prepare_author(obj):
        return "" if not obj.author else obj.author.username

    @staticmethod
    def prepare_autocomplete(obj):
        return " ".join((obj.author.username, obj.title, obj.description))

    def get_model(self):
        return Product

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(created_at__lte=timezone.now())
