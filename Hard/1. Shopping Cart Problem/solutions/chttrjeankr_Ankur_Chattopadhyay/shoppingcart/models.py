import json

from django.core.exceptions import ValidationError
from django.core.serializers import deserialize, serialize
from django.db import models

from shoppingcart.utilities import delivery_cost, order_directory


class Category(models.Model):
    """docstring for Category."""

    name = models.CharField(max_length=20)

    def __str__(self):
        return f"Category {self.pk}: {self.name}"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Item(models.Model):
    """docstring for Item."""

    name = models.CharField(max_length=20)
    category = models.ForeignKey("Category", on_delete=models.PROTECT)
    original_price = models.FloatField()
    discount_price = models.FloatField(null=True, blank=True)
    weight_in_gms = models.FloatField()
    available = models.BooleanField(default=True)

    @property
    def actual_price(self):
        return self.discount_price or self.original_price

    @property
    def savings(self):
        if self.discount_price:
            return self.original_price - self.discount_price
        else:
            return 0

    def __str__(self):
        return f"Item {self.pk}: {self.name}"

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"


class Order(models.Model):
    """docstring for Order."""

    PAYMENT_CHOICES = [
        ("NETB", "Net Banking"),
        ("COD", "Cash On Delivery"),
        ("CCARD", "Credit Card"),
        ("DCARD", "Debit Card"),
    ]
    DELIVERY_CHOICES = [
        ("TKW", "Takeaway"),
        ("HMD", "Home Delivery"),
    ]
    ORDER_STATUSES = [
        ("TRAN", "In Transit"),
        ("COMP", "Completed"),
        ("CANC", "Cancelled"),
    ]

    billing_date_time = models.DateTimeField(auto_now_add=True)
    order_modified = models.DateTimeField(auto_now=True)
    order_status = models.CharField(
        max_length=4, choices=ORDER_STATUSES, default="TRAN"
    )
    customer_name = models.CharField(max_length=40)
    customer_mobile_no = models.BigIntegerField()
    payment_method = models.CharField(max_length=5, choices=PAYMENT_CHOICES)
    delivery_option = models.CharField(max_length=3, choices=DELIVERY_CHOICES)
    distance_from_shop = models.IntegerField(blank=True, null=True, default=0)
    shipping_address = models.TextField(blank=True, null=True)

    def get_billed_items(self):
        item_list = self.get_items_from_json_cart()
        return item_list

    @property
    def total_tax(self):
        tax_rate = 0.06
        total_price = self.total_item_price
        return round(tax_rate * total_price, 2)

    @property
    def total_shipping(self):
        if self.delivery_option == "HMD":
            try:
                return delivery_cost[
                    filter(
                        lambda x: self.distance_from_shop in x, delivery_cost.keys()
                    ).__next__()
                ]
            except StopIteration:
                return None
        else:
            return 0

    @property
    def total_item_price(self):
        price = 0
        item_list = self.get_billed_items()
        for item, quantity in item_list:
            price += item.actual_price * quantity
        return round(price, 2)

    @property
    def total_savings(self):
        saved = 0
        item_list = self.get_billed_items()
        for item, quantity in item_list:
            saved += item.savings * quantity
        return saved

    @property
    def amount_payable(self):
        return round((self.total_item_price + self.total_tax + self.total_shipping), 2)

    def get_items_from_json_cart(self):
        with open(order_directory + f"order_{self.pk}.json") as f:
            cart_list = json.load(f)

        item_list = []
        for item in cart_list[1:]:
            quantity = item.pop("quantity")
            item_deserialized = list(deserialize("json", json.dumps([item])))[0]
            item_obj = item_deserialized.object
            item_list.append((item_obj, quantity))

        return item_list

    def save_cart(self, cart):
        cart_list = [{"order_id": self.pk}]
        for i, (item, quantity) in enumerate(cart.items()):
            ser_item = Item.objects.filter(pk=item.pk)
            store_cart = json.loads(serialize("json", ser_item))
            store_cart[0]["quantity"] = quantity
            cart_list.extend(store_cart)

        with open(order_directory + f"order_{self.pk}.json", "w") as f:
            json.dump(cart_list, f)

    def clean(self):
        if self.total_shipping is None:
            raise ValidationError("Undeliverable Shipping Address")

    def save(self, cart, *args, **kwargs):
        super().save(*args, **kwargs)
        self.save_cart(cart)

    def __str__(self):
        return f"Order {self.pk}"

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
