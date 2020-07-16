from django.urls import path, include
from shoppingcart import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_to_cart/", views.add_to_cart, name="add_to_cart"),
    path("clear_cart/", views.clear_cart, name="clear_cart"),
    path("shopping_list/", views.display_shopping_list, name="display_shopping_list"),
    path("order/", views.create_order, name="create_order"),
]
