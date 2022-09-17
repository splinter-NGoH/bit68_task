from django.urls import path
from rest_framework import routers

from .views import SearchProductView

router = routers.DefaultRouter()
router.register("search", SearchProductView, basename="search-product")

urlpatterns = [
    path("search/", SearchProductView.as_view({"get": "list"}), name="search-product")
]
