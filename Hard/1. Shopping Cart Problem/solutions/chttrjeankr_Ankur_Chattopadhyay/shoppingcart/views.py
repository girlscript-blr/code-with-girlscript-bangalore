from datetime import datetime

from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from django.urls import reverse

from shoppingcart.forms import CategoryForm, ItemForm, OrderForm
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


# ----------Order "R" (Vendor)----------


def show_all_orders(request):
    if request.method == "POST":
        new_status = request.POST.get("new_status")
        order_id = request.POST.get("order_id")
        if new_status and order_id:
            order = Order.objects.filter(pk=order_id).update(
                order_status=new_status, order_modified=datetime.now()
            )
        return redirect(reverse("all_orders"))
    if request.method == "GET":
        order_by = request.GET.get("order_by", "-billing_date_time")
        choices = {}
        filter_fields = []
        for field in Order._meta.fields:
            if field.choices:
                filter_fields.append(field.attname)
                choices[field.name] = field.choices

        params = {}
        for field_name in filter_fields:
            val = request.GET.get(field_name)
            if val:
                params[field_name] = val

        if any(params.values()):
            orders = Order.objects.filter(**params)
        else:
            orders = Order.objects.all()
        search = request.GET.get("q")
        if search:
            orders = orders.filter(pk=search)
        orders_sorted = orders.order_by(order_by)

        context = {
            "choices": choices,
            "orders": orders_sorted,
            "statuses": choices["order_status"],
        }
        return render(request, "vendor/all_orders.html", context)


# ----------Item "CRUD" (Vendor)----------


def create_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            messages.success(request, "Item Added")
            return redirect(reverse("all_items"))
        else:
            messages.error(request, "Item creation Skipped")
            # return redirect(reverse("create_item"))

    else:
        form = ItemForm()

    categories = Category.objects.all()
    return render(
        request,
        "vendor/create_item.html",
        context={"categories": categories, "form": form},
    )


def show_all_items(request):
    if request.method == "GET":
        order_by = request.GET.get("order_by", "-pk")
        category_id = request.GET.get("category_id")
        choices = {}
        filter_fields = []
        for field in Item._meta.fields:
            if field.choices:
                filter_fields.append(field.attname)
                choices[field.name] = field.choices
            if field.is_relation:
                filter_fields.append(field.attname)
                associated_model = field.related_model
                choices[field.attname] = [
                    (obj.pk, obj.name) for obj in associated_model.objects.all()
                ]
            if field.get_internal_type() == "BooleanField":
                filter_fields.append(field.attname)
                choices[field.attname] = [
                    (True, True),
                    (False, False),
                ]

        params = {}
        for field_name in filter_fields:
            val = request.GET.get(field_name)
            if val:
                params[field_name] = val

        if any(params.values()):
            items = Item.objects.filter(category__id=category_id, **params)
        elif category_id:
            items = Item.objects.filter(category__id=category_id)
        else:
            items = Item.objects.all()
        search = request.GET.get("q")
        if search:
            items = items.filter(name__contains=search)
        items_sorted = items.order_by(order_by)
        context = {
            "choices": choices,
            "items": items_sorted,
        }
        return render(request, "vendor/all_items.html", context)


def delete_item(request, item_id):
    deleted_item = Item.objects.filter(pk=item_id).delete()
    messages.info(request, f"Item {item_id} was deleted")
    return redirect(reverse("all_items"))


def edit_item(request, item_id):
    try:
        ins = Item.objects.get(pk=item_id)
    except ObjectDoesNotExist:
        messages.error(request, "Item doesn't exist")
        return redirect(reverse("all_items"))
    if request.method == "POST":
        form = ItemForm(request.POST, instance=ins)
        if form.is_valid():
            item = form.save()
            messages.success(request, "Item Edited")
            return redirect(reverse("all_items"))
        else:
            messages.error(request, "Item manipulation Skipped")
            # return redirect(reverse("edit_item"))

    else:
        form = ItemForm(instance=ins)

    categories = Category.objects.all()
    return render(
        request,
        "vendor/edit_item.html",
        context={"categories": categories, "form": form},
    )


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
