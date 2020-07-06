#include <iostream>
#include <string.h>
#include <iomanip>
#include <string.h>
#include <ctime>

#define MAX 6

using namespace std;

struct ShoppingItems {
	string itemName;
	int price;
};

static struct ShoppingItems object[MAX];
string name, phoneNumber;
int paymentMethod, selectedItem, quantity;
float price, totalSum, tax;
static string shopName = "GadgetifyWithGSBlr", shopAddress = "311/5 Akshay nagar, Bangalore, Karnataka, India",
	shopContactNo = "+91 9988776655";

void products() {
	object[0].itemName = "Basshead earphones";
	object[0].price = 1200;
	object[1].itemName = "Bluetooth computer mouse";
	object[1].price = 600;
	object[2].itemName = "64gb Pendrive";
	object[2].price = 880;
	object[3].itemName = "Inkjet Printer";
	object[3].price = 3000;
	object[4].itemName = "Laptop Stand";
	object[4].price = 800;
	object[5].itemName = "USB keyboard";
	object[5].price = 390;
	
}
void input(){
	cout << "Welcome to " + shopName << endl<<endl;
	cout << "Enter you Name:          ";
	cin >> name;
	cout << "Enter your phone Number: ";
	cin >> phoneNumber;
	cout<<"Choose a payment method:"<<endl<<"1. Cash"<<endl<<"2. Card"<<endl<<"3. Online"<<endl<<"enter the corresponding index: ";
	cin>>paymentMethod;
	cout<<endl;
	cout<<"Available products on our store:"<<endl;
	for(int i=0;i<MAX;i++){
		cout<<i+1<<". "<<object[i].itemName<<setw(20)<<object[i].price<<endl;
	}
	cout<<endl<<endl;
	cout << "Select the corresponding index:";
	cin >> selectedItem;
	cout<<endl;
	cout << "Quantity of " << object[selectedItem - 1].itemName;
	cin >> quantity;
}
void calculate(){
	price = quantity * object[selectedItem - 1].price;
	tax = 0.06 * price;
	totalSum = tax + price;
}
void output(){
	int i=10;
	while(i--)
		cout<<endl;
	cout<<"                                            "<<shopName<<endl;
	cout<<"                             "<<shopAddress<<endl;
	cout<<"                                              "<<shopContactNo<<endl<<endl;
	cout<<"                                            "<<"Hey, "<<name<<"!"<<endl;
	cout<<"                                              "<<phoneNumber<<endl;
	cout<<"Your Bill Details:"<<endl<<endl;
	cout<<"Item name:                     "<<object[selectedItem - 1].itemName<<endl;
	cout<<"Price:                         "<< object[selectedItem - 1].price<<endl;
	cout<<"Quantity:                      "<<quantity<<endl;	
	cout<<"Tax on the purchased product:  "<<tax<<endl;
	cout<<"Amount to be paid:             "<<totalSum<<endl;
	cout<<"Opted payment Method:          ";
	if(paymentMethod==1)
		cout<<"cash"<<endl;
	else if(paymentMethod==2)
		cout<<"card"<<endl;
		else cout<<"online"<<endl;
	cout<<endl;
	time_t tt;  
    struct tm * ti;  
    time (&tt); 
    ti = localtime(&tt); 
	cout <<"Date: "<<  ti->tm_mday <<"-"<<ti->tm_mon<<"-"<<1900 +ti->tm_year<< endl;	
	cout<<"time: "<<ti->tm_hour<<":"<<ti->tm_min<<":"<<ti->tm_sec<<endl<<endl; 
	cout<<"thankyou for shopping at "<<shopName<<"!"<<endl<<"      Visit Again :)";
}
int main()
{
	products();
	input();
	calculate();
	output();
	return 0;
}


