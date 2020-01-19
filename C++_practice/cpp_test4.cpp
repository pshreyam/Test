#include <iostream>
using namespace std;

class Node
{
public:
    int info;
    Node *next;
};

int main(int argc,const char * argv[])
{
    Node *newNode=new Node();
    Node *newNode1=new Node();

    newNode->info=1;
    newNode->next=newNode1;
    newNode1->info=2;
    newNode1->next=newNode;

    return 0;
}
