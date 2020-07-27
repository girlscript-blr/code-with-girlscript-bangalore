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
    path("create_item/", views.create_item, name="create_item"),
    path("edit_category/<int:category_id>/", views.edit_category, name="edit_category"),
    path(
        "edit_category/<int:category_id>/delete",
        views.delete_category,
        name="delete_category",
    ),
    path("create_category/", views.create_category, name="create_category"),
    path("edit_item/<int:item_id>/", views.edit_item, name="edit_item"),
    path("edit_item/<int:item_id>/delete", views.delete_item, name="delete_item"),
    path("all_orders/", views.show_all_orders, name="all_orders"),
    path("all_items/", views.show_all_items, name="all_items"),
    path("all_categories/", views.show_all_categories, name="all_categories"),
    path("vendor/", views.vendor, name="vendor"),
    path("status/", views.get_order_status, name="order_status"),
]
