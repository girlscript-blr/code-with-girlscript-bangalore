#include <bits/stdc++.h>
#include <iostream>

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

   string n;

   cout<<"Number of Teams playing the tournament:";
   cin>>n;

    while(!isNumber(n)){
        cout<<"Retry!";
        cin>>n;
    }
    int num=stoi(n);
    cin.ignore();

    string name[num+1], captain[num+1], franchise[num+1], home_ground[num+1];
   for(int i=1;i<=num;i++){
    cout<<"\nFill Team"<<i<<" Details:";
    cout<<"\nName:";
    getline(cin,name[i]);
    cout<<"\nCaptain:";
    getline(cin,captain[i]);
    cout<<"\nFranchise:";
    getline(cin,franchise[i]);
    cout<<"\nHome Ground:";
    getline(cin,home_ground[i]);

   }
   cout<<"\nSI No.\t\tTeam Name\tCaptain\t\tFranchise\tHome Ground\n";
   for(int i=1;i<=num;i++){
    cout<<i<<"\t\t"<<name[i]<<"\t\t"<<captain[i]<<"\t\t"<<franchise[i]<<"\t\t"<<home_ground[i]<<"\n";
   }


    return 0;
}

