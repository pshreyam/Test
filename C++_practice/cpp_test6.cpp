#include <iostream>
#include <string>
using namespace std;

class Vehicle
{
private:
    int speed;
    int age;
    string name;
public:
    Vehicle(int speed,int age,string name){this->speed=speed;this->age=age;this->name=name;}
    ~Vehicle(){}
    void get_info()
    {
        cout<<"Name: "<<this->name<<endl<<"Speed: "<<this->speed<<endl<<"Age: "<<this->age<<endl;
    }
    void improve_speed_by_value(int speed_factor)
    {
        this->speed+=speed_factor;
    }
};

int main()
{
    Vehicle v1(90,2,"Ford");
    v1.get_info();
    v1.improve_speed_by_value(30);
    v1.get_info();
    return 0;
}
