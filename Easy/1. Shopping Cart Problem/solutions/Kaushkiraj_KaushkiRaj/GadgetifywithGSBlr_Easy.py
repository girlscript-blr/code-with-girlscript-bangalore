from datetime import datetime

text = '  Welcome to GadgetifyWithGSBlr  '  
welcome_text = text.center(61, '*')
print(welcome_text,'\n')

print('List of items available in shop : \n')

class ItemList:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def info(self):
        return self.name + ': Rs.' + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count
        total_price_gst = total_price+(total_price * 0.06)
        return round(total_price), round(total_price_gst)

Item1 = ItemList('Boat Bluetooth Headset', 1999)
Item2 = ItemList('Sony Wired Headset', 2490)
Item3 = ItemList('Mi Smart Band 4', 2299)
Item4 = ItemList('Honor Band 5i', 1799)
Item5 = ItemList('Zebronics Wired Keyboard', 349)
Item6 = ItemList('HP 100 Wired USB Keyboard', 649)

items = [Item1,Item2,Item3,Item4,Item5,Item6]

index = 1
for item in items:
    print(str(index) + '. ' + item.info())
    index += 1

print('\n--------------------------------------------')

name = input("Enter your name: ")
phone_no = input("Enter your phone number: ")
pay_method = input("Select the payment method: Cash/Card/Online: ")
item_order = int(input("Enter the item number you want to purchase: "))
quantity = int(input("Enter the quantity of item you want to purchase: "))

selected_item = items[item_order-1]
amount, amount_gst = selected_item.get_total_price(quantity)

print('\n')
print('Generating bill.............')
print('\n')

print("\nShop name: GadgetifyWithGSBlr")
print("Shop address: 311/5 Akshay nagar, Bangalore, Karnataka, India")
print("Shop contact number: +91 9988776655\n")

print('Customer Name: ' + name)
print('Customer phone number: ' + phone_no)
print('Item purchased: ' + items[item_order-1].name + '  Quantity: ' + str(quantity) + '  Price/unit : ' + str(items[item_order-1].price))
print('Total amount to be paid: ' + str(amount_gst))
print('Payment method choosen: ' + pay_method)

print('\n')
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Billing date and time =", dt_string)

print('Thank you for visiting us!')





