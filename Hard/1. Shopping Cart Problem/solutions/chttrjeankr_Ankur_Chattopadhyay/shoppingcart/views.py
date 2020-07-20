from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from shoppingcart.forms import OrderForm
from shoppingcart.models import Item, ItemInOrder, Order
from shoppingcart.utilities import shop_details

cart = dict()


def index(request):
    return render(request, "index.html")


@csrf_exempt
def add_to_cart(request):
    if request.method == "POST":
        print(request.POST)
        form_id = request.POST["id"]
        item_id = form_id.lstrip("quantity_")
        quantity = int(request.POST["quantity"])
        new_item = Item.objects.get(pk=item_id)
        if quantity == 0:
            if cart.get(new_item):
                del cart[new_item]
        else:
            cart[new_item] = quantity
        return JsonResponse({"item": new_item.name})


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


