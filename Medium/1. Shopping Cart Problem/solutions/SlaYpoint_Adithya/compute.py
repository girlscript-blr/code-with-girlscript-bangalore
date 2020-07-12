def compute(items,purch,mode,d):
    keys = [k for k in items.keys()] #item names
    prc = [p for p in items.keys()[0]] #prices
    dis = [d for d in items.keys()[1]] #discounts
    prices = {} #contains purchased products with total prices 
    saved  = {}
    ship_chrg = 0 #shipping charge
    total_amt = 0 
    for k in keys:
        if k==keys[0].upper():
            a_quan = int(purch[k])
            a_price = int(prc[0])
            prices[k] = (a_price*a_quan)
            if dis[0]!=0:
                saved[k] = prices[k]-(dis[0]*a_quan)
                total_amt+=(dis[0]*a_quan)
            else:    
                total_amt+=(a_price*a_quan)
        elif k==keys[1].upper():
            b_quan = int(purch[k])
            b_price = int(prc[1])
            prices[k] = (b_price*b_quan)
            if dis[1]!=0:
                saved[k] = prices[k]-(dis[1]*b_quan)
                total_amt+=(dis[1]*b_quan)
            else:    
                total_amt+=(b_price*b_quan)
        elif k==keys[2].upper():
            c_quan = int(purch[k])
            c_price = int(prc[2])
            prices[k] = (c_price*c_quan)
            if dis[2]!=0:
                saved[k] = prices[k]-(dis[2]*c_quan)
                total_amt+=(dis[2]*c_quan)
            else:    
                total_amt+=(c_price*c_quan)
        elif k==keys[3].upper():
            d_quan = int(purch[k])
            d_price = int(prc[3])
            prices[k] = (d_price*d_quan)
            if dis[3]!=0:
                saved[k] = prices[k]-(dis[3]*d_quan)
                total_amt+=(dis[3]*d_quan)
            else:    
                total_amt+=(d_price*d_quan)
        else:
            e_quan = int(purch[k])
            e_price = int(prc[4])
            prices[k] = (e_price*e_quan)
            if dis[4]!=0:
                saved[k] = prices[k]-(dis[4]*e_quan)
                total_amt+=(dis[4]*a_quan)
            else:    
                total_amt+=(e_price*e_quan)
        
    tax_amt = total_amt*0.06 #amount with 6%tax

    if mode.upper()=='H':
        if d<=5:
            ship_chrg=0
        elif d<=30:
            ship_chrg=30
        elif d<=50:
            ship_chrg=60

    pay_amt = tax_amt+total_amt+ship_chrg #final amount

    return prices,saved,tax_amt,ship_chrg,pay_amt
            
    
