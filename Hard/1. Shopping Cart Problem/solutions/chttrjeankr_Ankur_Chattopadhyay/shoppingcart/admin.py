from datetime import datetime

from django.contrib import admin

from shoppingcart.models import Category, Item, Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    actions = ["mark_as_complete", "mark_as_cancelled", "mark_as_in_transit"]
    list_display = (
        "pk",
        "order_status",
        "billing_date_time",
        "order_modified",
        "amount_payable",
        "delivery_option",
        "payment_method",
    )
    list_filter = ("order_status", "delivery_option")

    def mark_as_complete(self, request, queryset):
        queryset.update(order_status="COMP", order_modified=datetime.now())

    mark_as_complete.short_description = "Mark selected orders as completed"

    def mark_as_cancelled(self, request, queryset):
        queryset.update(order_status="CANC", order_modified=datetime.now())

    mark_as_cancelled.short_description = "Mark selected orders as cancelled"

    def mark_as_in_transit(self, request, queryset):
        queryset.update(order_status="TRAN", order_modified=datetime.now())

    mark_as_in_transit.short_description = "Mark selected orders as in transit"

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "category",
        "original_price",
        "discount_price",
        "weight_in_gms",
        "available",
    )
    list_filter = ("category", "available")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
    )
