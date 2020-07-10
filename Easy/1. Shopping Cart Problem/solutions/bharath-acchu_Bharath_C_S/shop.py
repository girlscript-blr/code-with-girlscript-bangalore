import time
import re
from datetime import datetime
from pytz import timezone

print()
print()
print('*'*50 + ' Welcome to GadgetifyWithBlr '+ '*'*50)
print()
print(' '*50 + ' Here is the list of items ')
print()


print(' '*30+ ' Item/Item number'+" "*33+' Price(in ₹)')
print(' '*28+ '--------------------'+' '*30+'------------')
print(' '*25 +"1.Wireless Keyboard- HP Multimedia "+' '*20+' ₹ 1350.00')
print(' '*25 +"2.Wireless optical Mouse- Lenova yoga "+' '*17+' ₹ 6000.00')
print(' '*25 +"3.boAt Bassheads 242 Wired headset"+' '*21+' ₹ 550.00')
print(' '*25 +"4.boAt Airpods 201 earbuds "+' '*28+' ₹ 2000.00')
print(' '*25 +"5.Mi 20000 mAh Powe banks"+' '*30+' ₹ 1600.00')
print(' '*25 +"6.boAt bar bluetooth sounbar "+' '*26+' ₹ 8000.00')
print(' '*25 +"7.M3 Bluetooth 4.2 Fitband "+' '*28+' ₹ 350.00')
print(' '*25 +"8.SanDisk 64 GB pendrive "+' '*30+' ₹ 2500.00')
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


            # dictionary for retrievel of money
            dict_price = {1:int(1350),2:int(6000),3:int(550),4:int(2000),5:int(1600),6:int(8000),7:int(350),8:int(2500)}
            # dictionary for retrievel of item
            dict_item = {1:'Wireless Keyboard- HP Multimedia ',2:'Wireless optical Mouse- Lenova yoga',3:'boAt Bassheads 242 Wired headset',4:'boAt Airpods 201 earbuds',5:'Mi 20000 mAh Powe banks',6:'boAt bar bluetooth sounbar',7:'M3 Bluetooth 4.2 Fitband ',8:'SanDisk 64 GB pendrive '}
            print()
            print(' '*10+' Please select the items to be purchased from above list :')

            item = int(input(' '*10+' Enter the item number :'))
            #qty = int(input(' '*10+" Enter it's quantity :"))

            if item >=9:
                print('Invalid Choice, there is no such item number')
                time.sleep(5)
            else:
                qty = int(input(' '*10+" Enter it's quantity :"))

                amt = dict_price[item] * qty
                tax = float(amt)*0.06
                tot_amt = float(amt+tax)



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
                print(' '*25+ 'Item Bought'+' '*15+ 'Quantity'+' '*15+' Price')
                print(' '*25+ '------------'+' '*13+'---------'+' '*15+'--------')
                print()
                print(' '*15+dict_item[item]+' '*5+str(qty)+' '*23+str(amt))
                print()
                print()
                print()
                print(' '*10+' Total Tax : '+' '*30+str(tax))
                print(' '*10+' Sum to be paid : '+' '*25+str(tot_amt))
                print(' '*10+' Payment method used: '+' '*22+ mode)
                print()
                print()
                print('*'*55 + ' Visit Again, Happy shopping '+ '*'*55)

                time.sleep(5)
    else:
        print(' '*10+' Invalid Phone number, number should start with 0 or 91 followed by 10 digit number starting with 8 or 7 or 9')
        time.sleep(5)



