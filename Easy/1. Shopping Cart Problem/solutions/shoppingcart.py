products = [("Basshead earphones",1200),
                ("Bluetooth mouse",600)
]

def show_products():
    print("Press the corresponding number for the product")
    i=1
    print("{}|{}|{}".format("Sr.no".ljust(20),"Item".ljust(30),"Price".ljust(30)))
    for prod in products:
        print("{}|{}|{}".format(str(i).ljust(20),prod[0].ljust(30),str(prod[1]).ljust(30)))
        i=i+1

def show_cost(prod_num,qty):
    tax_rate = 6; 
    cost = products[prod_num-1][1]*qty*(1+(tax_rate/100)); 
    print("Your total cost for {} items of product {} with tax {} % is Rs.{}".format(qty,products[prod_num][0], tax_rate, cost))

def start():
    show_products()
    prod_num = input("Enter product nos. ")
    qty = input("Enter qty. ")
    show_cost(int(prod_num),int(qty))




