from user import entry
from compute import compute
from invoice import bill

products = [['A','1200'],['B','600'],['C','200'],['D','800'],['E','300']]

if __name__ == "__main__":
    
    name, phno, paym, purch_item = entry(products)#taking inputs from user
    #print(purchased)
    prices, tax_amount, f_amount = compute(purch_item, products)#computing prices
    #print(prices)
    #print(tax_amount)
    #print(f_amount)
    bill(name, phno, paym, products, purch_item, prices, tax_amount, f_amount)#generates an invoice bill
    