from datetime import datetime

print('Welcome to GadgetifyWithGSBlr\n')

items_in_shop = [['Basshead earphones', 1200], ['Dell Keyboard', 850], ['Bluetooth computer mouse', 600], ['Dell monitor', 12000], ['Dell charger', 2500], ['Asus gaming mouse', 820], ['Mobile cover', 200]]
options=['cash','card','online']

print("\nItems available in Shop:\n")
item_id = 1
print("Item_id   Item_name    Item_price/unit")
print('---------------------------------------------\n')
for item in items_in_shop:
    print(str(item_id) + ". " +(item[0]) + " Rs. " + str(item[1]))
    print('---------------------------')
    item_id += 1


name = input("Enter your name: ")
phone = input("Enter your phone number: ")
if phone.isdigit():
    phone_no=phone      
else :
    phone= input("Renter your phone number: ")

for i in range(len(options)):
    print(str(i+1) + ":", options[i])
pay_method= input("Enter a number: ")
list1=[1,2,3]
if pay_method.isdigit():
               if pay_method in list1:
                   pay_method = options[pay_method-1] 
else:
      pay_method= input(" Renter a number: ")
item_choosen = int(input("Enter the item_id of item you want to purchase: "))
quant = int(input("Enter the quantity of item you want to purchase: "))

amount = items_in_shop[item_choosen-1][1] * quant
tax = (amount * 6) / 100
amount_with_tax = amount + tax

print('\n\n')
print(' Please Wait Generating bill.............')
print('\n\n')

print("\nShop name: GadgetifyWithGSBlr")
print("Shop address: 311/5 Akshay nagar, Bangalore, Karnataka, India")
print("Shop contact number: +91 9988776655\n")

print('Customer Name: ' + name)
print('Customer phone number: ' + phone)
print ('the tax percentage is 6%')

print('Item purchased: ' + items_in_shop[item_choosen-1][0] + '  Quantity: ' + str(quant) + '  Price/unit : ' + str(items_in_shop[item_choosen-1][1]))
print('tax amount:',tax)
print('Total amount to be paid: ' + str(amount_with_tax))
print('Payment method choosen: ' +str(pay_method))

print('\n')
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Billing date and time =", dt_string)

print('Thank you for visiting us!Come Back Soon!!') 