#ifndef CPP_TEST_H
#define CPP_TEST_H

#include <iostream>
using namespace std;
#define Max 100

class Queue
{
    private:
        char queue_array[Max];
        int f;
        int r;
    public:
        Queue();
        ~Queue();
        void enqueue(char element);
        char dequeue();
        char frnt();
        char rear();
        bool isEmpty();
        bool isFull();
        void view_queue();
};

Queue::Queue(){f=-1;r=-1;}
Queue::~Queue(){}

bool Queue::isEmpty()
{
    return (f==r);
}

bool Queue::isFull()
{
    return (r==Max-1);
}

void Queue::enqueue(char element)
{
    if (!isFull())
    {
        r++;
        queue_array[r]=element;

    }
    else
    {
        cout<<"Cannot enqueue."<<endl;
    }
}

char Queue::dequeue()
{
    if (!isEmpty())
    {
        return queue_array[++f];
    }
    else
    {
        cout<<"Cannot dequeue."<<endl;
    }
}

char Queue::frnt()
{
    if (!isEmpty())
    {
        return queue_array[f];
    }
    else
    {
        cout<<"Cannot show front."<<endl;
    }
}

char Queue::rear()
{
    if (!isEmpty())
    {
        return queue_array[r];
    }
    else
    {
        cout<<"Cannot show front."<<endl;
    }
}
void Queue::view_queue()
{
    cout<<"Queue:"<<endl;
    for (int i=0;i<=r;i++)
    {
        cout<<queue_array[i]<<",";
    }
}






#endif // CPP_TEST_H

