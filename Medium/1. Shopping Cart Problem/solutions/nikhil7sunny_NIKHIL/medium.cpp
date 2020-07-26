#include<bits/stdc++.h>
#include<string>
using namespace std;

struct user{
	string uname;
	string phone ;
	string paymethod;
	string it[10];
	int quantity[10];
	string deliveryType;
	string address;
	float distance;
	float deliveryfee;
	float net[10];
	float total;
	int n;
}user_1;

struct shop{
	string sname ;
	string saddress;
	string sphone;
}shop_1;

struct item{
	string iname;
	float weight;
	float price;
	float discountPrice;

}item_list[7];

int size = 7,cnt = 0;
float tax = 0.06;
time_t now = time(0);
char* dt =ctime(&now);

void loop(){
	cout<<"\n";
	for (int i = 1;i<74;i++)
		cout<<"*";
}

void listassign(){
	item_list[0].iname = "Redmi Note 9 Pro Max";
	item_list[0].price = 16499;
	item_list[0].weight = 209;
	item_list[0].discountPrice = 15999;
	item_list[1].iname = "Redmi Note 9 Pro";
	item_list[1].price = 12999;
	item_list[1].weight = 210;
	item_list[1].discountPrice = 12000;
	item_list[2].iname = "Redmi 8A Dual";
	item_list[2].price = 6499;
	item_list[2].weight = 212.66;
	item_list[2].discountPrice = 0;
	item_list[3].iname = "Redmi 10 Pro";
	item_list[3].price = 50499;
	item_list[3].weight = 211;
	item_list[3].discountPrice = 45000;
	item_list[4].iname = "Redmi 10 Max";
	item_list[4].price = 49000;
	item_list[4].weight = 211;
	item_list[4].discountPrice = 43000;
	item_list[5].iname = "Redmi K30";
	item_list[5].price = 16100;
	item_list[5].weight = 230;
	item_list[5].discountPrice = 15400;
	item_list[6].iname = "Redmi A3";
	item_list[6].price = 12999;
	item_list[6].weight = 215;
	item_list[6].discountPrice = 12000;
	shop_1.sname = "GadgetifyWithGSBlr";
	shop_1.saddress = "311/5 Akshay nagar, Bangalore, Karnataka, India";
	shop_1.sphone = "+91 9988776655";
}

void displaylist(){
	cout<<setw(15)<<"ITEM NAME"<<setw(18)<<"PRICE"<<setw(19)<<"DISCOUNT PRICE"<<setw(10)<<"WEIGHT"<<"\n";
	cout<<setw(15)<<"---------"<<setw(18)<<"-----"<<setw(19)<<"--------------"<<setw(10)<<"------"<<"\n";
	for (int i = 0 ;i<size ;i++){
		cout<<setw(21)<<item_list[i].iname<<setw(8)<<"Rs "<<item_list[i].price;
		if(item_list[i].discountPrice != 0)
			cout<<setw(15)<<item_list[i].discountPrice;
		else
			cout<<setw(19)<<"No Discount";
		cout<<setw(10)<<item_list[i].weight<<"\n";

	}
}

void user_details(){
	string choice;
	cout<<"\n Enter the User Details :\n\n";
	cout<<setw(40)<<"Name : ";
	getline(cin,user_1.uname);
	cout<<setw(40)<<"Phone No : ";
	getline(cin,user_1.phone);
	cout<<setw(40)<<"Payment Method (cash/card/online) : ";
	getline(cin,user_1.paymethod);
	do{	
		cout<<setw(40)<<"Item to be Purchased : ";
		getline(cin,user_1.it[cnt]);
		cout<<setw(40)<<"Enter quantity : ";
		cin>>user_1.quantity[cnt];
		cin.ignore (std::numeric_limits<std::streamsize>::max(), '\n');
		cout<<setw(40)<<"Do You want to add another item to the cart\n";
		getline(cin,choice);
		cnt++;
	}while(choice.compare("yes") == 0);
	cout<<"\n Items successfully added to Cart\n";
	cout<<setw(40)<<"Delivery Type (Home Delivery/Take Away) : ";
	getline(cin,user_1.deliveryType);
	if(user_1.deliveryType.compare("Home Delivery") == 0){
		cout<<setw(40)<<"Distance : ";
		cin>>user_1.distance;
		cin.ignore (std::numeric_limits<std::streamsize>::max(), '\n');
		if(user_1.distance > 50)
			cout<<setw(40)<<"Cannot Deliver at a distance greater than 50 !!!!";
		else{
			cout<<setw(40)<<"Address :";
			getline(cin,user_1.address);
		}
	}
	cout<<"\n Your Order has been successfully Placed";
}

void caldelivery(){
	if(user_1.distance < 50 && user_1.distance > 20)
		user_1.deliveryfee = 60;
	else if (user_1.distance >20 && user_1.distance > 5)
		user_1.deliveryfee = 30;
	else
		user_1.deliveryfee = 0;
}

float netcalculate(){
	float sum = 0;
	user_1.total = 0;
	for (int i=0;i<cnt;i++){
		for(int j=0;j<size;j++){
			if(user_1.it[i].compare(item_list[j].iname) == 0){
				if(item_list[j].discountPrice == 0)
					user_1.net[i] = item_list[j].price * user_1.quantity[i];
				else 
					user_1.net[i] = item_list[j].discountPrice * user_1.quantity[i];
				user_1.total += item_list[j].price * user_1.quantity[i];
				break;
			}
		}
	sum += user_1.net[i];	
	}
	return sum;
}

void generatebill(){
	float tprice = netcalculate();
	int flag = 0;
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
	cout<<"\n"<<setw(30)<<"Name : "<<user_1.uname;
	cout<<"\n"<<setw(30)<<"Phone NO : "<<user_1.phone;
	cout<<"\n"<<setw(30)<<"Payment Method : "<<user_1.paymethod;
	cout<<"\n"<<setw(30)<<"Delivery Type : "<<user_1.deliveryType;
	if(user_1.deliveryType.compare("Home Delivery") == 0 && user_1.distance <50){
		cout<<"\n"<<setw(30)<<"Distance : "<<user_1.distance;
		cout<<"\n"<<setw(30)<<"Address : "<<user_1.address;
		flag = 1;
	}
	cout<<"\n\n"<<setw(15)<<"ITEM"<<setw(18)<<"QUANTITY"<<setw(15)<<"PRICE";
	cout<<"\n"<<setw(15)<<"----"<<setw(18)<<"--------"<<setw(15)<<"-----";
	for (int i=0;i<cnt;i++)
		cout<<"\n"<<setw(13)<<user_1.it[i]<<setw(18)<<user_1.quantity[i]<<setw(15)<<user_1.net[i];
	cout<<"\n"<<setw(50)<<"Amount Saved :  Rs "<<user_1.total-tprice;
	cout<<"\n"<<setw(50)<<"tax : "<<tax*100<<" %";
	tprice = tprice*(1+tax);
	if(flag){
		cout<<"\n"<<setw(50)<<"Delivery Fee : "<<user_1.deliveryfee;
		tprice = tprice + user_1.deliveryfee;
	}
	cout<<"\n"<<setw(50)<<"Total To Be Payed : "<<tprice;
}

int main(){
	listassign();
	displaylist();
	user_details();
	caldelivery();
	loop();
	generatebill();
	loop();
}