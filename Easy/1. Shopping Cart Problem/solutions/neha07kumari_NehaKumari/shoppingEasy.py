from datetime import datetime
n = (input("Enter your name: "))
p = int(input("Enter your phoneno.: "))
pm = (input("Enter the payment method(cash/card/online): "))

dict = {'0.Earphones':1200 ,'1.Tablet':10000,'2.Bluetooth Speaker':900,'3.Bluetooth Mouse':350,'4.Smart Phone':15000}
for key,value in dict.items():
    print(key, ':', value)
s, q =input("Enter a single shopping item(index no. from list) and its quantity: ").split()
s=int(s)
key=list(dict)
s2=key[s]
q=int(q)
if s2 in dict:
    s1=dict[s2]
bill=q*s1
ttax=0.06*bill
amt=bill+ttax
now=datetime.now()


print('----------------------------------------------------------------------------------------Bill--------------------------------------------------------------------------------------')
print('Shop name:GadgetifyWithGSBlr')
print('Shopping address:311/5 Akshay nagar, Bangalore, Karnataka, India')
print('Shop contact no: +91 9988776655')
print('Customer name:',n)
print('Customer phone no:',p)
print('Item bought, its quantity & price:',s2,',',q,',',bill)
print('Total Tax:',ttax)
print('Sum amount to be paid:',amt)
print('Payment method used:',pm)
print('Billing date and time:',now)
print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

