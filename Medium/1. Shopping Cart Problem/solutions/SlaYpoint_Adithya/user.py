def entry(Dict):
    items = Dict
    keys = [k for k in items.keys()]
    purch = {}    
    name = input("\nEnter your name : ") #name
    print("\nHey "+name+". Welcome to GadgetifyWithGSBlr.")
    phno = input("\nEnter your phone no. :") #phone number
    paym = input("\nPayment Method (cash/card/online) :") #payment method
    
    print("\nAvailable products in our store")
    print("--------------------------------------------------------")
    print("PRODUCT\t\tPRICE\t\tDISCOUNT\t\tWEIGHT")
    print("----------------------------")
    for key in keys:
            print(key,"\t  ",items[key]['prc'],"\t\t",items[key]['dis'],"\t\t",items[key]['w'])
    print("--------------------------------------------------------")
    
    flag="Y"
    
    while flag.upper()=="Y":

        product = input("\nWhat do you want to buy ? ").upper()
        
        if product in keys:
            try:
                quantity = int(input("\nHow many do you want to buy ? "))#quantity
            except:
                print('\n\tPlease enter an integer!')
                
            if product==keys[0].upper():
                purch[product]=quantity
            elif product==keys[1].upper():
                purch[product]=quantity
            elif product==keys[2].upper():
                purch[product]=quantity
            elif product==keys[3].upper():
                purch[product]=quantity
            else:
                purch[product]=quantity
            
            flag = input("\nDo you want to buy anything else ?(Y/N) ")

        else:
            print("\nSorry! Choose only from the below")
            print("--------------------------------------------------------")
            print("PRODUCT\t\tPRICE\t\tDISCOUNT\t\tWEIGHT")
            print("--------------------------------------------------------")
            for key in keys:
                    print(key,"\t  ",items[key]['prc'],"\t\t",items[key]['dis'],"\t\t",items[key]['w'])
            print("----------------------------")
           
    dist = 0 #distance
    add = "" #address
    flag = "Y"
    while flag.upper()=="Y":
        mode = input("\nTakeaway(T)/Home delivery(H) ? ")
        if mode.upper()=='H':
            try:
                dist = int(input("\nHow far are we from you(in KM) ?"))
                if dist > 50:
                    print("\nSorry ! we dont provide home delivery to this place.")
                    continue
            except:
                print("\n\tPlease enter an integer")
            add = input("\nYour Address: ")
        flag = "N"    

        print('\n\nThank You '+name+' for shopping !')

    return name, phno, paym, purch, mode, dist, add

'''
if __name__=="__main__":
    products = {
    'A': {'prc':1200,'dis':899,'w':150},
    'B': {'prc':800,'dis':0,'w':110},
    'C': {'prc':200,'dis':130,'w':140},
    'D': {'prc':600,'dis':499,'w':120},
    'E': {'prc':300,'dis':0,'w':130}
}
    name, phno, paym, purch, mode, dist, add = entry(products)
'''