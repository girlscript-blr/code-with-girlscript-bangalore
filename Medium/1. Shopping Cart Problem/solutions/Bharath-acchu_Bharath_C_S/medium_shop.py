import time
import re
from prettytable import PrettyTable
from datetime import datetime
from pytz import timezone

print()
print()
print('*'*50 + ' Welcome to GadgetifyWithBlr '+ '*'*50)
print()
print(' '*50 + ' Here is the list of items ')
print()

# shooping list is on the order: Item_no,Itemname , Actual_price , discount_price ,weight
shopping_list = {
    1:['Wireless Keyboard - HP multimedia', 1350 ,1000, 500],
    2:['Wireless Optical mouse - Lenova Yoga', 5900, 4000, 100],
    3:['boAt Bassheads 242 Wired Headset', 500,450,200],
    4:['boAt Earpods 201 earbuds',2000,1500,100],
    5:['Mi 20000 mAh Powe Bank',1600,1200,400],
    6:['boAt bluetooth soundbar',8000,7000,700],
    7:['M3 Bluetooth 4.2 Fitband',350,300,300],
    8:['Sandisk 64 GB pendrive',2500,2000,200]
}
b = PrettyTable()
b.field_names = ["Item_no.", "Item_Name", "Price","Discount_price","Weight"]
for i in shopping_list:
    b.add_row([i , shopping_list[i][0], shopping_list[i][1], shopping_list[i][2], shopping_list[i][3] ])

print(b)

print()
print()
print(' '*10+' Please Provide the following details :')
custname = str(input(' '*10+' Enter your name :'))
if not all(x.isalpha() or x == ' ' for x in custname):
    print(" "*10+"Please enter a Valid Name ")
    time.sleep(5)
else:
    custphone = input(' '*10+ ' Enter your PhoneNumber :')
    def isValid(s): 
        
        # 1) Begins with 0 or 91 
        # 2) Then contains 7 or 8 or 9. 
        # 3) Then contains 9 digits 
        Pattern = re.compile("(0/91)?[7-9][0-9]{9}") 
        return Pattern.match(s) 
    if (isValid(custphone)):  
        
    
        mode = input(' '*10+' Enter the payment method(cash/card/online) :')
        list1 = ['cash','Cash','CASH','card','CARD','Card','online','Online','ONLINE']

        if mode not in list1:
            print(' '*10+' Invalid payment mode ')
        else:
            tot_bill = 0
            discount_bill = 0
            # Storing shopping items
            shopped_items = { }

            while(True):



                print(' '*10+' Please select the items to be purchased from above list :')

                item = int(input(' '*10+' Enter the item number :'))
                #qty = int(input(' '*10+" Enter it's quantity :"))

                if item >=9:
                    print(' '*10+' Invalid Choice, there is no such item number')
                    time.sleep(5)
                else:
                    qty = int(input(' '*10+" Enter it's quantity :"))
                    
                    shopped_items[item] = qty
                    tot_bill += shopping_list[item][1] * qty
                    discount_bill += shopping_list[item][2]*qty

                    ch = input(' '*10+' Want to purchase another item : (press y to continue / n to quit) ')
                    if ch == 'n':
                        break

            # calculation for shipping

            dist = 0
            ship_charge = 0

            shipping = input(' '*10+' Choose t for Takeaway/ h for Home Delivery : ')
            if shipping == 'h':
                dist = float(input(' '*10+' Enter the distance from shop to the delivery address(in km) : '))
                if dist > 50:
                    ship_charge = 0
                    ship = False
                    print(' '*10+' Shipping is not available ')
                else :
                    ship = True
                    address = input(' '*10+' Enter shipping address : ')
            
            if shipping == 't':
                ship =False
                
            if dist <=5:
                ship_charge = 0
            elif dist <= 20 :
                ship_charge = 30
            elif dist <= 50:
                ship_charge = 60
            else:
                ship_charge = 0
                print(' '*10+' so shipping charge is made zero!')
                    
            print()
            print()
                

            

            print('*'*60 + ' Bill Details '+ '*'*60)
            print(' '*50 + ' Shop Name: GadgetifyWithBlr  ')
            print(' '*35 + ' Shop Address: 311/5 Akash Nagar , Bangalore,Karnataka,India ')
            print(' '*50 + ' Shop Phone.No : +91 9988776655 ')
            print()


                        
            India = timezone('Asia/Kolkata')
            ist = datetime.now(India)

            print(' '*70+'Date and Time of Purchase : '+ ist.strftime('%d/%m/%Y  %H:%M:%S'))
            print()
            print(' '*10+' Customer Name : ',custname)
            print(' '*10+' Customer Phone.No: ',custphone)
            print()
            d = PrettyTable()
            d.field_names = ["Item_name", "Quantity","Price","Discount_Price"]

            for i in shopped_items:
                    d.add_row([shopping_list[i][0], shopped_items[i] , shopping_list[i][1]*shopped_items[i], shopping_list[i][2]*shopped_items[i] ])

            print(d)       
            print()
            print(' '*10+' Total Tax on actual price of items : %.2f' %(tot_bill*0.06))
            print(' '*10+' Total Tax on discount price of items : %.2f' %(discount_bill*0.06))
            print(' '*10+' Total amount saved: ',tot_bill-discount_bill)
            if(ship):
                print(' '*10+' Shipping address: ',address)
                print(' '*10+' Shipping distance(in Km): ',dist)
                print(' '*10+' Shipping charges :',ship_charge)
            elif (dist > 50):
                #print(' '*10+' Shipping charges :',ship_charge)
                print(' '*10+' Shipping is not available, shipping charge : 0 ')
            else:
                print(' '*10+' Shipping charges :',ship_charge)



            print(' '*10+' Amount to be paid: %.2f' %(discount_bill*1.06 + ship_charge))

            
            print(' '*10+' Payment method used: ', mode)
            print()
            print()
            print('*'*55 + ' Visit Again, Happy shopping '+ '*'*55)

            time.sleep(5)
            
    else:
        print(' '*10+' Invalid Phone number, number should start with 0 or 91 followed by 10 digit number starting with 8 or 7 or 9')
        time.sleep(5)
