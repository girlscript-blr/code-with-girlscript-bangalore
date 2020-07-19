from django.core.exceptions import ValidationError
from django.forms import ModelForm

from shoppingcart.models import Order


class OrderForm(ModelForm):
    def clean(self):
        cleaned_data = super(OrderForm, self).clean()
        delivery_option = cleaned_data.get("delivery_option")
        distance_from_shop = cleaned_data.get("distance_from_shop")
        shipping_address = cleaned_data.get("shipping_address")

        print(f"{delivery_option}, {distance_from_shop}, {shipping_address}")

        if delivery_option == "HMD":
            if not (distance_from_shop and shipping_address):
                raise ValidationError("Wrong delivery option")

    class Meta:
        model = Order
        fields = [
            "customer_name",
            "customer_mobile_no",
            "payment_method",
            "delivery_option",
            "distance_from_shop",
            "shipping_address",
        ]
