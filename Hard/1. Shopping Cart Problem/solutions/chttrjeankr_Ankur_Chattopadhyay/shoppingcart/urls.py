from django.urls import path

from shoppingcart import views

urlpatterns = [
    path("", views.index, name="index"),
    path("clear_cart/", views.clear_cart, name="clear_cart"),
    path("categories/", views.display_categories, name="categories"),
    path(
        "shopping_list/<int:category>/",
        views.display_shopping_list,
        name="display_shopping_list",
    ),
    path("order/", views.create_order, name="create_order"),
    path("status/", views.get_order_status, name="order_status"),
]
