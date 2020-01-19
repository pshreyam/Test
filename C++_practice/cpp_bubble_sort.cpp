#include <iostream>
using namespace std;

void bubble_sort(int (&data)[10]);

int main()
{
    int data[10];

    for (int i=0;i<10;i++)
    {
        cin>>data[i];
    }

    bubble_sort(data);
    cout<<"------------------\n------------------"<<endl;

    for (int i=0;i<10;i++)
    {
        cout<<data[i]<<endl;
    }

    return 0;
}

void bubble_sort(int (&data)[10])
{
    int temp;
    int cnt=0;
    for (int i=0;i<9;i++)
    {
        for (int j=0;j<9-i;j++)
        {
            if (data[j]>data[j+1])
            {
                temp=data[j];
                data[j]=data[j+1];
                data[j+1]=temp;
                cnt+=1;
            }
        }
    }
    cout<<"--------\n--------\nCount:"<<cnt<<endl;
}
