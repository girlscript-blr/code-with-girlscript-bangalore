from datetime import datetime
#entry
print('Welcome to GadgetifyWithGSBlr\n')
#List to store items
items = [['Basshead earphones', 1200], ['Dell Keyboard', 1050], ['Bluetooth computer mouse', 600],['Hp charger', 2500], ['Hp monitor', 12000],['Dell monitor', 15000],['Hp Keyboard', 1850] ]
print('Items Available\n')
item_id = 1
print('Item_id Item_name\tItem_priceperunit\n')
#for loop to print item information
for item in items:
    print(str(item_id) + ") \t" +(item[0]) + " Rs: " + str(item[1]))
    item_id += 1
#user data entry
name = input('\nPlease enter your name: ')
phone_no = input('Please enter your phone number: ')
pay_method = input('Please select your payment method: Cash/Card/Online: ')
item_selected = int(input('Please enter the item_id of item you want to purchase: '))
quantity = int(input('Please enter the quantity of item you want to purchase: '))
#calculating cost of purchased product
amount = items[item_selected-1][1] * quantity
tax = (amount * 6) / 100
amt_with_tax = amount + tax

print('\nGenerating bill for your purchase\n')

print('Shop name: GadgetifyWithGSBlr')
print('Shop address: 311/5 Akshay nagar, Bangalore, Karnataka, India')
print('Shop contact number: +91 9988776655\n')
#Outputting the user data along with cost of purchased product
print('Customer Name: ' + name)
print('Customer phone number: ' + phone_no)
print('Item purchased by customer: ' + items[item_selected-1][0] + '  Quantity: ' + str(quantity) + '  Price per unit : ' + str(items[item_selected-1][1]))
print('Total amount to be paid (inclusive of all taxes): ' + str(amt_with_tax))
print('Payment method: ' + pay_method)
#Using datatime to output current data and time in the bill
now = datetime.now()
dt_str = now.strftime('%d/%m/%Y %H:%M:%S')
print('\nBilling date and time:', dt_str)
print('Thanks for visiting! Please come again')
