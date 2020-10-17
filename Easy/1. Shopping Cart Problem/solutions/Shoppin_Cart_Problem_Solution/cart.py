from datetime import datetime

print("Hola! We welcome you to GadgetifyWithGSBlr:)\n")
items=[['keyboard',1500],['mouse',800],['monitor',2500],['headphones',1600]]
print("The items available in the shop are")
print("Item_ID      Item_Name      Cost")
item_id=1
for item in items:
    print("{0}          {1}       {2}".format(item_id,item[0],item[1]))
    item_id+=1
print("\n")
name=input("Kindly enter your full name:")
phone_number=input("kindly enter your phone number:")
payment_method=input("Please enter your payment method:cash/card/online:")
item_selected=int(input("Kindly enter the item_id of item you want to shop:"))
quantity=int(input("please enter the quantity of item you want to buy:"))
print("\nHere is your BILL\n")

amount = items[item_selected-1][1] * quantity
tax = (amount * 6) / 100
total = amount + tax

print("Shop name: GadgetifyWithGSBlr")
print("Shop address: 311/5 Akshay nagar, Bangalore, Karnataka, India")
print("Shop contact number: +91 9988776655")
print("Customer Name: {0}".format(name))
print("Customer Phone Number: {0}".format(phone_number))
print("item bought: {0}     Quantity: {1}     Price: {2}".format(items[item_selected-1][0],quantity,items[item_selected-1][1]))
print("Total Tax: Rs {0}".format(tax))
print("Total amount to be paid(Inclusive of tax): Rs {0}".format(total))
print("Billing method used is: {0}".format(payment_method))
now = datetime.now()
date = now.strftime("%d/%m/%Y %H:%M:%S")
print("Billing date and time: {0}".format(date))
print("--------------------------THANK YOU!!!VISIT US AGAIN SOON------------------------")


