def entry(List):
    items= List
    purch = {}
    name = input("\nEnter your name : ") #name
    print("\nHey "+name+". Welcome to GadgetifyWithGSBlr.")
    phno = input("\nEnter your phone no. :") #phone number
    paym = input("\nPayment Method (cash/card/online) :") #payment method
    
    print("\nAvailable products in our store")
    print("----------------------------")
    print("PRODUCT\t\tPRICE")
    print("----------------------------")
    for i in range(5):
            print(items[i][0],"\t",items[i][1])
    print("----------------------------")
    
    flag="Y"
    
    while flag.upper()=="Y":

        product = input("\nWhat do you want to buy ? ").upper()
        
        if product==items[0][0].upper() or product==items[1][0].upper() or product==items[2][0].upper() or product==items[3][0].upper() or product==items[4][0].upper():
            try:
                quantity = int(input("\nHow many do you want to buy ? "))#quantity
            except:
                print('\n\tPlease enter an integer!')
                continue
            
            if product==items[0][0].upper():
                purch[product]=quantity
            elif product==items[1][0].upper():
                purch[product]=quantity
            elif product==items[2][0].upper():
                purch[product]=quantity
            elif product==items[3][0].upper():
                purch[product]=quantity
            else:
                purch[product]=quantity
            
            flag = input("\nDo you want to buy anything else ?(Y/N) ")

        else:
            
            print("\nSorry! Choose only from the below")
            print("----------------------------")
            print("PRODUCT\t\tPRICE")
            print("----------------------------")
            for i in range(5):
                    print(items[i][0],"\t",items[i][1])
            print("----------------------------")
    
    print('\nThank You '+name+' for shopping !')
    return name, phno, paym, purch




