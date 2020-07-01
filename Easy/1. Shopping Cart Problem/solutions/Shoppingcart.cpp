#include<iostream>
#include<cmath>
#include<ctime>//Using for time 
using namespace std;
class GadgetifyWithGSBlr
{
private:
int phonenumber;
char Name[15];
int paymentmethod;
int items;
int quantity;
int amount;
int tax;
int x;
public:
//GET PHONE NUMBER  FROM USER
int getphonenumber()
{
    cout<<"|                                     Enter your 10 digit Phone Number :";
cin>>phonenumber;
if(phonenumber>9999999999)
cout<<"|                                    Invalid Number                              |"<<endl;
return 0;
}
//GETTING NAME FROM USER
char getname()
{
    cout<<"|                                      Enter Your Name : ";
    cin>>Name;
}
// GET PAYMENT METHOD USED BY USER
int getpaymentmethod()
{
    cout<<"----------------------------------------------------------------------------------------------------------"<<endl;
    cout<<"|                            Select the Payment Method                                                    |"<<endl;
    cout<<"|                                Select Option (1/2/3):                                                   |"<<endl;
    cout<<"|                                  PRESS 1 for Cash                                                       |"<<endl;
    cout<<"|                                  PRESS 2 for Card                                                       |"<<endl;
    cout<<"|                                  PRESS 3 for Online                                                     |"<<endl;
    cout<<"-----------------------------------------------------------------------------------------------------------"<<endl;
    cin>>paymentmethod;
  if(paymentmethod>3)
  {
  cout<<"*                                     Invalid input given                                                    *"<<endl;
  cout<<"*                                          TRY AGAIN                                                         *"<<endl;
  cout<<"*                                   Select Payment method 1/2/3 :";
   cin>>paymentmethod;
   cout<<endl;
  }
  cout<<"|                                 *PAYMENT SUCCESSFUL*                                                      |"<<endl;
  return 0;
}
//GET THE LIST AND AMOUNT OF ITEMS SELECTED
int getitems()
{
    cout<<"-------------------------------------------------------------------------------------------------------------"<<endl;
    cout<<"|                                           ITEMS In Store                                                  |"<<endl;
    cout<<"|                                 1.Earphones         : Rs.1200/-per                                        |"<<endl;
    cout<<"|                                 2.Mobile Phone      : Rs.5600/-per                                        |"<<endl;
    cout<<"|                                 3.Laptop            : Rs.50,000/-per                                      |"<<endl;
    cout<<"|                                 4.Tablet            : Rs.3000/-per                                        |"<<endl;
    cout<<"|                                 5.Charger           : Rs.560/-per                                         |"<<endl;
    cout<<"-------------------------------------------------------------------------------------------------------------"<<endl;
    cout<<"                                  Select ANY 1  Item No. :";
    cin>>x;
    if(x>=6)
    {
    cout<<"*                                 Value enetered is not in list\n                                             *"<<endl;
    cout<<"*                                        TRY AGAIN                                                            *"<<endl;
    cout<<"*                                 Select ANY 1  Item No. :";
    cin>>x;
    cout<<endl;
    }
    switch (x)
    {
    case 1:   
    cout<<"->                                  Quantity Required : ";
                 cin>>quantity;
                 amount=1200*quantity;
                 cout<<"\nItem Cost : "<<amount<<endl;
                 tax=6%amount;
                 tax=tax*quantity;
                  cout<<"Total Tax :"<<tax<<endl;
                 amount=tax+amount;
                 cout<<"Total Bill Including Taxes :"<<amount<<endl;
                 break;
    case 2:     
    cout<<"->                                  Quantity Required : ";
                 cin>>quantity;
                 amount=5600*quantity;
                 cout<<"\nItem Cost : "<<amount<<endl;
                 tax=6%amount;
                  tax=tax*quantity;
                   cout<<"Total Tax :"<<tax<<endl;
                 amount=tax+amount;
                 cout<<"Total Bill Including Taxes :"<<amount<<endl;
                 break;
   
    case 3:      
    cout<<"->                                  Quantity Required : ";
                 cin>>quantity;
                 amount=50000*quantity;
                 cout<<"\nItem Cost : "<<amount<<endl;
                 tax=6%amount;
                  tax=tax*quantity;
                   cout<<"Total Tax :"<<tax<<endl;
                 amount=tax+amount;
                 cout<<"Total Bill Including Taxes :"<<amount<<endl;
                 break;
   
    case 4:      
    cout<<"->                                   Quantity Required : ";
                 cin>>quantity;
                 amount=3000*quantity;
                 cout<<"\nItem Cost : "<<amount<<endl;
                 tax=6%amount;
                  tax=tax*quantity;
                   cout<<"Total Tax :"<<tax<<endl;
                 amount=tax+amount;
                 cout<<"Total Bill Including Taxes :"<<amount<<endl;
                 break;
  
    case 5:      
   cout<<"->                                  Quantity Required : ";
                 cin>>quantity;
                 amount=560*quantity;
                 cout<<"\nItem Cost : "<<amount<<endl;
                 tax=6%amount;
                  tax=tax*quantity;
                  cout<<"Total Tax :"<<tax<<endl;
                 amount=tax+amount;
                 cout<<"Total Bill Including Taxes :"<<amount<<endl;
                 break;
  

    }
    return 0;
}

};//CLASS ENDS
int main()
{
  GadgetifyWithGSBlr g1;//INTIALIZING OBJECT OF CLASS

  cout<<"                      ________________________________________________________________    "<<endl;
  cout<<"                                      Gadget ify With GSBlr"<<endl;
  cout<<"                                   Address: 311/5 Akshay nagar,"<<endl;
  cout<<"                                   Bangalore, Karnataka, India "<<endl;
  cout<<"                                   Contact no: +91 9988776655"<<endl;
 time_t tt;
 struct tm * ti;
 time (&tt);
 ti = localtime(&tt); 
  cout<<"                                   Bought On :"<<asctime(ti)<<endl;
  cout<<"                       ________________________________________________________________"<<endl;
  g1.getname();//CALLING NAME FROM USER
  g1.getphonenumber();// CALLING PHONE NUMBER FROM USER
  g1.getitems();// GET THE USER TO SELECT ANY 1 ITEM AND DISPLAYING TOTAL AMOUNT TO BE PAID
  g1.getpaymentmethod();//GETTING PAYMENT METHOD FOR USER 
    return 0;
}
