#include <iostream>
#include <bits/stdc++.h>
using namespace std;

bool isNumber(string s)
{
    for (int i = 0; i < s.length(); i++)
        if (isdigit(s[i]) == false && s[i]!='.')
            return false;
    return true;
}

int main()
{
    cout<<"Enter number of teams: ";
    string num;
    cin>>num;
    while(!isNumber(num)){
        cout<<"Invalid input. Please enter a number.";
        cin>>num;
    }
    int n=stoi(num);
    cin.ignore();
    string teams[n][4];
    for(int i=0;i<n;i++){
        cout<<"\nEnter details of team-"<<i+1<<endl;
        string name,captain,franchise,home_ground;
        cout<<"Enter name: ";
        getline(cin,name);
        cout<<"Enter Captain: ";
        getline(cin,captain);
        cout<<"Enter franchise: ";
        getline(cin,franchise);
        cout<<"Enter Home Ground: ";
        getline(cin,home_ground);
        teams[i][0]=name;
        teams[i][1]=captain;
        teams[i][2]=franchise;
        teams[i][3]=home_ground;
    }
    cout<<"-----Team Details-----"<<endl;
    cout<<"SI No.   |   Team Name   |   Captain   |   Franchise   |   Home Ground   |"<<endl;
    for(int i=0;i<n;i++){
        cout<<"   "<<i+1<<"   |   "<<teams[i][0]<<"   |   "<<teams[i][1]<<"   |   "<<teams[i][2]<<"   |   "<<teams[i][3]<<"   |   "<<endl;
    }
    cout<<"\n-----Matches-----\n";
    int mn=0;
    cout<<"Match No.   |   Home Team   |   Away Team   |   Venue"<<endl;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(i==j)continue;
            cout<<"    "<<mn+1<<"    |    "<<teams[i][0]<<"    |    "<<teams[j][0]<<"    |    "<<teams[i][3]<<endl;
            mn++;
        }
    }
    return 0;
}
