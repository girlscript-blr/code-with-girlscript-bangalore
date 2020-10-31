#include <iostream>
#include<string.h>
using namespace std;
#include <bits/stdc++.h>

void calculate(int a,int f)
{
    map<int,int> Product{{101, 2000},
            {102, 1000},{108, 12000},
            {109, 2000},{110, 1500}};

    map<int,string> name{{101,"Samsung wireless headset"},
            {102,"MI wireless headset"},{108,"Apple Airpods"},
            {109,"Boat headset"},{110,"Noise headset"}};

   string b[]={"Samsung wireless headset","MI wireless headset","Apple Airpods","Boat headset","Noise headset"};


   int x,n_bill,t_bill;


           n_bill = f * Product[a];
           /*6% on the total bill */
           t_bill= n_bill + n_bill*0.06;
           cout<<"\n-------------------Amount to be paid---------------------";
           cout<<"\n"<<"Product"<<"                      "<<"Quantity"<<"    "<<"Amount per piece";
           cout<<"\n----------------------------------------------------------";
           cout<<"\n"<<name[a]<<"            "<<f<<"          "<<Product[a];
           cout<<"\n";
           cout<<"\nTotal amount(before tax):"<<"         "<<n_bill;
           cout<<"\n6% tax on the above amount:"<<"       "<<n_bill*0.06;
           cout<<"\nTotal amount to be paid:"<<"          "<<t_bill;



   }

void calculate(int a,int b);
int main()
{
  string name,phno,payment;
  int x,y;

  cout<<"\n---------------Welcome   to   GadgetifyWithGSBlr-------------------";

  cout<<"\nEnter the customer's name ";
  getline(cin,name);
  cout<<"\nEnter the customer's Phone number";
  getline(cin,phno);
  cout<<"\nChoose the Payment method - (cash/card/online)";
  getline(cin,payment);

  cout<<"\n------------LIST OF ITEMS-----------------\n";
  cout<<"\nProduct ID         Product Name               Price\n";
  cout<<"101                Samsung wireless headset:    Rs.2000\n";
  cout<<"102                MI wireless headset:         Rs.1000\n";
  cout<<"108                Apple Airpods:               Rs.12000\n";
  cout<<"109                Boat headset:                Rs.2000\n";
  cout<<"110                Noise headset:               Rs.1500\n";

  cout<<"\nSelect a single shopping item by the product ID and it’s quantity\n";
  cin>>x;
  cin>>y;

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
