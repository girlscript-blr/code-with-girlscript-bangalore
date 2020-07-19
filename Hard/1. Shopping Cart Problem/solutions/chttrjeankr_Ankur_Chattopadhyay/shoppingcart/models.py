from django.db import models


class Category(models.Model):
    """docstring for Category."""

    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.pk}: {self.name}"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Item(models.Model):
    """docstring for Item."""

    name = models.CharField(max_length=20)
    category_id = models.ForeignKey("Category", on_delete=models.PROTECT)
    original_price = models.FloatField()
    discount_price = models.FloatField(null=True, blank=True)
    weight_in_gms = models.FloatField()

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
        return f"{self.pk}: {self.name}"

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
    distance_from_shop = models.IntegerField()
    shipping_address = models.TextField()

    def get_billed_items(self):
        pass

    def calculate_total_tax(self):
        pass

    def calculate_total_shipping(self):
        pass

    def calculate_total_price(self):
        pass

    def calculate_total_saved(self):
        pass

    def check_order_status(self):
        return self.order_status

    def __str__(self):
        return f"{self.pk}: {self.customer_name}"

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class ItemInOrder(models.Model):
    """docstring for ItemInOrder."""

    item = models.ForeignKey("Item", on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey("Order", on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = "Item In Order"
        verbose_name_plural = "Items In Order"
        unique_together = [["item", "order"]]
