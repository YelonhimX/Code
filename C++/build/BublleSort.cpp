//最简单的冒泡排序
#include <iostream>
#include <stdio.h>
using namespace std;
int main()
{
    int abc[10];
    cout<<"Hello"<<endl;
    
    for(int i = 1;i<=5;i++)
    {
        cin>>abc[i];
    }
    for(int j = 1;j<=5;j++)
    {
        for (int k = 1; k <5; k++)
        {
         if(abc[k]<=abc[k+1])
         {
             swap(abc[k],abc[k+1]);
         }  /* code */
        }
        
    }
    for(int l = 1;l<=5;l++)
    {
        cout<<abc[l]<<" ";

    }
    system("pause");
    return 0;
    
}

