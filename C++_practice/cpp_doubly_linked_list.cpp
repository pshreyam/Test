#include <iostream>
using namespace std;

class Node
{
public:
    int info;
    //Node* prev;
    Node* next;
};

class DoublyLinkedList
{
private:
        Node *HEAD;
        Node *TAIL;
public:
    DoublyLinkedList();
    ~DoublyLinkedList();

    void add_to_head(int element);
    void add_to_tail(int element);
    void add(int element,Node* ptr);

    void rem(int element);
    void rem_from_head();
    void rem_from_tail();

    Node* retreive(int element);
    bool search(int element);
    void traverse();
};

DoublyLinkedList::DoublyLinkedList()
{
    HEAD=NULL;
    TAIL=NULL;
}

DoublyLinkedList::~DoublyLinkedList(){}

void DoublyLinkedList::add_to_head(int element)
{
    Node* newNode=new Node();
    newNode->info=element;
    newNode->next=HEAD;
    //newNode->prev=NULL;
    HEAD=newNode;
    if (TAIL=NULL)
    {
        TAIL=newNode;
    }
}

void DoublyLinkedList::add_to_tail(int element)
{
    Node* newNode=new Node();
    newNode->info=element;
    newNode->next=NULL;
    //newNode->prev=TAIL;
    TAIL->next=newNode;
    TAIL=newNode;
    /*
    if (HEAD==NULL)
    {
        HEAD=newNode;
    }
    */
}

void DoublyLinkedList::traverse()
{
    Node *temp;
    temp=HEAD;
    while (temp!=NULL)
    {
        cout<<temp->info<<",";
        temp=temp->next;
    }
    cout<<endl<<"------------------"<<endl;
}




int main()
{
    DoublyLinkedList d1;
    d1.add_to_head(1);
    d1.add_to_head(3);
    d1.add_to_tail(2);
    //d1.add_to_tail(3);
    d1.traverse();

    return 0;
}
