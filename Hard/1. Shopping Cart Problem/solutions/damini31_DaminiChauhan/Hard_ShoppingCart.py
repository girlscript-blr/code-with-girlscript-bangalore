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

def check_for_digits(a):
    return any(char.isdigit() for char in a)
    

def vendor_mode():
  k=2
  while(k!=0):
     vendor_list()
     try:  
        k = int(input("\nEnter the operation you want to perform.To exit,press 0: "))

        if(k==1):
            df=pd.read_csv("Category.csv",index_col=0)
            print(df)
            print("\nEnter the category you want to add. ")
            category_check=True
            while(category_check):
               new = input("\nCategory: ")
               if(len(new)==0):
                  print("Mandatory Field.Please enter Category Name.")
                  category_check=True
               else:
                      if(is_present(df['Name'],new)==True):
                        print("\nCategory Already Present")
                        category_check=False
                        
                      else:
                        if(check_for_digits(new)):
                          print("Category name can only contain alphabets....")
                          category_check=True
                        
                        else:
                          y=new
                          x=randint(100, 999)
                          new_entry={'Name':y,'Category ID':x}
                          df=df.append(new_entry,ignore_index=True)
                          print("\nThe updated category list is as follows :")
                          print(df)
                          df.to_csv("Category.csv")  
                          category_check=True
                          
                   
                    
                
            
         
        elif(k==2):
            df=pd.read_csv("Items.csv",index_col=0)
            print(df)
            print("\n")
            name_check=True
            while(name_check):
              name=input("\nEnter the name of the product name: ")
              if(len(name)==0):
                print("Mandatory Field.Please enter a value")
                name_check=True
              else: 
                 if(is_present(df['Name'],name)==True):
                     print("\nProduct name Already Present")
                     name_check=False
                 else:
                     if(check_for_digits(name)):
                          print("Product name can only contain alphabets....")
                          name_check=True
                     else:
                         name_check=False
                      
            o_check=False
            while(o_check == False):
                    o_price = input("\nEnter the original price of the product:")
                    if(len(o_price)==0):
                        print("\nMandatory Field.Please Enter a value.")
                        o_check ==False
                    else: 
                        try:
                           o_price= int(o_price)
                           o_check=True
                        except(ValueError):
                            print("Only integer values are allowed.")
                            o_check =False
            
            d_check=False
            while(d_check == False):
                    d_price = input("\nEnter the discount price of the product:")
                    if(len(d_price)==0):
                        print("\nMandatory Field.Please Enter a value.")
                        d_check = False
                    else: 
                        try:
                           d_price= int(d_price)
                           d_check=True
                        except(ValueError):
                            print("Only integer values are allowed.")
                            d_check = False
            weight=input("\nEnter the weight for the product: ")
            while(len(weight)==0):
                   print("Invalid Value.Try Again")
                   weight = input("\nWeight : ")
            gf=pd.read_csv("Category.csv",index_col=0)
            print(gf)
            check=False
            while(check==False):
                 ID=input("\nEnter the Category ID:")
                 if(len(ID)==0):
                      print("\nMandatory Field.Please Enter a value.")
                      check = False
                 else:
                   try:
                       ID=int(ID)
                       check=False
                       y=is_present(gf['Category ID'],ID)
                       
                       if(y == True):
                         PID=df['Product ID '][len(df['Product ID '])-1] + 1
                         new_entry={'Name':name,'Original Price':o_price,'Discount Price':d_price,'Weight':weight,'Category ID':ID,'Product ID ':PID}
                         df=df.append(new_entry,ignore_index=True)
                         print("\nThe updated item list is as follows: ")
                         print(df)
                         df.to_csv("Items.csv")
                         check=True
                       else:
                         print("Category ID not present.Please retry. ")
                         check=False
                         
               
                   except(ValueError):
                       print("Invalid Category ID.Please Retry.")
                       check=False
        
        elif(k==3):
                df=pd.read_csv("Items.csv",index_col=0)
                print(df)
                print("\n")
                
                print("Column List: ",df.columns)
                choice=int(input("\nDo you wish to filter or sort items.Press 1 to filter and 0 to sort: "))
                if(choice==1):
                  column=input("\nBy which column would you want to filter  the product: ")
                  y=is_present(df.columns,column)
                  if(y == True):
                     if(column == "Name" or column == "Weight"):
                        value=input("Enter the {} of the product you want to filter out: ".format(column))
                        if(is_present(df[column],value)==True):
                            print(df[df[column] == value])
                        else:
                            print("The value entered is not present.")
                  
                     else:
                        value=int(input("Enter the {} of the product you want to filter out: ".format(column)))
                        if(is_present(df[column],value)==True):
                            print(df[df[column] == value])
                        else:
                            print("The value entered is not present.")
                  else:
                            print("Column name entered cannot be found.")
                            print("\nLoading the vendor menu again.................")
                
                elif(choice==0):
                    column=input("\nBy which column would you want to sort the product: ")
                    y=is_present(df.columns,column)
                    if(y==True):
                       print(df.sort_values(column))
                    else:
                        print("Column name entered cannot be found.")
                        print("\nLoading the vendor menu again.................")
            
                else:
                       print("\nInvalid choice.Please try again.")
                       print("\nLoading the vendor menu again.................")
        
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
            elif(choice==0):
                print(df.sort_values('Name'))
            else:
                print("\nInvalid choice.Please try again.")
                print("\nLoading the vendor menu again.................")
            
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
                y=is_present(df.columns,column)
                if(y == True):
                  if(column == "Order ID" or column == "Total amount"):
                    value=int(input("Enter the {} of the order you want to filter out: ".format(column)))
                    if(is_present(df[column],value)==True):
                              print(df[df[column] == value])
                    else:
                            print("The value entered is not present.")
                  else:
                    value=input("Enter the {} you want to filter out: ".format(column))
                    if(is_present(df[column],value)==True):
                              print(df[df[column] == value])
                    else:
                            print("The value entered is not present.")
                else:
                    print("Column name entered cannot be found.")
                   
            elif(choice==0):
                 print("\nColumns which can be used to sort:")
                 print("\nOrder ID")
                 print("\nOrder Status")
                 print("\nBilling Date & Time")
                 print("\nTotal amount")
                 print("\nDelivery option")
                 column=input("\nBy which column would you want to sort the orders?  ")
                 print(df.sort_values(column))
            
            else:
                print("\nInvalid choice.Please try again.")
                print("\nLoading the vendor menu again.................")
                
        elif(k==6):
                df=pd.read_csv("Orders.csv",index_col=0)
                print(df)
                print("\n Status Change Options:-")
                print("\n Received")
                print("\n Delivered")
                print("\n Cancelled")
                ID=int(input("\nEnter the order ID for the order whose status you want to change: "))
                y=is_present(df['Order ID'],ID)
                if(y == True):
                  Status=input("\nEnter the new status for the order ID: ")
                  n=df[df['Order ID']==ID].index.values[0]
                  df.at[n,'Order Status']=Status
                  print("\nThe updated Order Details: ")
                  print(df[df["Order ID"]==ID])
                  df.to_csv("Orders.csv")
                else:
                  print("The Order ID entered is not present")
        else:
            if(k==0):
                break;
            else:   
                print("\nThe option chosen is not available") 
       
     except(ValueError):
         print("Invalid Value for the operation!")
         
         
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
   k=2
   while(k!=0):
       customer_list()
       try:
            k = int(input("\nEnter the operation you want to perform.To exit,press 0  "))
            
            if(k==1):
                df=pd.read_csv("Orders.csv",index_col=0)
                #Details
                p_list=[] #product list
                q_list=[] #q_list
                n_check=True
                while(n_check):
                   name=input("\nEnter your name : ")
                   if(len(name)==0):
                     print("\nMandatory Field.Please enter Customer's Name.")
                     n_check=True
                   else:
                     if(check_for_digits(name)):
                         print("\nCustomer name can only contain alphabets.")
                         n_check=True
                     else:
                         n_check=False
                p_check=True
                while(p_check):
                  phone=input("\nEnter your phone number: ")
                  if(len(phone)==0):
                     print("\nMandatory Field.Please enter Customer's Phone number.")
                     p_check = True
                  else:
                      if(phone.isdigit()):
                          p_check = False
                      else:
                          print("\nOnly Digits allowed.Please Re-enter")
                          p_check=True
                
                py_check=True
                while(py_check):
                  payment=input("\nPayment method to be used(Card/Cash/Online): ")
                  if(len(payment)==0):
                     print("\nMandatory Field.Please enter a valid Payment method.")
                     print("\nOptions Available :")
                     print("\n1.Cash")
                     print("\n2.Card")
                     print("\n3.Online")
                     py_check = True
                  else:
                      if(payment == "Cash" or payment == "Card" or payment == "Online"):
                          py_check=False
                      else:
                          print("Please enter a valid option.")
                          print("\nOptions Available :")
                          print("\n1.Cash")
                          print("\n2.Card")
                          print("\n3.Online")
                          py_check=True
                 
                check=True
                while(check):
                  print("\nChoose the Items from the list below by their Product ID")
                  pf=pd.read_csv("Items.csv",index_col=0)
                  print(pf)
                  j=2
                  while(j!=0):
                      p_check=True
                      while(p_check):
                         t=input("\nEnter the Product ID: ") 
                         if(len(t)==0):
                             print("\nMandatory Field.Please enter Product ID.")
                             p_check = True
                         else:
                             try:
                                t=int(t)
                                y=is_present(pf['Product ID '],t)
                                
                                if(y == True):
                                    p_list.append(t)
                                    q_check=True
                                    while(q_check):
                                       r=input("\nEnter the quantity of the product: ")
                                       if(len(r)==0 or r == "0"):
                                            print("\nMandatory Field.Quantity Cannot be zero or blank.")
                                            q_check = True
                                       else:
                                           try:
                                               r=int(r)
                                               q_list.append(r)
                                               j=int(input("\nDo you want to add more items?Press 0 to exit and 1 to add more items?  "))
                                               if(j==0):
                                                   check=False
                                               else:
                                                   check=True 
                                               q_check=False
                                               p_check = False
                                            
                                           except(ValueError):
                                                print("\nQuantity is numeric.Please Re-enter ")
                                                q_check=True
                                       
                                       
          
                                
                                else:
                                    print("\nEnter the correct Product ID")
                                    p_check = True
                            
                             except(ValueError):
                                print("\nProduct ID is numeric.Please Re-enter")
                                p_check=True
                                
                delivery=int(input("\nPress 0 for Home Delivery and 1 for Takeaway:  "))
                if(delivery==0):
                  distance=int(input("What is the distance between your residence and the outlet: "))
                  d_check=True
                  while(d_check):
                     distance=input("What is the distance between your residence and the outlet: ")
                     if(len(distance)==0):
                         print("\nMandatory Field.Please enter the distance as home delivery has been selected.")
                         d_check=True
                     else:
                          try:
                              distance=int(distance)
                              d_check=False
                          except(ValueError):
                              print("Only numeric digits can be entered.Try again")
                              d_check=True
                   
                  if(distance<50):
                        a_check=True
                        while(a_check):
                           address=input("Enter your address: ")
                           if(len(address)==0):
                               print("\nMandatory Field.Please enter the address as home delivery has been selected.")
                               a_check=True
                           else:
                               a_check=False
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
                o_check=True
                while(o_check):
                    ID=input("\nEnter the ID whose status you wish to see: ")
                    if(len(ID)==0):
                        print("\nMandatory Field.Please enter the Order ID.")
                        o_check = True
                    else:
                        try:
                            ID=int(ID) 
                            y = is_present(df['Order ID'],ID)
                            if(y == True):
                                print("\nThe Status of the Order ID {} is: ".format(ID),df[df['Order ID']== ID]['Order Status'].values[0])
                                o_check=False
                            else:
                                print("\nIncorrect Order ID.Please Re-enter.")
                                o_check=True
                        
                        except(ValueError):
                             print("Only integer values are allowed.")
                             o_check=True
           
            else:
                if(k==0):
                    break;
                else:
                    print("\nThe option chosen is not available") 
       
       except(ValueError):
            print("No operation selected!")
        
        
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
   try:
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
   except(ValueError):
        print("No mode selected!")
        print("-----------Restarting the application----------------")
