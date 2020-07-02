class shoplist:
    def __init__(self, sno, name, price, disc, wt):
        self.sno = sno
        self.name = name
        self.price = price
        self.disc = disc
        self.wt =wt
a=[]
s=[1,2,3,4,5,6,7,8]
n=["Boat Headphones","Santoor soap","Himalaya facewash","Notebook","camelin box", "cello pen", "apsara pencil", "camel eraser"]
p=[1000,20,50,40,80,10,5,6,3]
d=[800,15,40,30,70,8,5,6,3]
w=[200,100,100,100,300,10,10,5]
i=0
print("GadgetifyWithGSBlr")
print("311/5 Akshay nagar, Bangalore, Karnataka, India")
print("Contact:+91 9988776655")
print("Shopping list")
while(i<8):
    z=shoplist(s[i],n[i],p[i],d[i],w[i])
    a.append((z.sno,z.name,z.price,z.disc,z.wt))
    i+=1
i=0
while(i<len(a)):
    print('Slno:' + str(a[i][0])+ '  '+'name:'+str(a[i][1]) + '  '+ 'original price:Rs'+str(a[i][2])+ '  '+ 'discount price:Rs'+str(a[i][3])+ '  '+'money saved:Rs'+str(int(a[i][2])-int(a[i][3]))+'  '+ 'weight:'+str(a[i][4])+'g')
    i+=1
name=input("Enter your name:")
pno=input("Enter your Phone no:")
pay=input("Payment method: 1.cash, 2.card, 3.online")
l=[]
q=[]
ch='y'
while(ch=='y' or ch=='Y'):
    c=input('Enter the Slno of Commodity you want to buy:')
    l.append(c)
    q.append(input('Quantity:'))
    ch=input('Do you want to shop more? y:yes n:no')
i= 0
sum=0
dicount=0
while(i<len(l)):
    sum+=int(a[int(l[i])-1][3])*int(q[i])
    dicount+=(int(a[int(l[i])-1][2])-int(a[int(l[i])-1][3]))*int(q[i])
    i+=1
take=input("Delivery option 1.Takeaway 2.Home Delivery")
if(int(take)==2):
    dist=int(input("Enter the distance from shop in km"))
    if(dist<=5):
        pass
    elif(dist<=20):
        sum+=30
    elif(dist<=50):
        sum+=60
    else:
        print("Sorry, we do not deliver there, sincere apologies. Please proceed with takeaway")
        take=input("Take away? 1.Yes 2. No, Thanks, I dont want to continue with the order")
        if(int(take)==1):
            pass
        else:
            exit(0)
if(int(take)==2 and dist<=50):
    add = input("Enter your address")
cal = sum+dicount
cal+=cal*0.06
sum+=0.06*sum
print("GadgetifyWithGSBlr")
print("311/5 Akshay nagar, Bangalore, Karnataka, India")
print("Contact:+91 9988776655")
print("Bill")
i=0
while(i<len(l)):
    print('Name: ' +str(a[int(l[i])-1][1])+ '  '+ 'Net price: Rs' +str(a[int(l[i])-1][3]) + '  '+ 'Quantity: '+str(q[i])+ '  Total: Rs' +str(a[int(l[i])-1][3]*int(q[i])))
    i+=1
print('Total amount Rs'+str(round(sum,2)))
print('You saved Rs'+str(round(cal-sum,2))+'!')
