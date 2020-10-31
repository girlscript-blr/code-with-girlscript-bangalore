from datetime import datetime
n = (input("Enter your name: "))
p = int(input("Enter your phoneno.: "))
pm = (input("Enter the payment method(cash/card/online): "))

dict = {0:{"Name":"Earphones","Original_price":"1200", "Discount_price":"200", "weight":"150g"} ,1:{"Name":"Tablet","Original_price":"10000","Discount_price":"500","weight":"650g"},2:{"Name":"Bluetooth Speaker","Original_price":"900","Discount_price":"0","weight":"950g"},3:{"Name":"Bluetooth Mouse" ,"Original_price":"300","Discount_price":"0","weight":"120g"},4:{"Name":"Smart Phone","Original_price":"12000","Discount_price":"700","weight":"860g"}}
                                                                                                                                                                                                                                                                                                                                                    
for key,value in dict.items():
    print(key, ':', value)
s, q =input("Enter a single shopping item(index no. from list) and its quantity: ").split()
#"""if(d<=5) :
 #   shipping=0
#elif(d<=20):
 #   shipping=30
#else:
   # shipping=60
s=int(s)
#key=list(dict)
#s2=key[s]
q=int(q)
#if s2 in dict:
 #    s1=dict[s2]
q1=int((dict[s]['Discount_price']))
q2=int((dict[s]['Original_price']))

bill=q*(q2-q1)

h=(input("Want Home delivery/takeaway?? Write (Y) for takeaway else (N)"))
if(h=='N'):
    print('Ok! you selected the home delivery option.')
    d=int(input("Enter the distance of your home from the shop"))
    if(d>50):
        print("Sorry!! No delivery avaialable")
        ttax=0.06*bill
        amt=bill+ttax
    else:
           sh=(input("Enter the Shipping address"))
    if(d<=5) :
       shipping=0
       ttax=0.06*bill
       amt=bill+ttax
    elif(d<=20):
       shipping=30
       ttax=0.06*(30+bill)
       amt=30+bill+ttax
    else:
      shipping=60
      ttax=0.06*(60+bill)
      amt=60+bill+ttax
else:
    print('You selected to take your items with you.')
    ttax=0.06*bill
    amt=bill+ttax

now=datetime.now()


print('----------------------------------------------------------------------------------------Bill--------------------------------------------------------------------------------------')
print('Shop name:GadgetifyWithGSBlr')
print('Shopping address:311/5 Akshay nagar, Bangalore, Karnataka, India')
print('Shop contact no: +91 9988776655')
print('Customer name:',n)
print('Customer phone no:',p)
print('Item bought, its quantity & price & Discount price:',dict[s]['Name'],',',q,',',q*q2, ',',q*q1)
print('Total Tax:',ttax)
if((h=='N')and(d<=50)):
    print('Total Shipping charge:' ,shipping)
print('Total amount saved:' ,q*q1)   
print('Sum amount to be paid:',amt)
print('Payment method used:',pm)
print('Billing date and time:',now)
if((h=='N')and(d<=50)):
    print('Shipping address:',sh)
print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

