#include <iostream>
#include <string.h>
#include <iomanip>
#include <string.h>
#include <ctime>


using namespace std;

struct items {
	string itemName;
	int price;
	int qty;
	int dis;
	int discount;
	int weight;
};


static struct items object[5];
string name, ph;
int pm,n, dis;
int p;
	int dist;
	char address[100];
float price, total, tax;


int main()
{
	object[0].itemName = "Basshead earphones";
	object[0].price = 1200;
	object[0].discount=1000;
	object[0].weight=150;
	object[1].itemName = "Bluetooth computer mouse";
	object[1].price = 600;
	object[1].discount=400;
	object[1].weight=150;
	object[2].itemName = "Bose earphones";
	object[2].price = 1000;
	object[2].discount=900;
	object[3].weight=150;
	object[3].itemName = "Bolt earphones";
	object[3].price = 300;
	object[3].discount=280;
	object[3].weight=150;
	object[4].itemName = "Boat earphones";
	object[4].price = 1000;
	object[4].discount=850;
	object[4].weight=150;
	for(int i=0;i<5;i++)
	{
		object[i].dis=object[i].price-object[i].discount;
	}
	
		cout << "Welcome to GadgetifyWithGSBlr"<<endl;
	cout<< "Shop address: 311/5 Akshay nagar, Bangalore, Karnataka, India"<<endl;
	cout<<"Shop contact no: +91 9988776655"<<endl<<endl;
	cout << "Enter you Name:          ";
	getline(cin, name);
	cout << "Enter your phone Number: ";
	cin >> ph;
	cout<<"Choose a payment method:"<<endl<<"1. Cash, 2. Card, 3. Online"<<endl<<"enter the corresponding index: ";
	cin>>pm;
	cout<<endl;
	cout<<"Available products on our store:"<<endl;
	for(int i=0;i<5;i++){
		cout<<i+1<<".  "<<object[i].itemName<<"   --> Original price:   "<<object[i].price<<"   --> Discounted on the item:  "<<object[i].price-object[i].discount<<"    ---> Final amount to be paid:   "<<object[i].discount<<"   ---> Weight    "<<object[i].weight<<endl;
	}
	cout<<endl<<endl;

	cout<<"Enter total no of items you want to buy"<<endl;
	cin>>n;
	int selected[n], qty[n];
	for(int i=0;i<n;i++)
	{
	cout <<endl<< "Select the item by its number which you want to buy: "<<endl;
	cin>>selected[i];
	cout<<endl;
	cout << "Quantity of " << object[selected[i]-1].itemName<<endl;
	cin >> qty[i];
	dis= dis+ (object[selected[i]-1].dis)*qty[i];

		
	}
	
	
	cout<<"Select 1 for Takeaway and 2 for Home delivery"<<endl;
	cin>>p;
	if(p==2)
	{
		
		cout<<"Enter dist from shop to the delivery address in KM"<<endl;
		cin>>dist;
		if(dist > 50)
	{
		cout<<"Sorry we don't provide shipping to this address"<<endl;
	}
		cout<<"Enter your address"<<endl;
		scanf(" %[^\n]s", address);
	}


	for(int i=0;i<n;i++)
	{
	price = price + qty[i] * object[selected[i]-1].discount;
	
	}
	cout<<price<<endl;
		tax = 0.06 * price;
	total = tax + price;
	cout<<total<<endl;
	if(p==2)
	{
		if(dist<=5)
		total=total;
		if(dist>5 && dist<=20)
		total=total+30;
		if(dist>20 && dist<=50)
		total=total+90;
	}
	
	cout<<total<<endl;
	
	 cout << "Welcome to GadgetifyWithGSBlr"<<endl;
	cout<< "Shop address: 311/5 Akshay nagar, Bangalore, Karnataka, India"<<endl;
	cout<<"Shop contact no: +91 9988776655"<<endl<<endl;
	cout<<"                                            "<<"Hey, "<<name<<"!"<<endl;
	cout<<"                                              "<<ph<<endl;
	cout<<"Your Bill Details:"<<endl<<endl;
	cout<<"Total no of types of items"<<n<<endl;
	for(int i=0;i<n;i++)
	{
		
	cout<<"Item name: "<<object[selected[i]-1].itemName<<endl;
	
	cout<<"Quantity: "<<qty[i]<<endl;	
	cout<<"Original Price: "<< object[selected[i]-1].price<<endl;
	cout<<"Discount given on the item"<<object[selected[i]-1].price-object[selected[i]-1].discount<<endl;
		cout<<"Final Price: "<< object[selected[i]-1].discount<<endl;
			cout<<"weight: "<< object[selected[i]-1].weight<<endl;
	}
	
	if(p==1)
	{
		cout<<"Takeaway option selected"<<endl;
	}
	else
	{
		cout<<"Home delivery option selected"<<endl;
		cout<<"Address : "<<address<<endl;
		cout<<"dist in kms from shipping point: "<<dist<<endl;
		if(dist>50)
		{
			cout<<"Delivery cancelled because of more dist"<<endl<<endl;
		}
	}
	cout<<"Tax on the purchased product:  "<<tax<<endl;
	cout<<"Amount to be paid: "<<total<<endl;
	cout<<"Amount saved by you:  "<<dis<<endl;
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
	return 0;
}

