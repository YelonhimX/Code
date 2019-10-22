#include <iostream>
#include <stdio.h>
using namespace std;
#define MAXN 100000
int Bubble(int arr[],int m)
{
    for(int j = 1;j<=m;j++)
    {
        for (int k = 1; k <m; k++)
        {
         if(arr[k]<=arr[k+1])
         {
             swap(arr[k],arr[k+1]);
         }  /* code */
        }
        
    }

}
int main()
{
    int abc[MAXN];
    int n;
    cout<<"Hello"<<endl;
    cout<<"请输入排序数目"<<endl;
    cin>>n;
    cout<<"请输入数"<<endl;
    for(int i = 1;i<=5;i++)
    {
        cin>>abc[i];
    }
    Bubble(abc,n);
    for(int l = 1;l<=5;l++)
    {
        cout<<abc[l]<<" ";

    }
    system("pause");
    return 0;
    
}

