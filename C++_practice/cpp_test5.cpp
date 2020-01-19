#include <iostream>
#include <string>
using namespace std;

class Person
{
private:
    int age;
    string name;
public:
    Person(int age,string name){this->age=age;this->name=name;}
    ~Person(){}
    void get_info()
    {
        cout<<"Name: "<<name<<endl<<"Age: "<<age<<endl;
    }
};

int main()
{
    Person p1(19,"Shreyam Pokharel");
    p1.get_info();

    Person *ptr=new Person(44,"Adam Gilchrist");
    ptr->get_info();
    return 0;
}
