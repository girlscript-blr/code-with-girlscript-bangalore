//Solution of the Shopping Cart Easy - Problem

#include <iostream>
#include <stdio.h>
#include <string.h>
#include <ctime>

using namespace std;

class GadgetifyWithGSBlr
{
    private:
    char customer_name[100];
    char phone_no[15];
    char payment_method[25];
    char item[50];
    int s_no = 0;
    int quantity;
    double price = 0.0;
    double tax_amount = 0.0;
    double total_price = 0.0;
    double to_be_paid = 0.0;
    
    public :
    void catalog()
    {
      cout<<"Welcome to our shop \n";
      cout<<"The catalog is as follows \n";
      cout<<"1.Basshead Earphones : 1200 \n" ; 
	  cout<<"2.Bluetooth Computer Mouse : 600 \n"; 
	  cout<<"3.Bluetooth Headphones : 1600 \n";
	  cout<<"4.Fast Mobile Charger : 1400 \n" ;
	  cout<<"5.Smartband : 2200 \n";
    
    }
    void input()
    {
      cout<<"Please enter your name "<<endl;
      cin.get(customer_name , 100);cin.ignore();
      cout<<"Please enter your mobile number"<<endl;
      cin.get(phone_no , 20);cin.ignore();
      cout<<"Please enter payment method (cash/card/online)"<<endl;
      cin.get(payment_method , 25);cin.ignore();
      cout<<"Please enter the serial number of your selected item "<<endl;
      cin>>s_no;cin.ignore();
      cout<<"Quantity "<<endl;
      cin>>quantity;cin.ignore();
    }
    void calculate()
    {
          if(s_no == 1)
             price = 1200;
          if(s_no == 2)
             price = 600;
          if(s_no == 3)
             price = 1600;
          if(s_no == 4)
             price = 1400;
          if(s_no == 5)
             price = 2200;
          
          total_price = price*quantity;
          tax_amount = total_price * 0.06;
          to_be_paid = tax_amount + total_price;
          
    }
  void dispaly()
   {
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
      cout<<"Your selected item: "<<item<<"\t";
      cout<<"and its quantity: "<<quantity<<"\n";
      calculate();
      cout<<"Total price: "<<total_price<<endl;
      cout<<"Tax amount: "<<tax_amount<<"\n";
      cout<<"Amount to be paid: "<<to_be_paid<<"\n";
      
    };
  
};


int main()
{
    GadgetifyWithGSBlr O1;
    O1.catalog();
    O1.input();
    O1.calculate();
    O1.dispaly();
    return 0;
}

