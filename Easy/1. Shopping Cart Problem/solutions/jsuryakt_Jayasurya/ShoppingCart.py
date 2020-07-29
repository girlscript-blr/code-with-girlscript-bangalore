from collections import OrderedDict 
from datetime import date,datetime

shopName = "GadgetifyWithGSBlr"
shopAddress = "311/5 Akshay nagar,\n\t\t\t\t\t     Bangalore, Karnataka, India"
shopContactNo = "+91 9988776655"
items = OrderedDict({"Basshead earphones": 1200, "Bluetooth computer mouse": 600, "Pendrive 16GB": 300, "Powerbank 10000mAh": 900, "Fitness Band": 3000})

name = input("Enter Name: ")
phoneNo = int(input("Enter Phone Number: "))
paymentMethod = input("Enter Payment method (cash/card/online): ")

print("\n{0} {1:>12} {2:>23} \n".format("ID","Item","Price"))

for key,num in zip(items.keys(),range(len(items))):
    print("{0}. {1:<30} Rs.{2}".format(num+1, key, items[key]))
    
selectedItemID = int(input("Enter ID of item to select: "))
itemQuantity = int(input("Enter quantity of the item: "))

selectedItem = list(items.keys())[selectedItemID-1]

amount = items[selectedItem]*itemQuantity

taxAmount = 6/100 * amount

totalAmount = amount + taxAmount

print("\n------------------------------BILL GENERATED------------------------------\n")
print("Shop:",shopName,end="{:<12}".format(" "))
print("Address:",shopAddress)
print("Contact Us:",shopContactNo)
print("\nCustomer Name:",name,end="{:<10}".format(" "))
print("Phone No. :",phoneNo,end="{:<10}".format(" "))
print("\n\n{0} {1:>12} {2:>23} {3:>12} {4:>15}\n".format("ID","Item","Price","Quantity","Amount"))
print("---------------------------------------------------------------------")
print("{0:<6} {1:<26} {2:} {3:>10} {4:>18}\n".format(selectedItemID,selectedItem,items[selectedItem],itemQuantity,amount))
print("Total tax(6%):",taxAmount )
print("\nTotal Amount to be paid: Rs.{}/-\n".format(totalAmount))
print("Payment Method :", paymentMethod,end="{:<10}".format(" "))

now = datetime.now()
time = now.strftime("%B %d, %Y %I:%M:%S%p")

print("Billing Date & time:",time)
print("\n------------------------------THANK YOU-----------------------------------")