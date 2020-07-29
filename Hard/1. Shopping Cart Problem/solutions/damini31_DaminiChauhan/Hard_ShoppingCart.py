# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 14:43:31 2020

@author: daminichauhan1997
"""


import pandas as pd
from random import randint

pd.set_option('display.max_columns', 500)

def vendor_list():
    print("\n**********VENDOR MODE****************")
    print("\nPress 1 to Add shopping category")
    print("\nPress 2 to Add shopping item")
    print("\nPress 3 to View all shopping items and filter & sort them with name, category, original price, discount price.")
    print("\nPress 4 to View all shopping categories and filter & sort them with name.")
    print("\nPress 5 to View all customer orders and filter & sort them based on status.")
    print("\nPress 6 to Change order status.")
    print("\nPress 0 to exit.")

def is_present(a,new):
    x=False
    for i in a:
        if(i == new):
            x= True 
            break;
        else:
            x=False
    return x 


def vendor_mode():
    k=2
    while(k!=0):
        vendor_list()
        k = int(input("\nEnter the operation you want to perform.To exit,press 0: "))

        if(k==1):
            df=pd.read_csv("Category.csv",index_col=0)
            print(df)
            print("\nEnter the category you want to add. ")
            new = input("\nCategory: ")
            while(len(new)==0):
                print("Invalid Category Name.")
                new = input("\nCategory: ")
            if(is_present(df['Name'],new)==True):
                print("\nCategory Already Present")
            else:
                y=new
                x=randint(100, 999)
                new_entry={'Name':y,'Category ID':x}
                df=df.append(new_entry,ignore_index=True)
            print("\nThe updated category list is as follows :")
            print(df)
            df.to_csv("Category.csv")
         
        elif(k==2):
            df=pd.read_csv("Items.csv",index_col=0)
            print(df)
            print("\n")
            name=input("\nEnter the name of the product name: ")
            if(is_present(df['Name'],name)==False):
                o_price=int(input("\nEnter the original price of the product:"))
                d_price=int(input("\nEnter the discount price of the product:"))
                weight=input("\nEnter the weight for the product: ")
                gf=pd.read_csv("Category.csv",index_col=0)
                print(gf)
                check=True
                while(check):
                 ID=int(input("\nEnter the Category ID:"))
                 y=is_present(gf['Category ID'],ID)
                 if(y == True):
                   PID=df['Product ID '][len(df['Product ID '])-1] + 1
                   new_entry={'Name':name,'Original Price':o_price,'Discount Price':d_price,'Weight':weight,'Category ID':ID,'Product ID ':PID}
                   df=df.append(new_entry,ignore_index=True)
                   print("\nThe updated item list is as follows: ")
                   print(df)
                   df.to_csv("Items.csv")
                   check=False
                 else:
                    print("Invalid Category ID.Please Retry.")
                    check=True
            else:
                print("Item already present.")   
        
        elif(k==3):
                df=pd.read_csv("Items.csv",index_col=0)
                print(df)
                print("\n")
                
                print("Column List: ",df.columns)
                choice=int(input("\nDo you wish to filter or sort items.Press 1 to filter and 0 to sort: "))
                if(choice==1):
                    column=input("\nBy which column would you want to filter  the product: ")
                    if(column == "Name" or column == "Weight"):
                        value=input("Enter the product name/original price/Discount price/ID/weight of the product you want to filter out: ")
                        if(is_present(df[column],value)==True):
                              print(df[df[column] == value])
                        else:
                            print("The value entered is not present.")
                    else:
                        value=int(input("Enter the original price/Discount price/ID of the product you want to filter out: "))
                        if(is_present(df[column],value)==True):
                              print(df[df[column] == value])
                        else:
                            print("The value entered is not present.")
                else:
                    column=input("\nBy which column would you want to sort the product: ")
                    print(df.sort_values(column))
        
        elif(k==4):
            df=pd.read_csv("Category.csv",index_col=0)
            choice=int(input("\nDo you wish to filter or sort the categories by name.Press 1 to filter and 0 to sort : "))
            if(choice == 1):
               print("\nThe list of the categories: ")
               print("\n")
               print(df['Name'])
               name=input("\nEnter the Category name: ")
               if(is_present(df['Name'],name)==False):
                print("\nCategory Not Present.")
               else:
                print(df[df['Name']==name])
            else:
                print(df.sort_values('Name'))
            
        elif(k==5):
            df=pd.read_csv("Orders.csv",index_col=0)
            choice=int(input("\nDo you wish to filter or sort the orders.Press 1 to filter and 0 to sort: "))
            if(choice==1):
                print("\nColumns which can be used to filter:")
                print("\nOrder ID")
                print("\nOrder Status")
                print("\nBilling Date & Time")
                print("\nTotal amount")
                print("\nDelivery option")
                column=input("\nBy which column would you want to filter  the orders?   ")
                if(column == "Order ID" or column == "Total amount"):
                    value=int(input("Enter the OrderID/Total amount of the order you want to filter out: "))
                    if(is_present(df[column],value)==True):
                              print(df[df[column] == value])
                    else:
                            print("The value entered is not present.")
                else:
                    value=input("Enter the Order status/Billing date/Delivery option you want to filter out: ")
                    if(is_present(df[column],value)==True):
                              print(df[df[column] == value])
                    else:
                            print("The value entered is not present.")
            else:
                 print("\nColumns which can be used to sort:")
                 print("\nOrder ID")
                 print("\nOrder Status")
                 print("\nBilling Date & Time")
                 print("\nTotal amount")
                 print("\nDelivery option")
                 column=input("\nBy which column would you want to sort the orders?  ")
                 print(df.sort_values(column))
         
        elif(k==6):
                df=pd.read_csv("Orders.csv",index_col=0)
                print(df)
                print("\n Status Change Options:-")
                print("\n Received")
                print("\n Delivered")
                print("\n Cancelled")
                ID=int(input("\nEnter the order ID for the order whose status you want to change: "))
                Status=input("\nEnter the new status for the order ID: ")
                n=df[df['Order ID']==ID].index.values[0]
                df.at[n,'Order Status']=Status
                print("\nThe updated Order Details: ")
                print(df[df["Order ID"]==ID])
                df.to_csv("Orders.csv")
        else:
            if(k==0):
                break;
            else:
                print("\nThe option chosen is not available") 
            
def customer_list():
    print("\n**********CUSTOMER MODE****************")
    print("\n1.Press 1 to Create a new order")
    print("\n2.Press 2 to check the order status")
    print("\n3.Press 0 to exit")
    print("\n***************************************")
    
def calculate_bill(p_list,q_list,distance):
        pf=pd.read_csv("Items.csv",index_col=0)
        total=0
        savings=0
        print("\n  Product ID         Product Name             Original Price          Discount Price         Quantity         Total Amount")
        for i in range(len(p_list)):
            name=pf[pf['Product ID ']== p_list[i]]['Name'].values[0]
            o_price = pf[pf['Product ID '] == p_list[i]]['Original Price'].values[0]
            d_price = pf[pf['Product ID '] == p_list[i]]['Discount Price'].values[0]
            if(d_price!=0):
                f_price=d_price
                savings = savings + (o_price - d_price)*q_list[i]
            else:
                f_price=o_price
        
            print("\n  ",p_list[i],"            ",name,"                ",o_price,"                  ",d_price,"                ",q_list[i],"                  ",f_price*q_list[i])
            
            total=total + (f_price * q_list[i])
        fee=0
        if(distance==0):
                print("\n--------------------------------------------------------------------------------------------------------------------------")
                print("\nTotal Bill before tax: ",total)
                print("\nTax to be paid(6%): " ,total*0.06)
                print("\nTotal bill to be paid(including tax: ", total+(total*0.06))
            
        else:
                if(distance<=5):
                    fee=0
                elif(distance>5 and distance<=20):
                    fee=30
                else:
                    fee=60
                print("\n--------------------------------------------------------------------------------------------------------------------------")
                print("\nTotal Bill before tax :Rs",total)
                print("\nTax to be paid(6%) :Rs" ,total*0.06)
                print("\nDelivery charges upto {} kms ".format(distance),fee)
                print("\nTotal bill to be paid(including tax :Rs", total+(total*0.06) + fee)
                print("\nTotal Money Saved :Rs",savings)
        
        return total+(total*0.06) + fee            

def customer_mode():
        print("\n**********CUSTOMER MODE****************")
        k=2
        while(k!=0):
            customer_list()
            k = int(input("\nEnter the operation you want to perform.To exit,press 0  "))
            
            if(k==1):
                df=pd.read_csv("Orders.csv",index_col=0)
                #Details
                p_list=[] #product list
                q_list=[] #q_list
                name=input("\nEnter your name : ")
                phone=input("\nEnter your phone number: ")
                payment=input("\nPayment method to be used(Card/Cash/Online): ")
                check=True
                while(check):
                  print("\nChoose the Items from the list below by their Product ID")
                  pf=pd.read_csv("Items.csv",index_col=0)
                  print(pf)
                  j=2
                  while(j!=0):
                    t=int(input("\nEnter the Product ID: "))
                    y= is_present(pf['Product ID '],t)
                    if(y == True):
                      p_list.append(t)
                      r=int(input("\nEnter the quantity of the product: "))
                      q_list.append(r)
                      j=int(input("\nDo you want to add more items?Press 0 to exit and 1 to add more items?  "))
                      check = False
                    else:
                      print("Enter the correct Product ID")
                      check = True
                        
                delivery=int(input("\nPress 0 for Home Delivery and 1 for Takeaway:  "))
                if(delivery==0):
                    distance=int(input("What is the distance between your residence and the outlet: "))
                    if(distance<50):
                        address=input("Enter your address: ")
                        print("\n*************************************************************************")
                        print("\n**************************Welcome to GSBLr*******************************")
                        print("\n                  Shop name: GadgetifyWithGSBlr")
                        print("\n       Shop address: 311/5 Akshay nagar, Bangalore, Karnataka, India")
                        print("\n                  Shop contact no: +91 9988776655")
                        print("\nCustomer Name: ",name)
                        print("\nCustomer Mobile Number: ",phone)
                        print("\nPayment method used: ",payment)
                        total=calculate_bill(p_list,q_list,distance)
                        from datetime import datetime
                        now = datetime.now() 
                        print("\nBilling date and time :",now)
                        print("Address :",address)
                        order_status="in progress"
                        o_ID=randint(100,999)
                        print("Order ID: ",o_ID)
                        print("Order Status: ",order_status)
                        new_entry={'Order ID':o_ID,'Order Status':order_status,'Billing Date & Time':now,'Total amount':total,'Delivery option':"Home delivery",'Payment method':payment}
                        df=df.append(new_entry,ignore_index=True)
                        df.to_csv("Orders.csv")
                    else:
                        print("Home Delivery not available for distance more than 50 kms :")
                        c=int(input("Do you wish to continue.Press 1 to  continue and 0 to exit."))
                        if(c==0):
                            order_status="Cancelled"
                            total=0
                            from datetime import datetime
                            now = datetime.now()
                            delivery = "None"
                            payment = "None"
                            o_ID=randint(100,999)
                            new_entry={'Order ID':o_ID,'Order Status':order_status,'Billing Date & Time':now,'Total amount':total,'Delivery option':"Takeaway",'Payment method':payment}
                            print("Order ID: ",o_ID)
                            print("Order Status: ",order_status)
                            df=df.append(new_entry,ignore_index=True)
                            df.to_csv("Orders.csv")
                            print("Thank you for visiting us today")
                            break;
                        else:
                            print("\n*************************************************************************")
                            print("\n**************************Welcome to GSBLr*******************************")
                            print("\n                  Shop name: GadgetifyWithGSBlr")
                            print("\n       Shop address: 311/5 Akshay nagar, Bangalore, Karnataka, India")
                            print("\n                  Shop contact no: +91 9988776655")
                            print("\nCustomer Name: ",name)
                            print("\nCustomer Mobile Number: ",phone)
                            print("\nPayment method used: ",payment)
                            total=calculate_bill(p_list,q_list,distance=0)
                            from datetime import datetime
                            now = datetime.now() 
                            print("\nBilling date and time :",now)
                            order_status="Received"
                            o_ID=randint(100,999)
                            new_entry={'Order ID':o_ID,'Order Status':order_status,'Billing Date & Time':now,'Total amount':total,'Delivery option':"Takeaway",'Payment method':payment}
                            print("Order ID: ",o_ID)
                            print("Order Status: ",order_status)
                            df=df.append(new_entry,ignore_index=True)
                            df.to_csv("Orders.csv")
    
                        
                else:
                            print("\n*************************************************************************")
                            print("\n**************************Welcome to GSBLr*******************************")
                            print("\n                  Shop name: GadgetifyWithGSBlr")
                            print("\n       Shop address: 311/5 Akshay nagar, Bangalore, Karnataka, India")
                            print("\n                  Shop contact no: +91 9988776655")
                            print("\nCustomer Name: ",name)
                            print("\nCustomer Mobile Number: ",phone)
                            print("\nPayment method used: ",payment)
                            total=calculate_bill(p_list,q_list,distance=0)
                            from datetime import datetime
                            now = datetime.now() 
                            print("\nBilling date and time :",now)
                            order_status="Received"
                            o_ID=randint(100,999)
                            new_entry={'Order ID':o_ID,'Order Status':order_status,'Billing Date & Time':now,'Total amount':total,'Delivery option':"Takeaway",'Payment method':payment}
                            print("Order ID: ",o_ID)
                            print("Order Status: ",order_status)
                            df=df.append(new_entry,ignore_index=True)
                            df.to_csv("Orders.csv")   
            elif(k==2):
                df=pd.read_csv("Orders.csv",index_col=0)
                check=True
                while(check):
                 ID=int(input("\nEnter the ID whose status you wish to see: "))
                 y= is_present(df['Order ID'],ID)
                 if(y == True):
                   print("\nThe Status of the Order ID {} is: ".format(ID),df[df['Order ID']== ID]['Order Status'].values[0])
                   check=False
                 else:
                    print("\nIncorrect Order ID.Please Re-enter.")
                    check=True
            else:
                if(k==0):
                    break;
                else:
                    print("\nThe option chosen is not available") 
            
#User Interface to take input
def menu():
    print("\n********************Welcome to GSBLr****************************")
    print("\nChoose the mode from the list below to operate in the desired more")
    print("\n--------------------------------------------------------------------")
    print("\n1.Vendor Mode(Press 1 to operate in vendor mode")
    print("\n2.Customer Mode(Press 2 to operate in customer mode")
    print("\n Press 0 to exit\n")
    print("\n--------------------------------------------------------------------")

ch=2
while(ch!=0):
    menu()
    print("\nEnter the mode you want to operate in ,Else press 0 to exit.\n")
    ch=int(input())
    if(ch==1):
        vendor_mode()
    elif(ch==2):
        customer_mode()
    else:
        if(ch==0):
           break;
        else:
            print("\nMode not available")