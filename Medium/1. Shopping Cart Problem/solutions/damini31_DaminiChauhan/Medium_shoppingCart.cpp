#include <iostream>
#include<string.h>
using namespace std;
#include <bits/stdc++.h>


void calculate(int x[],int y[],int n,int OS)
{
    map<int,string> Product{{101,"Samsung headset"},
            {102,"MI headset"},{108,"Apple Airpods"},
            {109,"Boat headset"},{110, "Noise headset"}};

    map<int,int> cost{{101, 2000},
            {102, 1000},{108, 12000},
            {109, 2000},{ 110, 1500}};

    map<int,int> discount{{101, 1899},
            {102, 950},{108, 0},
            {109, 0},{110, 1399}};

    map<int,int> savings{{101, 101},
            {102, 50},{108, 0},
            {109, 0},{110, 101}};

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
             cout<<"\n"<<Product[x[j]]<<"             "<<y[j]<<"                       Rs:"<<cost[x[j]]<<"                       Rs:"<<discount[x[j]]<<"                         Rs:"<<discount[x[j]]*y[j];
           }
           else
           {
             c = cost[x[j]];
             d = d + c*y[j];
            cout<<"\n"<<Product[x[j]]<<"              "<<y[j]<<"                      Rs:"<<cost[x[j]]<<"                       Rs:"<<cost[x[j]]<<"                       Rs:"<<cost[x[j]]*y[j];
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



void calculate(int a[],int b[],int n,int distance);
int main()
{
  string name,phno,payment;
  int x[5];
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

  cout<<"\n Select shopping item by their product ID and enter it’s quantity\n";
  cout<<"\n-----------------------------LIST OF ITEMS-------------------------------\n";
  cout<<"\n";
  cout<<"\nProduct ID      Product Name              Original Price        Discounted Price           Weight" ;
  cout<<"\n101              Samsung headset             Rs.2000                Rs.1899                 150 g    \n";
  cout<<"\n102              MI headset                  Rs.1000                Rs.950                  120 g    \n";
  cout<<"\n108              Apple Airpods               Rs.12000               No discount             150 g    \n";
  cout<<"\n109              Boat headset                Rs.2000                No discount             150 g    \n";
  cout<<"\n110              Noise headset               Rs.1500                Rs.1399                 120 g    \n";

  cout<<"\n Please enter the product names as it is:";

  for(int i=0;i<5;i++)
  {
      cout<<"\nEnter Product ID: ";
      cin>>x[i];
      cout<<"\nEnter the quantity :";
      cin>>y[i];
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



  string address;
  int t,distance;
  cout<<"\nTakeaway/Home delivery.Press 1 for Takeaway and 0 for Home delivery.";
  cin>>t;
  getline(cin,dummy);
  if(t==0)
  {
      cout<<"\nAddress:";
      getline(cin,address);
      cout<<"\nDistance from shop to the delivery address in KM. (if Home delivery is selected)";
      cin>>distance;
      if(distance>50)
      {
          cout<<"\n Home delivery not available for distance greater than 50 km.Only takeaway is available";
          cout<<"\n Do you want to proceed with the order.Press Y for yes and N for No ?";
          char k;
          cin>>k;
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
