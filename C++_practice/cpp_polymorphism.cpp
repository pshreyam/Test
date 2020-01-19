#include <iostream>
using namespace std;
class Shape
{
    //This is an abstract class for various shapes as it has a pure virtual function get_area
    protected:
        int height,breadth;
    public:

        //Constructors
        Shape(int height,int breadth){this->height=height;this->breadth=breadth;}
        Shape(Shape &s){this->height=s.height;this->breadth=s.breadth;}
        //Destructor
        ~Shape(){}
        //Class functions
        virtual float get_area()=0;//Pure Virtual function
};

class Rectangle:public Shape
{
    public:
        //Inheriting constructor
        Rectangle(int height,int breadth):Shape(height,breadth){}
        float get_area()
        {

            return this->height * this->breadth;
        }

};

class Triangle:public Shape
{
    public:
        //Inheriting constructor
        Triangle(int height,int breadth):Shape(height,breadth){}
        float get_area()
        {

            return 0.5 * this->height * this->breadth;
        }

};


int main()
{
    Rectangle r1(1,2);
    Triangle t1(1,2);
    Shape *sp;
    sp=&t1;
    cout<<sp->get_area();
    sp=&r1;
    cout<<endl<<sp->get_area();

    return 0;
}
