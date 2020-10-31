//Solution of the Shopping Cart Medium Problem

#include <iostream>
#include <stdio.h>
#include <string.h>
#include <ctime>

using namespace std;

class GadgetifyWithGSBlr
{
    public :
    void catalog()
    {
      cout<<"\t Welcome to our shop:"<<endl;
      cout<<"The catalog is as follows: "<<endl;
      cout<<"1.Name: Basshead Earphones, Original Price: Rs. 1200, Discount price: Rs. 899, Weight: 150g"<<endl ; 
	  cout<<"2.Name: Bluetooth Computer Mouse, Original Price: Rs. 600, Discount price: Rs. 499, Weight: 120g"<<endl; 
	  cout<<"3.Name: Bluetooth Headphones, Original Price: 1600, Weight: 400g"<<endl;
	  cout<<"4. Name: Fast Mobile Charger, Original Price: 1400, Weight: 500g"<<endl ;
	  cout<<"5. Name: Smartband, Original Price: 2200, Weight: 50g "<<endl;
     }
};  

struct elements
{
      int s_no ;
      int quantity;
      int price;
      string name;
};

char customer_name[100];
char phone_no[15];
char payment_method[25];
int method = 0;
double tax_amount = 0.0;
double total_price = 0.0;
double to_be_paid = 0.0;
double del_price = 0.0;
int km;
char address[200];
int i;
int n ;

int main()
{
    GadgetifyWithGSBlr O1;
    O1.catalog();
      // Input
      cout<<"Please enter your name "<<endl;
      cin.get(customer_name , 100);cin.ignore();
      cout<<"Please enter your mobile number "<<endl;
      cin.get(phone_no , 20);cin.ignore();
      cout<<"Please enter payment method (cash/card/online)"<<endl;
      cin.get(payment_method , 25);cin.ignore();
     
      cout<<"Enter the number of items you want to buy \n";
      cin>>n;cin.ignore();
      struct elements e1[n];
      for(i=0;i<n;i++)
      {
      cout<<"Please enter the serial number of your selected item: \n";
      cin>>e1[i].s_no;cin.ignore();
      cout<<"Quantity \n";
      cin>>e1[i].quantity;cin.ignore();
      
            if(e1[i].s_no == 1)
            {
                e1[i].price = 899;
                e1[i].name.assign("Basshead Earphones");
                cout<<"You saved total Rs. "<<e1[i].quantity*301<<" on this product \n"; 
            }
            else if(e1[i].s_no == 2)
            {
                 e1[i].price = 499;
                 e1[i].name.assign("Bluetooth Computer Mouse");
                 cout<<"You saved total Rs. "<<e1[i].quantity*101<<" on this product \n"; 
            }
            else if(e1[i].s_no == 3)
            {
            e1[i].price = 1600;
            e1[i].name.assign("Bluetooth Headphones");
            }
            else if(e1[i].s_no == 4)
            {
            e1[i].price = 1400;
            e1[i].name.assign("Fast Mobile Charger");
            }
            else if(e1[i].s_no == 5)
            {
            e1[i].price = 2200;
            e1[i].name.assign("Smartband");
            }
            else
            e1[i].price = 0;
          
        total_price += e1[i].price * e1[i].quantity; 
      }   
       
      cout<<"Please select 1 for Takeaway and 2 for Home Delivery"<<endl;
      cin>>method;cin.ignore();
      if(method == 2)
      {
          cout<<"Enter the distance from shop to the delivery address in KM \n";
          cin>>km;cin.ignore();
          
          if(km <= 5)
          {
          del_price = 0;
          cout<<"Enter the Shipping address";
          cin>>address;cin.ignore();
          }
          else if(km<=20)
          {
          del_price = 30;
          cout<<"Enter the Shipping address";
          cin>>address;cin.ignore();
          }
          else if(km <= 50)
          {
          del_price = 60;
          cout<<"Enter the Shipping address \n";
          cin>>address;cin.ignore();
          }
          else
          cout<<"The shop doesn’t provide home delivery to addresses more than 50KM away";
       }
      
      tax_amount = total_price * 0.06;
      to_be_paid = tax_amount + total_price + del_price;
      
      
    // Display
   
    // current date/time based on current system
      time_t now = time(0);
    // convert now to string form
      char* dt = ctime(&now);
      cout<<"\t Your bill \n";
      cout<<"Shop name: GadgetifyWithGSBlr \n";
      cout<<"Shop address: 311/5 Akshay nagar, Bangalore, Karnataka, India \n";
      cout<<"Shop contact no: +91 9988776655 \n";
      cout<<"The date and time :"<<dt<<"\n";
      cout<<"Name: "<<customer_name<<"\n";
      cout<<"Mobile No."<<phone_no<<"\n";
      cout<<"Payment Method:"<<payment_method<<"\n";
      
      if(method == 2)
      cout<<"Home Delivery: \n"<<"Shipping Adress: \n"<<address<<endl;
      else
      cout<<"Takeway \n";
      
      for(i=0;i<n;i++)
      {
         cout<<"Your selected item: "<<e1[i].name<<"\t";
         cout<<"and its quantity: "<<e1[i].quantity<<"\n"; 
      }
      
      cout<<"Total price: "<<total_price<<endl;
      cout<<"Tax amount: "<<tax_amount<<"\n";
      cout<<"Delivery price: "<<del_price<<endl;
      cout<<"Amount to be paid: "<<to_be_paid<<"\n";
      
     return 0;
}

