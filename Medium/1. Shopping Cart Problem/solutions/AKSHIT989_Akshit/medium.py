from prettytable import PrettyTable
#shopping items
shoppingItems = {
   #no: [     name             ,price, discounted_price,  weight      ]
    1 : ['Basshead Earphones'  ,1200 , 899   , 150] ,
    2 : ['Bluetooth Mouse'     ,600  , 600   , 120] ,
    3 : ['32-GB Pen drive'     ,499  , 399   , 30] ,
    4 : ['29-Inch LED monitor' ,33499, 29999 , 4000] ,
    5 : ['i7-processor'        ,18999, 18999 , 15] ,
    6 : ['1-TB Hard Drive'     ,3999 , 3999  , 175] ,
    7 : ['16-GB DDR4 RAM'      ,10999, 9999  , 35]
}
y=PrettyTable()
y.field_names = ["Item No.", "Item Name", "Price","Discount price","Weight"]
for i in shoppingItems:
    y.add_row([i , shoppingItems[i][0], shoppingItems[i][1], shoppingItems[i][2], shoppingItems[i][3] ])

global total_bill
total_bill=0
discounted_bill=0

#customer data input
Name      = input('\nEnter your Name: ')
phone     = input('Enter Contact No.: ')
payMethod = input('Enter payment method(cash/card/online): ')

bill = { } #storing purchased items

#shopping list input starts from here
while(True):
    print('\nShopping list::\n')
    print(y)
    
    choice=int(input('Enter your choice:'))
    quantity=int(input('Enter quantity:'))
    bill[choice]=quantity
    total_bill += shoppingItems[choice][1]*quantity
    discounted_bill+=shoppingItems[choice][2]*quantity
    opt=input('\nDo you want to continue:(Y-Yes/N-No):')
    if opt=='n':
        break
#shopping list input ends here
dist=0
address=''

thd=input('Select T-Takeaway/H-Home Delivery: ')
if thd=='h' :
    dist=int(input('Distance from shop to the delivery address(in km): '))
    address=input('Shipping Address: ')

ship_charge=0
if dist<=5:
    ship_charge=0
elif dist<=20:
    ship_charge=30
elif dist<=50:
    ship_charge=60
else:
    ship_charge=-1


#BILL GENERATION
print('-------------------------------------------------------------------')
print('                           Your bill:                            \n')
#printing static data
print(
    '                                        Shop name: GadgetifyWithGSBlr\n',
    '                                    Shop address: 311/5 Akshay nagar,\n',
    '                                          Bangalore, Karnataka, India\n'
    '                                      Shop contact no: +91 9988776655\n'
)
#end of printing static data
#printing variable data
print('\nCustomer name: '+ Name)
print('Contact No.: '+ phone)
print('\nItems bought:')


x = PrettyTable()
x.field_names = ["Item Name", "Quantity", "Price","Discount price"]

for i in bill:
    x.add_row([shoppingItems[i][0],bill[i] , shoppingItems[i][1]*bill[i], shoppingItems[i][2]*bill[i] ])
print(x)

print('\nTotal tax on original price: %.2f' %(total_bill*0.06))
print('\nTotal tax on discount price: %.2f' %(discounted_bill*0.06))

if ship_charge==-1:
    print('Shipping not possible')
    ship_charge=0
else:
    print('Total Shipping charges: ',ship_charge)

print('Total Amount saved: ', total_bill-discounted_bill)

print('Amount to be paid: %.2f' %(discounted_bill*1.06 + ship_charge))
print('\nPayment method used:'+ payMethod)

import datetime
now = datetime.datetime.now()
print ('Date and time:',now.strftime("%d-%m-%Y %H:%M:%S"))

if thd=='h':
    print('Shipping Address:', address)

print('-------------------------------------------------------------------')