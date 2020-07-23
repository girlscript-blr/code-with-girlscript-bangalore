#include<bits/stdc++.h>
#include<iomanip>
#include<string>
#include<ctime>
using namespace std;

float tax = 1.06;
time_t now = time(0);
char* dt =ctime(&now);

struct list{
	string name ;
	float price;
}item[7];

struct user{
	string uname;
	string phone;
	string paymethod;
	string it;
	int quantity;
	float net;
}user1;

struct shop{
	string sname ;
	string saddress;
	string sphone;
}shop_1;

int size = 7;

void loop(){
	cout<<"\n";
	for (int i = 1;i<70;i++)
		cout<<"*";
}

void listassign(){
	item[0].name = "Redmi Note 9 Pro Max";
	item[0].price = 16499;
	item[1].name = "Redmi Note 9 Pro";
	item[1].price = 12999;
	item[2].name = "Redmi 8A Dual";
	item[2].price = 6499;
	item[3].name = "Redmi 10 Pro";
	item[3].price = 50499;
	item[4].name = "Redmi 10 Max";
	item[4].price = 49000;
	item[5].name = "Redmi K30";
	item[5].price = 16100;
	item[6].name = "Redmi A3";
	item[6].price = 12999;
	shop_1.sname = "GadgetifyWithGSBlr";
	shop_1.saddress = "311/5 Akshay nagar, Bangalore, Karnataka, India";
	shop_1.sphone = "+91 9988776655";
}

void displaylist(){
	cout<<setw(30)<<"ITEM NAME   "<<"     PRICE"<<"\n";
	cout<<setw(30)<<"---------   "<<"     -----"<<"\n";
	for (int i = 0 ;i<size ;i++){
		cout<<setw(30)<<item[i].name<<" : "<<item[i].price<<"\n";
	}
}

void details(){
	cout<<"\n Enter the User Details :\n\n";
	cout<<setw(20)<<"Name : ";
	getline(cin,user1.uname);
	cout<<setw(20)<<"Phone No : ";
	getline(cin,user1.phone);
	cout<<setw(20)<<"Payment Method (cash/card/online) : ";
	getline(cin,user1.paymethod);
	cout<<setw(20)<<"Item to be Purchased : ";
	getline(cin,user1.it);
	cout<<setw(20)<<"Enter quantity : ";
	cin>>user1.quantity; 
	cout<<"\n Your Order has been successfully Placed";
}

void generatebill(){
	for (int i = 0 ;i<size;i++){
		if(user1.it.compare(item[i].name) == 0){
			user1.net = item[i].price *user1.quantity * tax;
			break;
		}
	}
	cout<<"\n\n\n";
	cout<<"\t\t"<<dt<<"\n"<<"\t\t\t"<<shop_1.sname;
	cout<<"\n"<<"\t\t\t------------------\n"<<setw(15)<<shop_1.sphone;
	// cout<<"\n"<<shop_1.saddress;
	cout<<setw(26);
	for(int i = 0;i<shop_1.saddress.size();i++){
		cout<<shop_1.saddress[i];
		if(shop_1.saddress[i] == ','){
			cout<<"\n"<<setw(40);
		}
	}
	cout<<"\n\n";
	cout<<"\t\t\t BILL GENERATED\n";
	cout<<"\t\t\t --------------";
	cout<<"\n"<<setw(15)<<"User Details";
	cout<<"\n"<<setw(30)<<"Name : "<<user1.uname;
	cout<<"\n"<<setw(30)<<"Phone NO : "<<user1.phone;
	cout<<"\n"<<setw(30)<<"Payment Method : "<<user1.paymethod;
	cout<<"\n\n"<<setw(30)<<"ITEM PURCHASED  "<<"QUANTITY";
	cout<<"\n"<<setw(20)<<user1.it<<setw(17)<<user1.quantity;
	cout<<"\n\n"<<setw(40)<<"Tax :  "<<6;
    cout<<"\n\n"<<setw(40)<<"Total : Rs  "<<user1.net;
}

int main(){
	cout<<"\t\t\tGadgetifyWithGSBlr\n";
	cout<<"\t\t\t------------------\n\n\n";
	listassign();
	displaylist();
	details();
	loop();
	generatebill();
	loop();
	// cout<<item[0].name;
	cout<<"\n";
}