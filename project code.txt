
rice=0
dal=0
special_item={1:0 , 2:0 ,3:0 ,4:0 ,5:0 ,6:0 ,7:0,8:0,9:0}
gender_list=[0,0,0]
person=[0,0,0,0,0,0]
set_data=set()
print("enter number of people")
n=int(input())            
for i in range(n):
  print("enter details for person:",i+1)
  aadhar=int(input("enter aadhar number "))      

  name=input("enter name ")                 
    
  g=int(input("enter 1 for male, 2 for female ,3 for other "))
  gender(g)

  age=int(input("enter valid age "))      
  data(aadhar,name,gender,age)
 
  r=int(input("enter amount(in grams) of rice he/she eats in a day "))     
  rice+=r

  d=int(input("enter amount(in grams) of dal he/she eats in day "))     
  dal+=d


  print("select enter any two number from list(one by one) for choosing special item ")
  if age<2:
    print("for cerlac->1 , for amul powder->2 ,for Nandini Milk Tetrapack->3 ")
    x=int(input())
    y=int(input())
    special_item[x]+=1
    special_item[y]+=1
    person[0]+=1
  elif age>=2 and age<18:
    print("for Nandini Milk Tetrapack->3, for Bread->4 , for Tiger/Parle G->5 , for canned fruits->6 , for canned veggies->7 ")
    x=int(input())
    y=int(input()) 
    special_item[x]+=1
    special_item[y]+=1
    person[1]+=1
  elif age>=70:
    print("for Nandini Milk Tetrapack->3, for canned fruits->6 , for canned veggies->7, for medicine pack->8 ")
    x=int(input())
    y=int(input())
    special_item[x]+=1
    special_item[y]+=1
    person[2]+=1
  elif (age>18 and age<70) and (g==2):
    print("for Nandini Milk Tetrapack->3, for canned fruits->6 , for canned veggies->7, for calcium sandoz tablet->9 ")
    x=int(input())
    y=int(input())
    special_item[x]+=1
    special_item[y]+=1
    person[3]+=1
  elif (age>18 and age<70) and (g==1):
    print("for Nandini Milk Tetrapack->3, for canned fruits->6 , for canned veggies->7 ")
    x=int(input())
    y=int(input())
    special_item[x]+=1
    special_item[y]+=1
    person[4]+=1
  elif (age>18 and age<70) and (g==3):
    print("for Nandini Milk Tetrapack->3, for canned fruits->6 , for canned veggies->7, for calcium sandoz tablet->9 ")
    x=int(input())
    y=int(input())
    special_item[x]+=1
    special_item[y]+=1
    person[5]+=1
output(rice,dal)





def output(rice,dal):
  rice=rice/1000
  dal=dal/1000
  print("Person Info:")
  print("_______________________________________________________________________")
  print("         Age Group                      |           No. of people    ")
  print("_______________________________________________________________________")
  print(f" Infants: Below 2years                  |               {person[0]}            ") 
  print("_______________________________________________________________________")
  print(f" Children: Between 3 to 18 years        |               {person[1]}            ")
  print("_______________________________________________________________________")
  print(f" Old Age: Above 70 years                |               {person[2]}            ")
  print("_______________________________________________________________________")
  print(f" Adult Female: Between 18 to 69 years   |               {person[3]}            ") 
  print("_______________________________________________________________________")
  print(f" Adult Male: Between 18 to 69 years     |               {person[4]}            ") 
  print("_______________________________________________________________________")
  print(f" Adult Other: Between 18 to 69 years    |               {person[5]}            ") 
  print("_______________________________________________________________________")

  print()
  print("Food Info:")
  print("__________________________________________________________________")
  print("         Food Item                 |        Required Qunatity     ")
  print("__________________________________________________________________")
  print(" Rice in Kg per day                |          {:.3f}".format(round(rice, 2))           )
  print("__________________________________________________________________")
  print(" Dal in Kg per day                 |          {:.3f}".format(round(dal, 2))             )
  print("__________________________________________________________________")
  print(f" Cerelac                           |          {special_item[1]}                  ")
  print("__________________________________________________________________")
  print(f" Amul Powder                       |          {special_item[2]}                  ")
  print("__________________________________________________________________")
  print(f" Nandini Milk TetraPacks           |          {special_item[3]}                  ")
  print("__________________________________________________________________")
  print(f" Breads                            |          {special_item[4]}                  ")
  print("__________________________________________________________________")
  print(f" Tiger/Parle G                     |          {special_item[5]}                  ")
  print("__________________________________________________________________")
  print(f" Canned Veggies                    |          {special_item[7]}                  ")
  print("__________________________________________________________________")
  print(f" Canned Fruits                     |          {special_item[6]}                  ")
  print("__________________________________________________________________")
  print(f" Medicine Packs                    |          {special_item[8]}                  ")
  print("__________________________________________________________________")
  print(f" Calcium Sandoz Tablets            |          {special_item[9]}                  ")
  print("__________________________________________________________________")


def gender(x):
  if x==1:
    gender_list[0]+=1
  if x==2:
    gender_list[1]+=1
  if x==3:
    gender_list[2]+=1


def data(aadhar,name,gender,age):
  gen=""
  if aadhar not in set_data:
    if gender==1:
      gen="Male"
    elif gender==2:
      gen="Female"
    elif gender==3:
      gen="Other"
    set_data.add((aadhar,name,gen,age))
  return


