#include<iostream>
using namespace std;

class Node
{
public:
    char info;
    Node* next;
};

class LinkedList
{
private:
    Node* HEAD;
    Node* TAIL;
public:
    LinkedList();
    ~LinkedList();

    void add(char data,Node *pre);
    void add_to_head(char data);
    void add_to_tail(char data);

    void remove(char data);
    void remove_from_head();
    void remove_from_tail();

    void traverse();
    Node* retreive(char data);
    bool search(char data);
};

LinkedList::LinkedList()
{
    HEAD=NULL;
    TAIL=NULL;
}

LinkedList::~LinkedList(){}

void LinkedList::add_to_head(char data)
{
    Node* newNode=new Node();
    newNode->info=data;
    newNode->next=HEAD;
    HEAD=newNode;
    if (TAIL==NULL)
    {
        TAIL=newNode;
    }
}

void LinkedList::add_to_tail(char data)
{
    Node* newNode=new Node();
    newNode->info=data;
    newNode->next=NULL;
    TAIL->next=newNode;
    TAIL=newNode;
    if (HEAD==NULL)
    {
        HEAD=newNode;
    }
}

void LinkedList::add(char data,Node *pre)
{
    Node* newNode=new Node();
    newNode->info=data;
    newNode->next=pre->next;
    pre->next=newNode;
}

void LinkedList::remove(char data)
{
    Node *nodetodelete,*temp;
    nodetodelete=HEAD;
    temp=HEAD;
    while (nodetodelete!=NULL)
    {
        if (nodetodelete->info==data)
        {
            temp->next=nodetodelete->next;
            delete nodetodelete;
            return;
        }
        temp=nodetodelete;
        nodetodelete=nodetodelete->next;
    }
    cout<<"Data not found."<<endl;
}

void LinkedList::remove_from_head()
{
    Node* nodetodelete;
    nodetodelete=HEAD;
    HEAD=HEAD->next;
}

void LinkedList::remove_from_tail()
{
    Node* nodetodelete;
    Node* temp;
    nodetodelete=HEAD;
    temp=HEAD;
    while(nodetodelete!=NULL)
    {
        if (nodetodelete==TAIL)
        {
            delete nodetodelete;
            TAIL=temp;

        }
        temp=nodetodelete;
        nodetodelete=nodetodelete->next;
    }

}

void LinkedList::traverse()
{
    Node* temp;
    temp=HEAD;
    while (temp!=NULL)
    {
        cout<<temp->info<<",";
        temp=temp->next;
    }
    cout<<endl<<"-----------------------------"<<endl;
}

Node* LinkedList::retreive(char data)
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
    cout<<"Data not present"<<endl;
}

bool LinkedList::search(char data)
{
    Node* temp;
    temp=HEAD;
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


int main()
{
    LinkedList ll;
    ll.add_to_head('b');
    ll.add_to_head('c');
    ll.add_to_head('a');
    Node* ptr=ll.retreive('c');
    ll.add('e',ptr);
    ll.add_to_tail('g');
    ll.add_to_tail('h');
    ll.traverse();
    //ll.remove_from_head();
    //ll.remove_from_head();
    //ll.remove('g');
    //ll.remove('c');
    /*
    bool res=ll.search('h');
    if (res==true)
    {
        cout<<"Data found.\n";
    }
    else
    {
        cout<<"Data not found.\n";
    }
    ll.traverse();
    */


    return 0;
}
