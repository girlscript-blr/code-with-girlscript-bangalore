def compute(Dict,List):
    items = List #list of all products with prices
    purch = Dict #purchased products
    prices = {} #contains purchased products with total prices 
    total_amt = 0 
    for k in purch.keys():
        if k==items[0][0].upper():
            a_price = int(items[0][1])
            a_quan = int(purch[k])
            prices[k] = (a_price*a_quan)
            total_amt+=(a_price*a_quan)
        elif k==items[1][0].upper():
            b_price = int(items[1][1])
            b_quan = int(purch[k])
            prices[k] = (b_price*b_quan)
            total_amt+=(b_price*b_quan)
        elif k==items[2][0].upper():
            c_price = int(items[2][1])
            c_quan = int(purch[k])
            prices[k] = (c_price*c_quan)
            total_amt+=(c_price*c_quan)
        elif k==items[3][0].upper():
            d_price = int(items[3][1])
            d_quan = int(purch[k])
            prices[k] = (d_price*d_quan)
            total_amt+=(d_price*d_quan)
        else:
            e_price = int(items[4][1])
            e_quan = int(purch[k])
            prices[k]= (e_price*e_quan)
            total_amt+=(e_price*e_quan)
        
    tax_amt = total_amt*0.06 #amount with 6%tax
    pay_amt = tax_amt+total_amt #final amount

    return prices,tax_amt,pay_amt
            

            

           



