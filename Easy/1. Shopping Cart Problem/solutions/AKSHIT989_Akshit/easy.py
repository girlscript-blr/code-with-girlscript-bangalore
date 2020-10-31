#shopping items
shoppingItems = {
    1 : ['Basshead Earphones'  ,1200 ] ,
    2 : ['Bluetooth Mouse'     ,600  ] ,
    3 : ['32-GB Pen drive'     ,499  ] ,
    4 : ['29-Inch LED monitor' ,33499],
    5 : ['i7-processor'        ,18999] ,
    6 : ['1-TB Hard Drive'     ,3999 ],
    7 : ['16-GB DDR4 RAM'      ,10999]
}
global total_bill
total_bill=0

#customer data input
Name      = input('\nEnter your Name: ')
phone     = input('Enter Contact No.: ')
payMethod = input('Enter payment method(cash/card/online): ')
#end of customer data input

bill = { } #storing purchased items

#shopping list input starts from here
print('\nShopping list::\n')
print(' No.      Item Name           Price')
print('-------------------------------------')
print(
    ' 1.   Basshead Earphones      1200\n' ,
    '2.   Bluetooth Mouse         600\n'  ,
    '3.   32-GB Pen drive         499\n'  ,
    '4.   29-Inch LED monitor     33499\n' ,
    '5.   i7-processor            18999\n' ,
    '6.   1-TB Hard Drive         3999\n' ,
    '7.   16-GB DDR4 RAM          10999\n' 
)
choice=int(input('Enter your choice:'))
quantity=int(input('Enter quantity:'))

total_bill += (shoppingItems[choice][1]*quantity)
#shopping list input ends here

#BILL
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

print('\nItem bought: ',shoppingItems[choice][0])
print('Quantity: ', quantity)
print('Price: ', shoppingItems[choice][1]*quantity)
print('Total tax: %.2f' %(total_bill*0.06))
print('Amount to be paid: %.2f' %(total_bill*1.06))
print('Payment method used:'+ payMethod)

import datetime
now = datetime.datetime.now()
print ('\nDate and time:',now.strftime("%d-%m-%Y %H:%M:%S"))

print('-------------------------------------------------------------------')