#include<iostream>
#include<string>
#include<cstdlib>
#include<ctime>
using namespace std;

class customer_class
{
public:
    string name;
    string phone;
    int payment_method;
    int selected_item;
    int quantity;
};

int main()
{
    customer_class customer;
    time_t current_time;
    time (&current_time);
    string item_list[6] = {"Pocket Printer","Gaming Headphone","Touch Pen","RGB Gaming Mouse","Bluetooth Speakers","Mechanical Keyboard"};
    int price[6] = {550,1800,500,1000,1550,3800};
    string payment[3] = {"cash","card","online"};
    cout << "                                    WELCOME TO OUR SHOP - \"GadgetifyWithGSBlr\"              " << endl << endl << endl;
    cout << "Here is a list of shopping items available: " << endl<<endl;
    cout << "            1 . Pocket Printer : Rs. 550" << endl <<
            "            2 . Gaming Headphone: Rs 1800" << endl;
    cout << "            3 . Touch Pen : Rs. 500" << endl <<
            "            4 . RGB Gaming Mouse: Rs 1000" << endl;
    cout << "            5 . Bluetooth Speakers : Rs. 1550" << endl <<
            "            6 . Mechanical Keyboard: Rs 3800" << endl << endl;
    cout << "Hello Dear Customer ! Please enter your details below for the generation of bill amount" << endl << endl;
    cout << "       Your Name: ";
    getline(cin,customer.name);
    cout << "       Your Phone Number: ";
    getline(cin,customer.phone);
    cout << "       Please choose the method number from the below list - " << endl;
    cout << "               1. cash" << endl << "               2. card" << endl << "               3. online" << endl;
    cout << "       Preferable payment method: ";
    cin >> customer.payment_method;
    cout << "       Please select the shopping item number:  ";
    cin >> customer.selected_item;
    cout << "       Please Enter the item quantity(in numbers): ";
    cin >> customer.quantity;
    cout << endl;
    cout << "       Here is your Bill:" << endl << endl;
    cout << "           Shop name: GadgetifyWithGSBlr" <<endl;
    cout << "           Shop address: 311/5 Akshay nagar, Bangalore, Karnataka, India" << endl;
    cout << "           Shop contact no: +91 9988776655" << endl;
    cout << "           Customer name: " << customer.name << endl;
    cout << "           Customer phone no: " << customer.phone << endl;
    cout << "           Item bought, it's quantity & price: " << customer.quantity << " "
         << item_list[customer.selected_item-1] << " " << price[customer.selected_item-1] << endl;
    double total_amount = price[customer.selected_item-1]*customer.quantity;
    double tax_amount = price[customer.selected_item-1]*customer.quantity*0.06;
    cout << "           Total tax: " << tax_amount << endl;
    cout << "           Sum amount to be paid: " << total_amount+tax_amount << endl;
    cout << "           Payment method used: " << payment[customer.payment_method-1] << endl;
    cout << "           Billing date and time: " << asctime(localtime(&current_time)) << endl;
}
