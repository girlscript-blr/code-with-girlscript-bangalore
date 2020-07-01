#include <iostream>
#include <string.h>
#include <iomanip>
#include <string.h>
#include <ctime>


using namespace std;

struct items {
	string itemName;
	int price;
};


static struct items object[5];
string name, ph;
int pm, selected, qty;
float price, total, tax;



void output(){

    cout << "Welcome to GadgetifyWithGSBlr"<<endl;
	cout<< "Shop address: 311/5 Akshay nagar, Bangalore, Karnataka, India"<<endl;
	cout<<"Shop contact no: +91 9988776655"<<endl<<endl;
	cout<<"                                            "<<"Hey, "<<name<<"!"<<endl;
	cout<<"                                              "<<ph<<endl;
	cout<<"Your Bill Details:"<<endl<<endl;
	cout<<"Item name: "<<object[selected - 1].itemName<<endl;
	cout<<"Price: "<< object[selected - 1].price<<endl;
	cout<<"Quantity: "<<qty<<endl;	
	cout<<"Tax on the purchased product:  "<<tax<<endl;
	cout<<"Amount to be paid: "<<total<<endl;
	cout<<"Opted payment Method:  ";
	if(pm==1)
		cout<<"cash"<<endl;
	else if(pm==2)
		cout<<"card"<<endl;
		else cout<<"online"<<endl;
	cout<<endl;
	time_t tt;  
    struct tm * ti;  
    time (&tt); 
    ti = localtime(&tt); 
	cout <<"Date: "<<  ti->tm_mday <<"-"<<ti->tm_mon<<"-"<<1900 +ti->tm_year<< endl;	
	cout<<"time: "<<ti->tm_hour<<":"<<ti->tm_min<<":"<<ti->tm_sec<<endl<<endl; 
	
}
int main()
{
	object[0].itemName = "Basshead earphones";
	object[0].price = 1200;
	object[1].itemName = "Bluetooth computer mouse";
	object[1].price = 600;
	object[2].itemName = "Bose earphones";
	object[2].price = 1000;
	object[3].itemName = "Bolt earphones";
	object[3].price = 300;
	object[4].itemName = "Boat earphones";
	object[4].price = 100;
	
		cout << "Welcome to GadgetifyWithGSBlr"<<endl;
	cout<< "Shop address: 311/5 Akshay nagar, Bangalore, Karnataka, India"<<endl;
	cout<<"Shop contact no: +91 9988776655"<<endl<<endl;
	cout << "Enter you Name:          ";
	cin >> name;
	cout << "Enter your phone Number: ";
	cin >> ph;
	cout<<"Choose a payment method:"<<endl<<"1. Cash, 2. Card, 3. Online"<<endl<<"enter the corresponding index: ";
	cin>>pm;
	cout<<endl;
	cout<<"Available products on our store:"<<endl;
	for(int i=0;i<5;i++){
		cout<<i+1<<".  "<<object[i].itemName<<"   -->   "<<object[i].price<<endl;
	}
	cout<<endl<<endl;
	cout << "Select the item by its number which you want to buy: ";
	cin>>selected;
	cout<<endl;
	cout << "Quantity of " << object[selected - 1].itemName;
	cin >> qty;
	
	price = qty * object[selected - 1].price;
	tax = 6/100 * price;
	total = tax + price;
	
	output();
	return 0;
}

