#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main()
{
    vector<vector<string> >patient_data;
    
    string curr_date;
    cout<<"Enter current date: ";
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
                
                string age;
                cout<<"Enter age: ";
                cin>>age;
                patient.push_back(age);
                
                string gender;
                cout<<"Enter gender.: ";
                cin>>gender;
                patient.push_back(gender);
                
                string blood_type;
                cout<<"Enter Blood Type: ";
                cin>>blood_type;
                patient.push_back(blood_type);
                
                string weight;
                cout<<"Enter weight: ";
                cin>>weight;
                patient.push_back(weight);
                
                string height;
                cout<<"Enter height: ";
                cin>>height;
                patient.push_back(height);
                
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
        cout<<"--------------------------------------------------------------------\n";
        if(flag==1)break;
    }

    return 0;
}
