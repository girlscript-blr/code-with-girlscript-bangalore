import tkinter as tk
from datetime import datetime

# define app
app = tk.Tk(screenName='GadgetifyWithGSBlr Shopping')
app.geometry('1920x1080')
app.title('GadgetifyWithGSBlr Shopping')
app.configure(background='gray')

# define products
product_dict = {'Redmi Note 9: Rs. 11999': 11999,
                'Mi Notebook 14: Rs. 54999': 54999,
                'Burning Chrome: Rs. 560': 560,
                'Snow Crash: Rs. 3790': 379,
                'HP X1000 Wired Mouse: Rs. 349': 349}
product_dict_keys = list(product_dict.keys())
product_dict_values = list(product_dict.values())


# get key if item is valid
def get_key(value):
    if value in product_dict_values:
        return product_dict_keys[product_dict_values.index(value)]


# generate bill
def gen_bill():
    _name = 'Customer Name: ' + name.get() + '\n'
    _phone = 'Customer Phone Number: ' + phone.get() + '\n'
    _payment_method = 'Payment Method: ' + payment_method.get() + '\n'
    _item_price = 'Item Price: ' + str(item.get()) + '\n'
    _item_name = "Item Name :- " + get_key(item.get()).split(":")[0] + "\n"
    _quantity = quantity.get()

    if _quantity == '' or int(_quantity) < 1:
        error = tk.Label(app, text="Bill couldn't be generated as quantity is invalid",
                         height=5, width=128, bg="#FF0000", fg="#FFFFFF")
        error.grid(row=8, column=0, columnspan=10)
        error.after(3000, lambda: error.destroy())
    else:
        # calculate tax
        tax = 0.06 * item.get() * int(_quantity)

        tax_charged = "Tax on the Item purchased: Rs. " + str(round(tax, 2)) + "\n"
        total_price = "Final Price of the product: Rs. " + str(round(1.06*tax/0.06, 2)) + "\n"

        with open(name.get().replace(' ', '_')+'.txt', "w") as f:
            f.write(datetime.now().strftime('\t\t%d %B %Y, %H:%M:%S') + '\n')
            f.write('\t\tGadgetifyWithGSBlr\n')
            f.write('\t\tAddress: 311/5 Akshay Nagar, Bangalore, Karnataka, India\n')
            f.write('\t\tContact No.: +91 9988776655\n')
            f.write(_name)
            f.write(_phone)
            f.write(_item_name)
            f.write(_item_price)
            f.write('Quantity: '+_quantity+'\n')
            f.write(tax_charged)
            f.write(total_price)
            f.write(_payment_method)
            f.close()

        temp = tk.Label(app, text="Bill generated Successfully!!!", height=5, width=128, bg="#2ECA12", fg="#DEF031")
        temp.grid(row=8, column=0, columnspan=10)
        temp.after(3000, lambda: temp.destroy())

        name.delete(0, tk.END)
        phone.delete(0, tk.END)
        quantity.delete(0, tk.END)
        r1.select()
        item.set(11999)


# banner
def make_banner():
    banner = tk.Label(app, text="GadgetifyWithGSBlr Shopping Mall", height=3, width=100, bg="#C39BD3", fg="#F2F4F4")
    banner.grid(row=0, column=0, columnspan=10)
    banner.config(font=("Verdana", 20))


# labels
def make_labels():
    name_label = tk.Label(app, text="Customer Name", height=2, width=24, bg="#C39BD3", fg="#F2F4F4")
    name_label.grid(row=1, column=0, pady=12)
    phone_label = tk.Label(app, text="Mobile No.", height=2, width=24, bg="#C39BD3", fg="#FFFFFF")
    phone_label.grid(row=2, column=0, pady=12)
    payment_method_label = tk.Label(app, text="Payment Method", height=2, width=24, bg="#C39BD3", fg="#F2F4F4")
    payment_method_label.grid(row=3, column=0, pady=12)
    item_label = tk.Label(app, text="Item Name", height=2, width=24, bg="#C39BD3", fg="#F2F4F4")
    item_label.grid(row=4, column=0, pady=12)
    quantity_label = tk.Label(app, text="Quantity", height=2, width=24, bg="#C39BD3", fg="#F2F4F4")
    quantity_label.grid(row=5, column=0, pady=12)


# entries
name = tk.Entry(width=32)
name.grid(row=1, column=1, pady=12, ipady=5)
phone = tk.Entry(width=32)
phone.grid(row=2, column=1, pady=12, ipady=5)
quantity = tk.Entry(width=32)
quantity.grid(row=5, column=1, pady=12, ipady=5)

payment_method = tk.StringVar()
r1 = tk.Radiobutton(app, text='Cash', value='Cash', variable=payment_method, width=24)
r1.grid(row=3, column=1, ipady=5)
r2 = tk.Radiobutton(app, text='Card', value='Card', variable=payment_method, width=24)
r2.grid(row=3, column=2, ipady=5)
r3 = tk.Radiobutton(app, text='Online Banking', value='Online Banking', variable=payment_method, width=24)
r3.grid(row=3, column=3, ipady=5)
r3.select()

item, c = tk.IntVar(app, 11999), 1
for key, val in product_dict.items():
    tk.Radiobutton(app, text=key, value=val, variable=item, width=24).grid(row=4, column=c, pady=7)
    c += 1

# buy
buy = tk.Button(app, text='Buy Now', width=28, command=gen_bill, bg='#FF8826', fg='#974EF9')
buy.grid(row=7, column=2, ipady=5, pady=10)

make_banner()
make_labels()

app.mainloop()
