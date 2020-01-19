#include <iostream>
#include <string>
using namespace std;

class Food{
private:
    string name;
    float price;
public:
    Food(string name,float price){this->name=name;this->price=price;}
    ~Food(){}
    void get_info()
    {
        cout<<"Name: "<<this->name<<endl;
        cout<<"Price: "<<this->price<<endl;
    }

    void set_num_of_food(int num)
    {
        //this->name=this->name;
        this->price*=num;
    }
};

int main(/*int argc,const char * argv[]*/)
{
    Food f1("Pizza",300.56);
    f1.get_info();
    f1.set_num_of_food(4);
    f1.get_info();
    return 0;
}
