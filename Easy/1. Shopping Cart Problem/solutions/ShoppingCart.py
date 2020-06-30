
from datetime import datetime

print('Welcome to GadgetifyWithGSBlr\n\n')

items_in_shop = [['Basshead earphones', 1200], ['Dell Keyboard', 850], ['Bluetooth computer mouse', 600], ['Dell monitor', 12000], ['Dell charger', 2500], ['Asus gaming mouse', 820], ['Mobile cover', 200]]


print("\nItems available in Shop:\n")
item_id = 1
print("Item_id   Item_name    Item_price/unit")
print('---------------------------------------------\n')
for item in items_in_shop:
    print(str(item_id) + ". " +(item[0]) + " Rs. " + str(item[1]))
    print('---------------------------')
    item_id += 1


name = input("Please enter your name: ")
phone_no = input("Please enter your phone number: ")
pay_method = input("Please select your payment method: Cash/Card/Online: ")
item_choosen = int(input("Please enter the item_id of item you want to purchase: "))
quant = int(input("Please enter the quantity of item you want to purchase: "))

amount = items_in_shop[item_choosen-1][1] * quant
tax = (amount * 6) / 100
amount_with_tax = amount + tax

print('\n\n')
print('Generating bill.............')
print('\n\n')

print("\nShop name: GadgetifyWithGSBlr")
print("Shop address: 311/5 Akshay nagar, Bangalore, Karnataka, India")
print("Shop contact number: +91 9988776655\n")

print('Customer Name: ' + name)
print('Customer phone number: ' + phone_no)
print('Item purchased: ' + items_in_shop[item_choosen-1][0] + '  Quantity: ' + str(quant) + '  Price/unit : ' + str(items_in_shop[item_choosen-1][1]))
print('Total amount to be paid: ' + str(amount_with_tax))
print('Payment method choosen: ' + pay_method)

print('\n')
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Billing date and time =", dt_string)

print('Thank you for visiting us!')