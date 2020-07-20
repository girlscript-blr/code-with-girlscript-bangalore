from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from collections import defaultdict, namedtuple
from shoppingcart.utilities import shopping_list, shop_details, delivery_cost
import datetime

# Create your views here.

cart = defaultdict(int)
Item = namedtuple(
    "Item", ["item_name", "final_price_per_item", "amount_saved_per_item"]
)


def index(request):
    return render(request, "index.html")


@csrf_exempt
def add_to_cart(request):
    if request.method == "POST":
        print(request.POST)
        form_id = request.POST["id"]
        item_name = form_id.lstrip("quantity_")
        quantity = int(request.POST["quantity"])

        final_price_per_item = shopping_list[item_name].get(
            "discount_price", shopping_list[item_name]["original_price"]
        )
        try:
            amount_saved_per_item = (
                shopping_list[item_name]["original_price"]
                - shopping_list[item_name]["discount_price"]
            )
        except KeyError:
            amount_saved_per_item = 0
        item_tuple = Item(item_name, final_price_per_item, amount_saved_per_item)

        cart[item_tuple] += quantity
        print(cart)
        return JsonResponse({"item": item_name})


def clear_cart(request):
    if cart:
        cart.clear()
        messages.info(request, "Cart cleared! Add more items")
        return redirect(reverse("display_shopping_list"))
    else:
        messages.error(request, "Cart is already empty")
        return redirect(reverse("create_order"))


def display_shopping_list(request):
    shopping_list = Item.objects.all()
    return render(
        request,
        "shopping_list.html",
        context={"shopping_list": shopping_list, "cart": cart},
    )


def create_order(request):
    if request.method == "GET":
        return render(request, "create_order.html", context={"cart": dict(cart)})
    if request.method == "POST":
        if cart:
            bill = get_bill(request)
            if bill is None:
                return redirect(reverse("create_order"))
            else:
                cart.clear()
                return render(request, "display_bill.html", context={"bill": bill})
        else:
            messages.error(request, "No items in cart to be billed")
            return redirect(reverse("create_order"))


def get_delivery_cost(dist):
    try:
        return delivery_cost[
            filter(lambda x: dist in x, delivery_cost.keys()).__next__()
        ]
    except StopIteration:
        return None


def get_bill(request):
    customer_name = request.POST.get("name")
    customer_phone_no = request.POST.get("phoneNumber")
    payment_method = request.POST.get("paymentMethod")
    delivery_method = request.POST.get("delivery")

    delivery_cost = 0
    shipping_address = ""
    if delivery_method == "homedel":
        dist_in_kms = int(request.POST.get("distKMs"))
        shipping_address = request.POST.get("shippingAddress")
        delivery_cost = get_delivery_cost(dist_in_kms)
        if delivery_cost is None:
            messages.warning(request, "Undeliverable Shipping Address")
            return None
    price = 0
    saved = 0
    for item_tuple, quantity in cart.items():
        price += item_tuple.final_price_per_item * quantity
        saved += item_tuple.amount_saved_per_item * quantity

    tax_applied = round(0.06 * price, 2)
    total_price = round(price + tax_applied + delivery_cost, 2)
    bill = {
        **shop_details,
        "customerName": customer_name,
        "customerPhoneNumber": customer_phone_no,
        "cart": dict(cart.copy()),
        "totalTax": tax_applied,
        "deliveryMethod": delivery_method,
        "deliveryCost": delivery_cost,
        "totalPrice": total_price,
        "totalSavings": saved,
        "paymentMethod": payment_method,
        "shippingAddress": shipping_address,
        "billingDateTime": datetime.datetime.now(),
    }
    return bill
