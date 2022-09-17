from django.urls import path

from .views import CartApiView

urlpatterns = [
    path('<slug:slug>/cart/', CartApiView.as_view(), name='cart_items'),
    # path('<slug:slug>/cart/<str:id>', CartDeleteUpdateApiView.as_view(), name='cart'),

]
