#ifndef LINDEDLIST_H
#define LINKEDLIST_H
class Node
{
public:
    int info;
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

    void add_to_head(int data);
    void add_to_tail(int data);
    void add(int data,Node* prev);

    void remove_from_head();
    void remove_from_tail();
    void remove();

    void traverse();
    Node* retreive(int data);
    bool search();
};

#endif
