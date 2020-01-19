#include <iostream>
using namespace std;

class Node
{
public:
    int info;
    Node *next;
};

class LinkedList
{
private:
    Node *HEAD;
    Node *TAIL;
public:
    LinkedList();
    ~LinkedList();

    void add_to_head(int data);
    void add_to_tail(int data);
    void add(int data,Node *ptr);

    void remove_from_head();
    void remove_from_tail();
    void remove(int data);

    Node *retreive(int data);
    void traverse();
};

LinkedList::LinkedList()
{
    HEAD=NULL;
    TAIL=NULL;
}

LinkedList::~LinkedList(){}

void LinkedList::add_to_head(int data)
{
    Node *newNode=new Node();
    newNode->info=data;
    newNode->next=HEAD;
    HEAD=newNode;
    if (TAIL==NULL)
    {
        TAIL=newNode;
    }
}

void LinkedList::add_to_tail(int data)
{
   Node *newNode=new Node();
   newNode->info=data;
   newNode->next=NULL;
   TAIL->next=newNode;
   TAIL=newNode;
   if (HEAD==NULL)
   {
       HEAD=newNode;
   }
}

void LinkedList::add(int data,Node *ptr)
{
    Node *newNode=new Node();
    newNode->info=data;
    newNode->next=ptr->next;
    ptr->next=newNode;
}

void LinkedList::remove_from_head()
{
    Node *nodeToDelete;
    nodeToDelete=HEAD;
    HEAD=HEAD->next;
    delete nodeToDelete;
}

void LinkedList::remove_from_tail()
{
    Node *nodeToDelete;
    Node *temp;
    nodeToDelete=HEAD;
    temp=HEAD;
    while (nodeToDelete!=NULL)
    {
        if (nodeToDelete==TAIL)
        {
            delete nodeToDelete;
            TAIL=temp;
        }
        temp=nodeToDelete;
        nodeToDelete=nodeToDelete->next;
    }

}

void LinkedList::remove(int data)
{
    Node *nodeToDelete,*temp;
    nodeToDelete=HEAD;
    temp=HEAD;
    while (nodeToDelete!=NULL)
    {
        if (nodeToDelete->info==data)
        {
            temp->next=nodeToDelete->next;
            delete nodeToDelete;
            return;
        }
        temp=nodeToDelete;
        nodeToDelete=nodeToDelete->next;
    }
    cout<<"Data not found."<<endl;
}

Node *LinkedList::retreive(int data)
{
    Node* temp;
    temp=HEAD;
    while (temp!=NULL)
    {
        if (temp->info==data)
        {
            return temp;
        }
        temp=temp->next;
    }
    cout<<"Data not found!"<<endl;
}

void LinkedList::traverse()
{
    Node *temp;
    temp=HEAD;
    while (temp!=NULL)
    {
        cout<<temp->info<<endl;
        temp=temp->next;
    }
}

int main()
{
    LinkedList ll;
    ll.add_to_head(1);
    ll.add_to_head(2);
    ll.add_to_head(3);
    ll.add_to_head(4);
    ll.add_to_head(5);
    ll.add_to_head(6);
    ll.add_to_head(7);
    ll.add_to_tail(8);
    /*ll.traverse();
    cout<<"-----------------"<<endl;
    Node *ptr=ll.retreive(4);
    ll.add(7,ptr);
    ll.traverse();
    cout<<"-----------------"<<endl;
    ll.remove_from_head();
    ll.traverse();*/
    ll.remove(3);
    ll.traverse();
    return 0;
}
