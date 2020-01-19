#include "cpp_test.h"
int main()
{
    Queue q1;
	//Enqueue
	q1.enqueue('s');
	q1.enqueue('t');
    q1.enqueue('u');
    q1.enqueue('d');
	//Dequeue
	cout<<q1.dequeue();
	cout<<q1.dequeue();
	/*cout<<q1.dequeue();
	cout<<q1.dequeue();
	cout<<q1.dequeue();
	cout<<q1.dequeue();
	cout<<q1.dequeue();
	cout<<q1.dequeue();*/
	q1.view_queue();
	return 0;
}
