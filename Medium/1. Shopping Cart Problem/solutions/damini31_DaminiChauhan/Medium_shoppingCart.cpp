#include <iostream>
#include<string.h>
using namespace std;
#include <bits/stdc++.h> 


void calculate(string x[],int y[],int n,int OS)
{
    
    map<string,int> cost{{"Samsung headset", 2000}, 
            {"MI headset", 1000},{"Apple Airpods", 12000},
            {"Boat headset", 2000},{ "Noise headset", 1500}}; 
            
    map<string,int> discount{{"Samsung headset", 1899}, 
            {"MI headset", 950},{"Apple Airpods", 0},
            {"Boat headset", 0},{ "Noise headset", 1399}}; 
            
    map<string,int> savings{{"Samsung headset", 101}, 
            {"MI headset", 50},{"Apple Airpods", 0},
            {"Boat headset", 0},{ "Noise headset", 101}};
            
   string b[]={"Samsung headset","MI headset","Apple Airpods","Boat headset","Noise headset"};
   int bill;
   int c=0,d=0;
     cout<<"\n----------------------------------------------------Bill-----------------------------------------------------------";
           cout<<"\nProduct               Quantity           Price(before discount)         Price(after discount)         Total Amount";
   for(int j=0;j<n;j++)
   {
        if(discount[x[j]]!=0)
          {
             c= discount[x[j]];
             d= d + c*y[j]; 
             cout<<"\n"<<x[j]<<"             "<<y[j]<<"                       Rs:"<<cost[x[j]]<<"                       Rs:"<<discount[x[j]]<<"                         Rs:"<<discount[x[j]]*y[j];  
           }
           else
           {
             c = cost[x[j]];
             d = d + c*y[j];
            cout<<"\n"<<x[j]<<"              "<<y[j]<<"                      Rs:"<<cost[x[j]]<<"                       Rs:"<<cost[x[j]]<<"                       Rs:"<<cost[x[j]]*y[j];  
           }
    }
            cout<<"\n------------------------------------------------------------------------------------------------------------------";
           int g=0;
                cout<<"\n"<<"Total amount(before tax):"<<"                               Rs:"<<d;
                cout<<"\n"<<"Tax(6%)"<<"                                                 Rs:"<<0.06*d;
           if(OS<50)
           {
             if(OS<=5)
             {
                 g=0;
                 cout<<"\nDelivery Fee Upto "<<OS<<"kms                                 Rs:"<<g;                                                                                                         
             }
             else if(OS<=20 and OS>5)
             {
                 g=30;
                 cout<<"\nDelivery Fee Upto "<<OS<<" kms                                Rs:"<<g;
             }
              else
             {
                 g=50;
                 cout<<"\nDelivery Fee Upto "<<OS<<" kms                                Rs:"<<g;
             }
             
             
           }
           else
           {
               g=0;
           }
                cout<<"\n"<<"Total amount to be paid:"<<"                               Rs:"<< d + (0.06*d) + g;
           int s=0;
           for(int j=0;j<n;j++)
           {
               s=s+(savings[x[j]] * y[j]);
           }
                cout<<"\nTotal money saved: "<<"                                     Rs:"<<s;
   
}
    


void calculate(string a[],int b[],int n,int distance);
int main()
{
  string name,phno,payment;
  string x[5];
  int y[5];
  int i=0;
  int n=0;
  int ch;
 
  string dummy;
  dummy=" ";
  cout<<"\n---------------Welcome   to   GadgetifyWithGSBlr-------------------";
  
  cout<<"\nEnter the customer's name ";
  getline(cin,name);
  cout<<"\nEnter the customer's Phone number";
  getline(cin,phno);
  cout<<"\nChoose the Payment method - (cash/card/online)";
  getline(cin,payment);
 
  cout<<"\nSelect items you want to purchase shopping item and it’s quantity\n";
  cout<<"\n-----------------------------LIST OF ITEMS-------------------------------\n";
  cout<<"\n";
  cout<<"\nProduct Name              Original Price        Discounted Price           Weight" ;
  cout<<"\nSamsung headset:             Rs.2000                Rs.1899                 150 g    \n";
  cout<<"\nMI headset:                  Rs.1000                Rs.950                  120 g    \n";
  cout<<"\nApple Airpods:               Rs.12000               No discount             150 g    \n";
  cout<<"\nBoat headset:                Rs.2000                No discount             150 g    \n";
  cout<<"\nNoise headset:               Rs.1500                Rs.1399                 120 g    \n";
 
 
  for(int i=0;i<5;i++)
  {
      cout<<"\nEnter Product Name: ";
      getline(cin,x[i]);
      cout<<x[i];
      cout<<"\nEnter the quantity :";
      cin>>y[i];
      cout<<y[i];
      n++;
      cout<<"\nDo you want to add more items?(press 0 to exit and 1 to add more items)";
      cin>>ch;
      cout<<"\n";
      getline(cin,dummy);
      if(ch==0)
      {
          break;
      }
  }
  
  for(int i=0;i<n;i++)
  {
    x[i].resize(x[i].size()-1);
  }
  
  
  string delivery,address;
  int distance;
  cout<<"\nTakeaway/Home delivery: ";
  getline(cin,delivery);
  cout<<delivery;
  delivery.resize(delivery.size()-1);
  int t = delivery.compare("Home delivery");
  if(t==0)
  {
      cout<<"\nAddress:";
      getline(cin,address);
      cout<<address;
      cout<<"\nDistance from shop to the delivery address in KM. (if Home delivery is selected)";
      cin>>distance;
      cout<<distance;
      if(distance>50)
      {
          cout<<"\n Home delivery not available for distance greater than 50 km.Only takeaway is available";
          cout<<"\n Do you want to proceed with the order.Press Y for yes and N for No ?";
          char k;
          cin>>k;
          cout<<k;
          if(k=='Y')
          {
                cout<<"\n**************GagdetifyWithGSBLr********************";
                cout<<"\n        Shop name: GadgetifyWithGSBlr       ";
                cout<<"\nShop address: 311/5 Akshay nagar, Bangalore, Karnataka,India";
                cout<<"\n     Shop contact no: +91 9988776655";
                cout<<"\n               Customer Name: "<<name;
                cout<<"\n               Phone Number: "<<phno;
                cout<<"\n               Payment method: "<<payment;
                calculate(x,y,n,distance);
            cout<<"\n------------------------------------------------------------------------------------------------------------------";
          }
          else
          {
           cout<<"\n-------------------------------------------------------------------";
           cout<<"\nThank you for visiting for us................";
           cout<<"\nHave a great day...............";
          }
        }
        else
        {
            cout<<"\n********************GagdetifyWithGSBLr*************************";
            cout<<"\n            Shop name: GadgetifyWithGSBlr       ";
            cout<<"\n    Shop address: 311/5 Akshay nagar, Bangalore, Karnataka,India";
            cout<<"\n     Shop contact no: +91 9988776655";
            cout<<"\n               Customer Name: "<<name;
            cout<<"\n               Phone Number: "<<phno;
            cout<<"\n               Payment method: "<<payment;
            calculate(x,y,n,distance);
            cout<<"\n---------------------------------------------------------------------------------------------------------------------";
            cout<<"\n Delivery Address: "<<address;
        }
    }
    else
    {
             cout<<"\n**********************************************GagdetifyWithGSBLr****************************************************";
             cout<<"\n                                        Shop name: GadgetifyWithGSBlr                                               ";
             cout<<"\n                                Shop address: 311/5 Akshay nagar, Bangalore, Karnataka,India";
             cout<<"\n                                         Shop contact no: +91 9988776655";
             cout<<"\nCustomer Name: "<<name;
             cout<<"\nPhone Number: "<<phno;
             cout<<"\nPayment method: "<<payment;
             calculate(x,y,n,distance);
             cout<<"\n------------------------------------------------------------------------------------------------------------------";
        
    }
 time_t my_time = time(NULL); 
 cout<<"\n                               Billing Date & Time:"<<ctime(&my_time);
             cout<<"-------------------------------------------Have A Great Day--------------------------------------------------------";
  
 
 return 0;
}