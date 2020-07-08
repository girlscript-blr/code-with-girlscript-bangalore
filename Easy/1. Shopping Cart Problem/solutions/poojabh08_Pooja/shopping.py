import time

def bill_generate():
    print('\n\nShop name: GadgetifyWithGSBlr')
    print('Shop address: 311/5 Akshay nagar, Bangalore, Karnataka, India')
    print('Shop contact no: +91 9988776655')
    print('Customer Name: {}'.format(name))
    print('Customer Phone no: {}'.format(phone_no))
    print('Item Purchased: {}  \nQuantity: {}  \nPrice: {}'.format(item_name,item_qty,item_cost))
    tax = (item_cost*item_qty)*(6/100)
    total = (item_cost*item_qty) + tax
    print('Tax: {}'.format(tax))
    print('Total: {}'.format(total))
    print('Payment method: {}'.format(payment))
    ltime = time.asctime(time.localtime())
    print('Billing Date and Time: {}'.format(ltime))

Item = {'Digital Hand Band': 1800 ,'Basshead earphones': 1200, 'Bluetooth computer mouse': 600, 'A Mini Bluetooth Speaker': 2500, 'Portable Wi-Fi': 1950}

name = input("Enter your name: ")
phone_no = input("Enter your Phone Number: ")
print("Choose your payment methods as follows\n1. Cash \n2. Card \n3. Online ")
pay = int(input())
p = ['Cash','Card','Online']
payment = p[pay-1]
print("\nPick your Items here ")
i=1
for key in list(Item.keys()):
    print("{}. {}".format(i,key))
    i+=1
item_index = int(input())
item_qty = int(input("Enter quantity: "))
item_name = list(Item.keys())[item_index - 1]
item_cost = list(Item.values())[item_index - 1]
bill_generate()


    


