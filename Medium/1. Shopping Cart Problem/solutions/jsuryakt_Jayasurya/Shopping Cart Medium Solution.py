from collections import OrderedDict 
from datetime import date,datetime

#Shop Info
shopName = "GadgetifyWithGSBlr"
shopAddress = "311/5 Akshay nagar,\n\t\t\t\t\t     Bangalore, Karnataka, India"
shopContactNo = "+91 9988776655"

#Items in Ordered Dictionary
items = OrderedDict({"Basshead earphones": [1200,899,150], "Bluetooth computer mouse": [600,399,120], "Pendrive 16GB": [300,'-',98], "Powerbank 10000mAh": [900,'-',400], "Fitness Band": [3000,2299,200]})

#Taking User Info
name = input("Enter Name: ")
phoneNo = int(input("Enter Phone Number: "))
paymentMethod = input("Enter Payment method (cash/card/online): ")
deliveryType = input("Home Delivery/Takeaway ?")

#Setting Up some flags
deliveryFlag = 0
distanceFlag = 0
deliveryCharge = 0

#Checking Delivery Type and setting Delivery Amount
"""
Distance	Price
<= 5 KM	Free
<= 20 KM	Rs. 30
<= 50 KM	Rs. 60
> 50 KM	No delivery
"""
if deliveryType.lower() == "home delivery":
    deliveryFlag = 1
    distance = float(input("What is the distance to you Home? (in km)"))
    if distance <= 20 and distance > 5:
        deliveryCharge = 30
    elif distance <= 50 and distance > 20:
        deliveryCharge = 60
    elif distance > 50:
        print("\nSorry we don't deliver to your address!\n\nDelivery changed to Takeaway!\n")
        deliveryType = "Take-Away"
        deliveryFlag = 0
        distanceFlag = 1
    if distanceFlag == 0:
        address = input("What is your address ?")
else:
    distance = 0.0

#Displaying Items to User
print("\n{0} {1:>12} {2:>23} {3:>25} {4:>15}\n".format("ID","Item","Price","Discounted Price","Weight(gm)"))

amount = 0
ans = 'Y'
lst = []
totAmount = 0

#Taking Multiple Inputs
while(ans != 'n'):
    for key,num in zip(items.keys(),range(len(items))):
        print("\n{0}.  {1:<30} Rs.{2:<12} Rs.{3:<20} {4:3}".format(num+1, key, items[key][0],items[key][1],items[key][2]))

    selectedItemID = int(input("\nEnter ID of item to select: "))
    itemQuantity = int(input("Enter quantity of the item: "))
    selectedItem = list(items.keys())[selectedItemID-1]
    
    #Checking if there is any discount on the product and if there is any then calculating Amount Saved
    if items[selectedItem][1] == '-':
        amount = items[selectedItem][0]*itemQuantity
        amountSaved = 0
    else:
        amount = items[selectedItem][1]*itemQuantity
        amountSaved = (items[selectedItem][0] - items[selectedItem][1]) * itemQuantity
    
    #Storing all Item values in a list to PRINT later
    lst.append([selectedItemID,itemQuantity,selectedItem,items[selectedItem][0],items[selectedItem][1],amount,amountSaved])
    totAmount += amount
    
    ans = input("\nDo you want to add more items?  (Y/N)").lower()

#Tax Amount 6%
taxAmount = 6/100 * totAmount

#Total Amount
totalAmount = totAmount + taxAmount

#Generating Bill
print("\n------------------------------BILL GENERATED------------------------------\n")
print("Shop:",shopName,end="{:<12}".format(" "))
print("Address:",shopAddress)
print("Contact Us:",shopContactNo)
print("\nCustomer Name:",name,end="{:<10}".format(" "))
print("Phone No. :",phoneNo,end="{:<10}".format(" "))
print("Delivery Type :",deliveryType.upper())

#If DeliveryType was set to Home, then displaying Address
if deliveryFlag:
    print("\nAddress :",address)

#Displaying User seleected Items
print("\n\n{0} {1:>12} {2:>23} {3:>22} {4:>15} {5:>15} {6:>18}\n".format("ID","Item","Price","Discounted Price","Quantity","Amount", "Amount Saved"))
print("------------------------------------------------------------------------------------------------------------------")
for i in range(len(lst)):
    print("{0:<6} {1:<26} {2:>5} {3:>15} {4:>18} {5:>18} {6:>15}".format(lst[i][0],lst[i][2],lst[i][3],lst[i][4],lst[i][1],lst[i][5],lst[i][6]))
print("------------------------------------------------------------------------------------------------------------------")
print("Total Amount (Without Tax): Rs.{}/-".format(totAmount))
print("\nTotal tax(6%): Rs.{}/-".format(taxAmount))
print("\nTotal Amount after Tax: Rs.{}/-\n".format(totalAmount))

#If DeliveryType was set to Home, then displaying Delivery Charges
if deliveryFlag:
    if deliveryCharge == 0:
        print("Yayy! We are offering Free Delivery to you.\n") #If Distance is <=5
    totalAmount += deliveryCharge
    print("Delivery Charges: Rs.{}/-".format(deliveryCharge))
    
print("\nTotal Amount to be paid: Rs.{}/-\n".format(totalAmount))
print("Payment Method :", paymentMethod,end="{:<10}".format(" "))

now = datetime.now()
time = now.strftime("%B %d, %Y %I:%M:%S%p")

print("Billing Date & time:",time)
print("\n------------------------------THANK YOU----------------------------------------")