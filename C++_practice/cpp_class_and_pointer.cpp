#include <iostream>
using namespace std;
class Vehicle
{
private:
    int age;
    int speed;
public:
    Vehicle(){this->age=1;this->speed=60;}
    Vehicle(int age,int speed){this->age=age;this->speed=speed;}
    Vehicle(Vehicle &h){this->age=h.age;this->speed=h.speed;}

    ~Vehicle(){}

    void get_info()
    {
        cout<<"Age: "<<this->age<<endl;
        cout<<"Speed: "<<this->speed<<endl;
    }

    /*
    void set_speed(int speed)
    {
        this->speed=speed;
    }
    void set_age(int age)
    {
        this->age=age;
    }
    */
};

int main(int argc,const char * argv[])
{
    Vehicle bmw(2,80);
    Vehicle *pbmw=&bmw;
    pbmw->get_info();

    Vehicle *audi=new Vehicle(2,100);
    //audi->set_age(3);
    //audi->set_speed(90);
    audi->get_info();

    Vehicle c(bmw);
    c.get_info();
}
