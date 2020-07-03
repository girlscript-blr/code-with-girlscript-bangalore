import datetime
import os
save_path = os.getcwd()+'/bills/' #directory path

def bill(name, phno, paym, List, Dict, prices,taxamt, payamt):
    items = List #all items
    purch = Dict #purchased itesm
    tax_amt = taxamt #total tax
    final_amt = payamt #payable amount

    d = str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().day) #date
    t = str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute)+":"+str(datetime.datetime.now().second) #time
    
    complete_path = os.path.join(save_path,d+"-"+t+"_"+name+".txt") #file path

    file = open(complete_path,"w")
    file.write("\n")
    file.write("=============================================================")
    file.write("\n\t\t\t\t\tGADGETIFYWithGSBlr")
    file.write("\n\t\t311/5 Akshay nagar, Bangalore, Karnataka, India")
    file.write("\n\t\t\t\t\tCall +919988776655")
    file.write("\n\n\t\t\t\t\t\t\t\t\t\tDate: "+d+"\n\t\t\t\t\t\t\t\t\t\tTime:"+t+"")
    file.write("\nCustomer Name: "+str(name)+"")
    file.write("\nCustomer PhoneNo.: "+str(phno)+"")
    file.write("\nPayment method: "+str(paym)+"")
    file.write("\n=============================================================")
    file.write("\n\t\tITEM\tQUANTITY\tPRICE\tTOTAL")                     
    file.write("\n-------------------------------------------------------------")

    for key in purch.keys():
        if key=="A":
            file.write(str("\n\t\t"+str(key)+"\t\t "+str(purch['A'])+" \t\t "+str(items[0][1])+" \t\t "+str(prices['A'])))
        elif key=='B':
            file.write(str("\n\t\t"+str(key)+"\t\t "+str(purch['B'])+" \t\t "+str(items[1][1])+" \t\t "+str(prices['B'])))
        elif key=='C':
            file.write(str("\n\t\t"+str(key)+"\t\t "+str(purch['C'])+" \t\t "+str(items[2][1])+" \t\t "+str(prices['C'])))
        elif key=='D':
            file.write(str("\n\t\t"+str(key)+"\t\t "+str(purch['D'])+" \t\t "+str(items[3][1])+" \t\t "+str(prices['D'])))
        else:
            file.write(str("\n\t\t"+str(key)+"\t\t "+str(purch['E'])+" \t\t "+str(items[4][1])+" \t\t "+str(prices['E'])))

    file.write("\n\n-------------------------------------------------------------")
    file.write("\n\t\t\t\t\tTotal tax : Rs. "+str(tax_amt))
    file.write("\n\t\t\t\t\tFinal amount : Rs. "+str(final_amt))
    file.write("\n\n-------------------------------------------------------------")
    file.write("\n\n\t\t\tThank You "+name+" for your shopping!")
    file.write("\n=============================================================")
    file.close()

    


