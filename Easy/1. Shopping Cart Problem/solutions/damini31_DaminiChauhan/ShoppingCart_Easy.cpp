#include <iostream>
#include<string.h>
using namespace std;
#include <bits/stdc++.h> 

void calculate(string a,int f)
{
    map<string,int> cost{{"Samsung wireless headset", 2000}, 
            {"MI wireless headset", 1000},{"Apple Airpods", 12000},
            {"Boat headset", 2000},{ "Noise headset", 1500}}; 
   
   string b[]={"Samsung wireless headset","MI wireless headset","Apple Airpods","Boat headset","Noise headset"};
  
   
   int x,n_bill,t_bill;
   for(int i=0;i<5;i++)
   {
       int x = a.compare(b[i]);
       if(x==0)
       {
           n_bill = f * cost[a];
           /*6% on the total bill */
           t_bill= n_bill + n_bill*0.06;
           cout<<"\n-------------------Amount to be paid---------------------";
           cout<<"\n"<<"Product"<<"                      "<<"Quantity"<<"    "<<"Amount per piece";
           cout<<"\n----------------------------------------------------------";
           cout<<"\n"<<a<<"            "<<f<<"          "<<cost[a];
           cout<<"\n";
           cout<<"\nTotal amount(before tax):"<<"         "<<n_bill;
           cout<<"\n6% tax on the above amount:"<<"       "<<n_bill*0.06;
           cout<<"\nTotal amount to be paid:"<<"          "<<t_bill;
           break;
          
       }
       
   } 

}

void calculate(string a,int b);
int main()
{
  string name,phno,payment,x;
  int y;
  
  cout<<"\n---------------Welcome   to   GadgetifyWithGSBlr-------------------";
  
  cout<<"\nEnter the customer's name ";
  getline(cin,name);
  cout<<"\nEnter the customer's Phone number";
  getline(cin,phno);
  cout<<"\nChoose the Payment method - (cash/card/online)";
  getline(cin,payment);
  cout<<"\nSelect a single shopping item and it’s quantity\n";
  getline(cin,x);
  cin>>y;
  cout<<"\n------------LIST OF ITEMS-----------------\n";
  cout<<"1. Samsung wireless headset: Rs.2000\n";
  cout<<"2. MI wireless headset: Rs.1000\n";
  cout<<"3. Apple Airpods: Rs.12000\n";
  cout<<"4. Boat headset: Rs.2000\n";
  cout<<"5. Noise headset: Rs.1500\n";
  
  
  
  /*removing space from the last character*/
  if(!x.empty())
  {
      x.resize(x.size()-1);
  }
 
  cout<<"\n---------------------Total Bill----------------------";
  cout<<"\n**************GagdetifyWithGSBLr********************";
  cout<<"\n        Shop name: GadgetifyWithGSBlr       ";
  cout<<"\nShop address: 311/5 Akshay nagar, Bangalore, Karnataka,India";
  cout<<"\n     Shop contact no: +91 9988776655";
  cout<<"\n               Customer Name: "<<name;
  cout<<"\n               Phone Number: "<<phno;
  cout<<"\n               Payment method: "<<payment;
  cout<<"\n               Product: "<<x;
  cout<<"\n               Product Quantity: "<<y;
  calculate(x,y);

 time_t my_time = time(NULL); 
 cout<<"\n\nBilling Date & Time:"<<ctime(&my_time);
 cout<<"----------------Have A Great Day------------------------";
   

 return 0;
}