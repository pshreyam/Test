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
    Node *HEAD=NULL;
    Node *TAIL=NULL;
public:
    LinkedList();
    ~LinkedList();

    void add_to_head(int element);
    void add_to_tail(int element);
    void add(int data, Node *predecessor);
    bool search(int data);
    void traverse();
    Node * retreive(int data);
    void remove_from_head();
    void remove(int data);
};


LinkedList::LinkedList(){HEAD=NULL;TAIL=NULL;}

LinkedList::~LinkedList(){}

void LinkedList::add_to_head(int element)
{
    Node *newNode=new Node();
    newNode->info=element;
    newNode->next=HEAD;
    HEAD=newNode;
    if (TAIL==NULL)
    {
        TAIL=HEAD;
    }
}

void LinkedList::add_to_tail(int element)
{
    Node *newNode=new Node();
    newNode->info=element;
    newNode->next=NULL;
    TAIL->next=newNode;
    TAIL=newNode;
}

void LinkedList::add(int data,Node *predecessor)
{
    Node *newNode=new Node();
    newNode->info=data;
    newNode->next=predecessor->next;
    predecessor->next=newNode;
}

void LinkedList::traverse()
{
    Node *temp=HEAD;
    while (temp!=NULL)
    {
        cout<<temp->info<<endl;
        temp=temp->next;
    }
}

bool LinkedList::search(int data)
{
    Node *temp=HEAD;
    while (temp!=NULL)
    {
        if (temp->info==data)
        {
            return true;
        }
        temp=temp->next;
    }
    return false;
}

void LinkedList::remove_from_head()
{
    Node *nodetodelete;
    nodetodelete=HEAD;
    HEAD=HEAD->next;
    delete nodetodelete;
}


void LinkedList::remove(int data)
{
    Node *temp=HEAD;
    Node *prev=HEAD;
    while (temp!=NULL)
    {
        if (temp->info==data)
        {
            prev->next=temp->next;
            delete temp;
            cout<<"Node deleted"<<endl;
            return;
        }
        prev=temp;
        temp=temp->next;
    }
    cout<<"Node not found"<<endl;
}

Node * LinkedList::retreive(int data)
{
    Node *temp=HEAD;
    while (temp!=NULL)
    {
        if (temp->info==data)
        {
            return temp;
        }
        temp=temp->next;
    }
    cout<<"Node not present."<<endl;
}


int main()
{
    LinkedList l1;

    l1.add_to_head(1);
    l1.add_to_head(2);

    l1.add_to_tail(4);
    l1.add_to_tail(3);

    l1.traverse();

    cout<<"List:"<<endl;
    l1.add(7,l1.retreive(2));
    l1.traverse();

    /*l1.remove(3);
    cout<<"NEW LIST"<<endl;
    l1.traverse();
    */

    /*
    bool a=l1.search(1);
    if (a==true)
    {
        cout<<"Data found."<<endl;
    }
    else
    {
        cout<<"Data not found."<<endl;
    }
    */
}





