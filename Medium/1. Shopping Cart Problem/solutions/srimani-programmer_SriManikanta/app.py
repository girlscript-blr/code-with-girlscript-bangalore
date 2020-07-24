__author__  = "Sri Manikanta Palakollu"

from datetime import datetime

class ShoppingApp:

    def __init__(self, customerName, customerPhoneNumber, paymentMethod):
        self.shopName = "GadgetifyWithGSBlr"
        self.shopAddress = "311/5 Akshay nagar, Bangalore, Karnataka, India"
        self.shopPhoneNumber = "+91 9988776655"

        self.itemDetails = {
            "Boat Headset" : [1200, 899, '100g'],
            "Oppo A5 2020" : [14990, 10990, '195g'],
            "Oppo A12 " : [10990, 9990, '215g'],
            "OnePlus 8" : [41999, 41000, '190g'],
            "Oppo Reno3" : [29990, 25590, '210g'],
            "Oppo F15" : [18990, 17990, '200g'],
            "Vivo U10" : [10990, "No Discount Available", '191g']
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
        self.totalAmountSaved = 0.0
        self.deliveryAmount = 0
        self.customerShippingAddress = None

    def itemSelection(self):
        
        itemId = 1
        print("Item Id \t Item Name \t\t\t Item Price \t\t\t Discount Price")
        for item, price in self.itemDetails.items():
            if(isinstance(price[1], int)): 
                print("{} \t\t {} \t\t\t  Rs. {} \t\t\t Rs. {} ".format(itemId, item, price[0], price[1]))
            else:
                print("{} \t\t {} \t\t\t  Rs. {} \t\t\t {} ".format(itemId, item, price[0], price[1]))

            itemId += 1
        
        selection = 0
        try:
            productSelection = int(input("Enter the number of products you want to buy from the above Items List: "))
        except ValueError:
            print("Please Enter the Integer Value.")
            exit(0)
        while productSelection != selection:
            # Item Id Selection from the list
            try:
                requestItemId = int(input("Enter the Item Id to Select the Product: "))
            except ValueError:
                print("Please Enter the Integer Value.")
                exit(0)

            if(requestItemId > 7 or requestItemId <= 0):
                print('Please Enter the valid Item Id. from the List')
                continue
            # Item Quantity Selection
            try:
                requestQuantity = int(input("Enter the Product Quantity for the Selected Item: "))
            except ValueError:
                print("Please Enter the Integer Value.")
                exit(0)

            if(requestQuantity <= 0):
                print("Please Enter the Valid Quantity number that should be greater than 0.")

            selection += 1
            
            self.cartItems[self.itemsList[requestItemId - 1]] = requestQuantity
            #print(self.cartItems)

    def calculateAmount(self):
        for item, quantity in self.cartItems.items():
            if(item in self.itemsList):
                priceDetails = self.itemsPrice[self.itemsList.index(item)]
                if(isinstance(priceDetails[1],str)):
                    self.totalAmount += (priceDetails[0] * quantity)
                else:
                    self.totalAmount += (priceDetails[1] * quantity)
                    self.totalAmountSaved += ((priceDetails[0] - priceDetails[1]) * quantity )

                # self.totalAmount += (self.itemsPrice[self.itemsList.index(item)] * quantity)
        
        self.totalTax =  round((self.totalAmount * 0.06), 3)
        self.totalAmount = self.totalAmount + self.totalTax
        # print(self.totalTax)
        # print(self.totalAmount)

    # Delivery Option Selections
    def delivery(self, type):
        try:
            distance = float(input("Enter your home distance in kilometers from the Store: "))
            if(distance > 50):
                print("Delivery is unavailable for More than 50 KMS.")
                exit(0)
            elif(distance > 20 and distance <= 50):
                self.totalAmount += 60
                self.deliveryAmount = 60
            elif(distance > 5 and distance <= 20):
                self.totalAmount += 30
                self.deliveryAmount = 30
            elif(distance > 0.1 and distance <= 5):
                pass
            else:
                print("Please Enter the distance greater than 0 KMS")
        except ValueError:
            print("Please Enter a Valid number for distance.")
            exit(0)
    


name = input("Enter Customer name: ")
phoneNumber = input("Enter Customer phone number: ")

# Payment Selection
paymentMethod = ['cash', 'card', 'online']
method = None

while True:
    try:
        method = int(input("Enter Customer payment Method\n 1.Cash\n 2.Card\n 3.Online\n Enter your choice between [1-3]: "))
        if(method < 1 or method > 3):
            print("Please enter your choice between [1-3]: ")
            continue
        else:
            break
    except ValueError:
            print("Please Enter the Integer Value.")
            exit(0)

# print(paymentMethod[method - 1])

app = ShoppingApp(name, phoneNumber, paymentMethod[method - 1])
# Item Selection By the Customer.
app.itemSelection()
#print(app.itemsPrice)
# # Total Purchased Amount Calculation
app.calculateAmount()

# Delivery option Selectons
deliveryOptions = ['home', 'take away']
options = None
while True:
    try:
        options = int(input('Enter your delivery Options\n 1. Home \n 2. Take Away\n Enter your Options between [1-2]: '))
        if(options < 1 or options > 2):
            print("Please enter your choice between [1-2]")
            continue
        else:
            break
    except ValueError:
        print("Please Enter the Integer Value.")
        exit(0)
    
if(deliveryOptions[options - 1] == 'home'):
    app.delivery(deliveryOptions[0])
    ShippingAddress = input("Enter the Customer Shipping Address: ")
    if(not ShippingAddress.isdigit()):
        app.customerShippingAddress = ShippingAddress
    else:
        print("Please Enter a valid Address")
        exit(0)

# Bill Generation for the Customer Purchased Product

print("################################### Billing Details ###################################")
print("\t\tShop Name: {}".format(app.shopName))
print("\t\tShop Address: {}".format(app.shopAddress))
print("\t\tShop Contact no: {}".format(app.shopPhoneNumber))
print("\n")
print("************************************ Customer Details **********************************")
print("\t\tCustomer Name: {}".format(app.customerName))
print("\t\tCustomer Phone Number: {}".format(app.customerPhoneNumber))

print('\n')
print('################################### Items Bought ###################################\n')

for item, quantity in app.cartItems.items():
    print("\t\tItem Bought : {}".format(item))
    print("\t\tItem Quantity: {}".format(quantity))
    if(isinstance(app.itemsPrice[app.itemsList.index(item)][1], int)):
        print("\t\tOriginal Item Price: {}".format(app.itemsPrice[app.itemsList.index(item)][0]))
        print("\t\tDiscount Price: {}".format(app.itemsPrice[app.itemsList.index(item)][1]))
        print('\n')
    else:
        print("\t\tItem Price: {}".format(app.itemsPrice[app.itemsList.index(item)][0]))
        print('\n')
print("\t\tTotal Tax Amount: {}".format(app.totalTax))

if(app.deliveryAmount > 0):
    print("\t\tDelivery Amount: {}".format(app.deliveryAmount))

if(app.totalAmountSaved > 0):
    print("\t\tTotal Amount Saved: {}".format(app.totalAmountSaved))

print("\t\tTotal Amount to be paid: {}".format(app.totalAmount))

print("\t\tPayment Method Used: {}".format(app.paymentModes.get(app.paymentMethod.lower(), "Payment is Not Selected Properly.")))

print("\t\tBilling Date and Time: {}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

if(app.customerShippingAddress is not None):
    print("\t\tShipping Address: {}".format(app.customerShippingAddress))