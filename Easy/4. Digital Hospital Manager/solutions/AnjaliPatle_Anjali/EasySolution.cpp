#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main()
{
    vector<vector<string> >patient_data;
    
    string curr_date;
    cout<<"Enter current date (in DD/MM/YYYY format): ";
    cin>>curr_date;
    int n=0,flag=0;
    cout<<"\nSelect operation:- \n1-Add a patient\n2-See Patient database\n3-See number of patient's at given date\n4-Show current number of patients\n5-Exit";
    while(1){
        cout<<"\nEnter option: ";
        cin>>n;
        switch(n){
            case 1:{
                vector<string>patient;
                patient.push_back(to_string(patient_data.size()+1));
                
                string name;
                cout<<"Enter patient's name: ";
                cin.ignore();
                getline(cin,name);
                patient.push_back(name);
                
                string phone;
                cout<<"Enter phone no.: ";
                cin>>phone;
                patient.push_back(phone);
                
                string emgnumber;
                cout<<"Enter emergency phone no.: ";
                cin>>emgnumber;
                patient.push_back(emgnumber);
                
                int age;
                cout<<"Enter age: ";
                cin>>age;
                patient.push_back(to_string(age));
                
                string gender;
                cout<<"Enter gender ('M' for Male, 'F' for Female or 'O' for Other): ";
                cin>>gender;
                while(gender!="O"&&gender!="M"&&gender!="F"){
                    cout<<"\nInvalid option for gender. Please choose M (male), F(female) or O(other): ";
                    cin>>gender;
                }
                patient.push_back(gender);
                
                string blood_type;
                cout<<"Enter Blood Type (A+,A-,B+,B-,AB+,AB-,O+ or O-): ";
                cin.ignore();
                getline(cin,blood_type);
                while(blood_type!="A+"&&blood_type!="A-"&&blood_type!="B+"&&blood_type!="B-"&&blood_type!="O+"&&blood_type!="O-"&&blood_type!="AB+"&&blood_type!="AB-"){
                    cout<<"\nInvalid option Blood Type. (Please choose from A+,A-,B+,B-,AB+,AB-,O+ or O-): ";
                    getline(cin,blood_type);
                }
                patient.push_back(blood_type);
                
                float weight;
                cout<<"Enter weight in Kg: ";
                cin>>weight;
                patient.push_back(to_string(weight));
                
                float height;
                cout<<"Enter heigh in cm: ";
                cin>>height;
                patient.push_back(to_string(height));
                
                string symptom;
                cout<<"Enter symptoms: ";
                cin.ignore();
                getline(cin,symptom);
                patient.push_back(symptom);
                
                patient.push_back(curr_date);
                patient_data.push_back(patient);
                break;
            }
            case 2:{
                cout<<"Patient ID  |  Patient Name  |  Phone No.  |  Emergency contact  |  Age  |  Gender  |  Blood Type  |  Weight  |  Height  |  Symptoms  |  Date of Admission"<<endl;
                
                for(int i=0;i<patient_data.size();i++){
                   for(int j=0;j<patient_data[0].size();j++){
                       cout<<patient_data[i][j]<<" | ";
                   }
                   cout<<endl;
                }
                break;
            }
            case 3:{
                string date;
                cout<<"\nEnter date: ";
                cin>>date;
                int ans=0;
                for(int i=0;i<patient_data.size();i++){
                    if(patient_data[i][10]==date)ans++;
                }
                cout<<"Number of patients= "<<ans;
                break;
            }
            case 4:{
                cout<<"Number of patients currently in hospital= "<<patient_data.size();
                break;
            }
            case 5:{
                flag=1;
                break;
            }
        }
        cout<<"\n--------------------------------------------------------------------\n";
        if(flag==1)break;
    }

    return 0;
}
