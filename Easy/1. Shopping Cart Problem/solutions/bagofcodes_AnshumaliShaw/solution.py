import tkinter as tk
from tkinter import *
from datetime import datetime

screen = tk.Tk(screenName="GadgetifyWithGSBlr Shopping")
screen.geometry("1600x640")
screen.title("GadgetifyWithGSBlr Shopping")
screen.configure(bg="grey")

product_list = {"JBL Basshead earphones: Rs. 1200" : 1200, "Bluetooth computer mouse: Rs. 600": 600, "HP Mouse: Rs. 200":200, 
                "Realme 5 pro: Rs. 15000": 15000, "Sandisk Pendrive: Rs. 850": 850}


#getting the item purchased

def get_key(val):
    for key, value in product_list.items():
        if val == value:
            return key

#creating the function "gen_bill" that generates the bill and creates a textfile of the same

def gen_bill():
    timestamp= datetime.now().strftime("                                            %d %B %Y, %H:%M:%S                                               ") + "\n"
    shop_name= "                                          Shop name: GadgetifyWithGSBlr                                                            " + "\n"
    shop_address="                        shop address: 311/5 Akshay nagar, Bangalore, Karnataka, India                                            " + "\n"
    shop_contact= "                                      Shop contact no: +91 9988776655                                                           " + "\n\n\n"
    
    prod_pur=prod_select.get()
    name_bill="Name of the customer :- " + name_entry.get() + "\n"
    contact="Mobile of the customer :- " + phone_entry.get() + "\n"
    item_purchased = "Item Purchased by the customer :- " + get_key(prod_pur).split(":")[0] + "\n"
    item_price = "Price of the Item purchased:- Rs. " + str(prod_pur) + "\n"
    quan="Quantity of the item purchased:- " + quantity_entry.get() + "\n"
    pay_mode = "Mode of Payment:- " + mop_select.get() + "\n"


    if(name_entry.get() == "" or phone_entry.get() == "" or quantity_entry.get() == ""):
        l2=Label(screen, text="Bill couldn't be generated due to one or more fields missing", height = 2, width= 100, bg="#EA2511" , fg= "#050506")
        l2.grid(row = 8, column= 0, columnspan=10)
        l2.after(3000, lambda: l2.destroy())

    else:
        #calculation of tax
        taxable_price =prod_pur* int(quantity_entry.get())
        tax = 0.06* taxable_price

        tax_charged= "Tax on the Item purchased:- Rs. " + str(tax) + "\n"
        total_price= "Final Price of the product:- Rs. " + str(taxable_price + tax) + "\n"

        file=open(str(name_entry.get()).split(" ")[0], "w")
        file.write(timestamp)
        file.write(shop_name)
        file.write(shop_address)
        file.write(shop_contact)
        file.write(name_bill)
        file.write(contact)
        file.write(item_purchased)
        file.write(item_price)
        file.write(quan)
        file.write(tax_charged)
        file.write(total_price)
        file.write(pay_mode)
        file.close()
        l1=Label(screen, text="Bill generated Successfully....!!!", height = 2, width= 100, bg="#2ECA12" , fg= "#DEF031")
        l1.grid(row = 8, column= 0, columnspan=10)
        l1.after(3000, lambda: l1.destroy())
    
    #clearing fields
    name_entry.delete(0,END)
    phone_entry.delete(0,END)
    quantity_entry.delete(0,END)
    r1_mop.select()
    prod_select.set(1200)
    
    

#create banner
banner = Label(screen, text= "GadgetifyWithGSBlr Shopping Mall", height = 3, width= 100, bg="#1282B6", fg= "#FFFFFF")
banner.grid(row=0, column = 0, columnspan=10)
banner.config(font=("Courier", 20))

#create fields labels

name =  Label(screen, text= "Name of the Customer", height = 2, width = 30, bg="#1282B6", fg= "#FFFFFF")
phone =  Label(screen, text= "Mobile No.", height = 2, width = 30, bg="#1282B6", fg= "#FFFFFF")
mode_of_pay =  Label(screen, text= "Payment Method", height = 2, width = 30, bg="#1282B6", fg= "#FFFFFF")
item =  Label(screen, text= "Item You want to Buy", height = 2, width = 30, bg="#1282B6", fg= "#FFFFFF")
quantity =  Label(screen, text= "Quantity", height = 2, width = 30, bg="#1282B6", fg= "#FFFFFF")

#placing labels on screen

name.grid(row = 1, column= 0, pady = 10)
phone.grid(row = 2, column= 0, pady = 10)
mode_of_pay.grid(row = 3, column= 0, pady = 10)
item.grid(row = 4, column= 0, pady = 10)
quantity.grid(row = 5, column= 0, pady = 10)

#creating entry box, radio button

name_entry = Entry(width= 40)
phone_entry = Entry(width= 40)
quantity_entry = Entry(width= 40)

mop_select = tk.StringVar()
r1_mop = Radiobutton(screen, text="Online Banking", value="Online Banking", width= 30, variable = mop_select)
r2_mop = Radiobutton(screen, text="Cash", value="Cash", width= 30, variable = mop_select)
r3_mop = Radiobutton(screen, text="Card", value="Card", width= 30, variable = mop_select)
r1_mop.select()

#placing entry box, radio button on screen

name_entry.grid(row = 1, column = 1, pady=10, ipady=6)
phone_entry.grid(row = 2, column = 1, pady=10, ipady=6)
quantity_entry.grid(row = 5, column = 1, pady=10, ipady=6)

r1_mop.grid(row = 3, column = 1, ipady=6)
r2_mop.grid(row = 3, column = 2, ipady=6)
r3_mop.grid(row = 3, column = 3, ipady=6)

#creating radio buttons for products list

prod_select= tk.IntVar(screen,1200)
count=1
for (k,v) in product_list.items():
    Radiobutton(screen, text = k, variable = prod_select, value = v, width =28).grid(row = 4, column = count, ipady= 6)
    count+=1

#creating BuyNow Button and placing that to screen

buy_now = Button(screen, text="Buy Now", command = gen_bill, width= 40, bg="#1282B6", fg= "#FFFFFF")
buy_now.grid(row =7, column = 2, ipady=6, pady=10)

screen.mainloop()