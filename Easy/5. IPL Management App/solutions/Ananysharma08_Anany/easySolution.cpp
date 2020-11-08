#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    int numberofteams;
    cin>>numberofteams; // total teams
    
    string teamdetails[numberofteams][4]; //Matrix that stores team details
    
    for(int count=0;count<numberofteams;count++){
        for(int j=0;j<4;j++){
            cin>>teamdetails[count][j];
        }
    }
    cout<<"SI No."<<" | "<<"Team Name"<<" | "<<"Captain"<<" | "<<"Franchise"<<" | "<<"Home Ground"<<endl;
    
    for(int count=0;count<numberofteams;count++){
        cout<<count+1<<" | ";
        for(int j=0;j<4;j++){
            cout<<teamdetails[count][j]<<" | ";
        }
        cout<<"\n";
    }
    
	return 0;
}