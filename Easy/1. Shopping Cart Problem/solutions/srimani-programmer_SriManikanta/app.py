__author__  = "Sri Manikanta Palakollu"

from datetime import datetime

class ShoppingApp:

    def __init__(self, customerName, customerPhoneNumber, paymentMethod):
        self.shopName = "GadgetifyWithGSBlr"
        self.shopAddress = "311/5 Akshay nagar, Bangalore, Karnataka, India"
        self.shopPhoneNumber = "+91 9988776655"
        self.itemDetails = {
            "Apple MacBook Air (13-inch, 8GB RAM, 128GB Storage, 1.8GHz Intel Core i5) - Silver" : 74763,
            "Apple MacBook Pro (13-inch, 8GB RAM, 256GB SSD, 1.4GHz Quad-core 8th-Generation" : 127999,
            "Apple MacBook Pro (16-inch, 16GB RAM, 512GB Storage, 2.6GHz 9th Gen Intel Core i7) - Space Grey" : 199900,
            "OnePlus 8 5G (Glacial Green 6GB RAM+128GB Storage" : 41999,
            "Oppo Reno3 Pro (Midnight Black, 8GB RAM, 128GB Storage)" : 29990,
            "Oppo F15 (Unicorn White, 8GB RAM, 128GB Storage)" : 18990,
            "Samsung Galaxy Note10 Lite (Aura Black, 8GB RAM, 128GB Storage)" : 39999
        }
        self.customerName = customerName
        self.customerPhoneNumber = customerPhoneNumber
        self.paymentMethod = paymentMethod
        self.paymentModes = {"cash": "cash", "card": "card", "online": "online"}
        self.itemsList = list(self.itemDetails.keys())
        self.itemsPrice = list(self.itemDetails.values())
        self.cartItems = {}
        self.totalTax = 0.0
        self.totalAmount = 0.0

    def itemSelection(self):
        print("Enter your item selection from the available List.! Please enter \"q\" to quit from the list")
        print('\n')
        itemNumberCount = 1
        print("Item Number \t Item Name \t\t\t\t\t\t\t Item Price")

        for item, price in self.itemDetails.items():
            print("{} \t\t {} : Rs. {}".format(itemNumberCount, item, price))
            itemNumberCount += 1

        print("\n")

        itemNumber = 0
        itemQuantity = 0

        while True:
            itemNumber = int(input("Enter your Item number to select the Item of your choice: "))

            if(itemNumber > 7 or itemNumber < 1):
                print("Please Enter the valid Item")
                continue
            else:
                break
        
        while True:
            itemQuantity = int(input("Enter your item Quantity of your choice: "))
            if(itemQuantity <= 0):
                print("Please Enter a valid Item Quantity...!")
                continue
            else:
                break

        self.cartItems[self.itemsList[itemNumber - 1]] = itemQuantity


    def calculateAmount(self):
        for item, quantity in self.cartItems.items():
            if(item in self.itemsList):
                self.totalAmount += (self.itemsPrice[self.itemsList.index(item)] * quantity)
        
        self.totalTax =  round((self.totalAmount * 0.06), 3)
        self.totalAmount = self.totalAmount + self.totalTax


name = input("Enter Customer name: ")
phoneNumber = input("Enter Customer phone number: ")
paymentMethod = input("Enter Customer payment Method [Cash/Card/Online]: ")
app = ShoppingApp(name, phoneNumber, paymentMethod)
# Item Selection By the Customer.
app.itemSelection()
# Total Purchased Amount Calculation
app.calculateAmount()
print("################################### Billing Details ###################################")
print("\t\tShop Name: {}".format(app.shopName))
print("\t\tShop Address: {}".format(app.shopAddress))
print("\t\tShop Contact no: {}".format(app.shopPhoneNumber))
print("\n")
print("\t\tCustomer Name: {}".format(app.customerName))
print("\t\tCustomer Phone Number: {}".format(app.customerPhoneNumber))

for item, quantity in app.cartItems.items():
    print("\t\tItem Bought : {}".format(item))
    print("\t\tItem Quantity: {}".format(quantity))
    print("\t\tItem Price: {}".format(app.itemsPrice[app.itemsList.index(item)]))
print("\t\tTotal Tax: {}".format(app.totalTax))
print("\t\tTotal Amount to be paid: {}".format(app.totalAmount))
print("\t\tPayment Used: {}".format(app.paymentModes.get(app.paymentMethod.lower(), "Payment is Not Selected Properly.")))
print("\t\tBilling Date and Time: {}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))