import datetime

from flask import Flask, render_template, request

from utilities import shop_details, shopping_list

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/shopping_list")
def display_shopping_list():
    return render_template("shopping_list.html", shopping_list=shopping_list)


@app.route("/order", methods=["GET", "POST"])
def create_order():
    if request.method == "GET":
        return render_template("create_order.html", shopping_list=shopping_list)
    if request.method == "POST":
        bill = get_bill(request)
        return render_template("display_bill.html", bill=bill)


def get_bill(request):
    customer_name = request.form.get("name")
    customer_phone_no = request.form.get("phoneNumber")
    payment_method = request.form.get("paymentMethod")
    selected_item = request.form.get("selectedItem")
    quantity = int(request.form.get("quantity"))
    item_cost = shopping_list[selected_item]
    price = item_cost * quantity
    tax_applied = 0.06 * price
    total_price = price + tax_applied
    bill = {
        **shop_details,
        "customerName": customer_name,
        "customerPhoneNumber": customer_phone_no,
        "selectedItem": selected_item,
        "quantity": quantity,
        "itemCost": item_cost,
        "totalTax": tax_applied,
        "totalPrice": total_price,
        "paymentMethod": payment_method,
        "billingDateTime": datetime.datetime.now(),
    }
    return bill


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
