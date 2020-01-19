#import <iostream>
using namespace std;

class Node
{
public:
    int info;
    Node* prev;
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

DoublyLinkedList
