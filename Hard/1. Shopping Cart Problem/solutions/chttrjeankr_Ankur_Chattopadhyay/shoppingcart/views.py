from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from shoppingcart.forms import OrderForm
from shoppingcart.models import Category, Item, Order
from shoppingcart.utilities import shop_details

cart = dict()


def index(request):
    return render(request, "index.html")


def clear_cart(request):
    if cart:
        cart.clear()
        messages.info(request, "Cart cleared! Add more items")
        return redirect(reverse("categories"))
    else:
        messages.error(request, "Cart is already empty")
        return redirect(reverse("create_order"))


def display_categories(request):
    categories = Category.objects.all()
    return render(request, "categories.html", context={"categories": categories},)


def display_shopping_list(request, category):
    if request.method == "POST":
        item_id = request.POST.get("item_pk")
        quantity = int(request.POST.get("quantity"))
        new_item = Item.objects.get(pk=item_id)
        if quantity == 0:
            if cart.get(new_item):
                del cart[new_item]
        else:
            cart[new_item] = quantity
        messages.success(request, f"Item {new_item.name} updated")
        return redirect("display_shopping_list", category=category)
    shopping_list = Item.objects.filter(category=category)
    return render(
        request,
        "shopping_list.html",
        context={"shopping_list": shopping_list, "cart": cart},
    )


def vendor(request):
    messages.success(request, "Vendor Logged In")
    return render(request, "vendor/vendor_main.html")

def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if cart:
            if form.is_valid():
                order = form.save(commit=False)
                order.order_status = "TRAN"
                order.save(cart)
                cart.clear()
                return render(
                    request,
                    "display_bill.html",
                    context={"order": order, **shop_details},
                )
            else:
                messages.error(request, "Form Validation Error")
                # return redirect(reverse("create_order"))
        else:
            messages.error(request, "No items in cart to be billed")
            return redirect(reverse("create_order"))

    else:
        form = OrderForm()

    return render(
        request, "create_order.html", context={"cart": dict(cart), "form": form},
    )


def get_order_status(request):
    if request.method == "GET":
        return render(request, "order_status.html")
    if request.method == "POST":
        order_id = request.POST.get("order_id")
        phone_number = request.POST.get("phone_number")
        try:
            queried_order = Order.objects.get(
                pk=order_id, customer_mobile_no=phone_number
            )
            return render(
                request,
                "display_bill.html",
                context={"order": queried_order, **shop_details, "status_check": True},
            )
        except ObjectDoesNotExist:
            messages.error(request, "Order Not Found")
            return redirect(reverse("order_status"))
