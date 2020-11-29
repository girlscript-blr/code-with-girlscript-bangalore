#include <iostream>

using namespace std;

int main()
{

   int num;

   cout<<"Number of Teams playing the tournament:";
   cin>>num;
   string name[num+1], captain[num+1], franchise[num+1], home_ground[num+1];
   for(int i=1;i<=num;i++){
    cout<<"\nFill Team"<<i<<" Details:";
    cout<<"\nName:";
    cin>>name[i];
    cout<<"\nCaptain:";
    cin>>captain[i];
    cout<<"\nFranchise:";
    cin>>franchise[i];
    cout<<"\nHome Ground:";
    cin>>home_ground[i];

   }
   cout<<"\nSI No.\t\tTeam Name\tCaptain\t\tFranchise\tHome Ground\n";
   for(int i=1;i<=num;i++){
    cout<<i<<"\t\t"<<name[i]<<"\t\t"<<captain[i]<<"\t\t"<<franchise[i]<<"\t\t"<<home_ground[i]<<"\n";
   }
    return 0;
}
