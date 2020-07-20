from django.core.exceptions import ValidationError
from django.db import models


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
        item_list = [
            (i.item, i.quantity) for i in ItemInOrder.objects.filter(order=self)
        ]
        return item_list

    @property
    def total_tax(self):
        tax_rate = 0.06
        total_price = self.total_item_price
        return round(tax_rate * total_price, 2)

    @property
    def total_shipping(self):
        from shoppingcart.utilities import delivery_cost

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
        items_in_order_set = ItemInOrder.objects.filter(order=self)
        for item_in_order in items_in_order_set:
            price += item_in_order.item.actual_price * item_in_order.quantity
        return round(price, 2)

    @property
    def total_savings(self):
        saved = 0
        items_in_order_set = ItemInOrder.objects.filter(order=self)
        for item_in_order in items_in_order_set:
            saved += item_in_order.item.savings * item_in_order.quantity
        return saved

    @property
    def amount_payable(self):
        return round((self.total_item_price + self.total_tax + self.total_shipping), 2)

    def clean(self):
        if self.total_shipping is None:
            raise ValidationError("Undeliverable Shipping Address")

    def save(self, cart, *args, **kwargs):
        super().save(*args, **kwargs)
        for item, quantity in cart.items():
            ItemInOrder(item=item, order=self, quantity=quantity).save()

    def __str__(self):
        return f"Order {self.pk}"

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class ItemInOrder(models.Model):
    """docstring for ItemInOrder."""

    item = models.ForeignKey("Item", on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey("Order", on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Order {self.order.pk}: Item {self.item.pk}"

    class Meta:
        verbose_name = "Item In Order"
        verbose_name_plural = "Items In Order"
        unique_together = [["item", "order"]]
