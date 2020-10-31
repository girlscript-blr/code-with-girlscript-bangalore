import datetime
import os
from collections import defaultdict, namedtuple

from flask import (
    Flask,
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    url_for,
)

from utilities import delivery_cost, shop_details, shopping_list

app = Flask(__name__)
app.secret_key = os.urandom(12)

cart = defaultdict(int)
Item = namedtuple(
    "Item", ["item_name", "final_price_per_item", "amount_saved_per_item"]
)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    form_id = request.form["id"]
    item_name = form_id.lstrip("quantity_")
    quantity = int(request.form["quantity"])

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
    return jsonify({"item": item_name})


@app.route("/clear_cart")
def clear_cart():
    if cart:
        cart.clear()
        flash("Cart cleared! Add more items")
        return redirect(url_for("display_shopping_list"))
    else:
        flash("Cart is already empty")
        return redirect(url_for("create_order"))


@app.route("/shopping_list")
def display_shopping_list():
    return render_template("shopping_list.html", shopping_list=shopping_list)


@app.route("/order", methods=["GET", "POST"])
def create_order():
    if request.method == "GET":
        return render_template("create_order.html", cart=cart)
    if request.method == "POST":
        if cart:
            bill = get_bill(request)
            if bill is None:
                flash("Undeliverable Shipping Address")
                return redirect(url_for("create_order"))
            else:
                cart.clear()
                return render_template("display_bill.html", bill=bill)
        else:
            flash("No items in cart to be billed")
            return redirect(url_for("create_order"))


def get_delivery_cost(dist):
    try:
        return delivery_cost[
            filter(lambda x: dist in x, delivery_cost.keys()).__next__()
        ]
    except StopIteration:
        return None


def get_bill(request):
    customer_name = request.form.get("name")
    customer_phone_no = request.form.get("phoneNumber")
    payment_method = request.form.get("paymentMethod")
    delivery_method = request.form.get("delivery")

    delivery_cost = 0
    shipping_address = ""
    if delivery_method == "homedel":
        dist_in_kms = int(request.form.get("distKMs"))
        shipping_address = request.form.get("shippingAddress")
        delivery_cost = get_delivery_cost(dist_in_kms)
        if delivery_cost is None:
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
        "cart": cart.copy(),
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
