#include <iostream>
#include <math.h>
using namespace std;
class Point
{
    private:
        int x_cord,y_cord;
    public:
        Point(int x_cord,int y_cord){this->x_cord=x_cord;this->y_cord=y_cord;}
        ~Point(){}
        float getModulus()
        {
            float modulus=sqrt((this->x_cord*this->x_cord)+(this->y_cord*this->y_cord));
            return modulus;
        }
        //copy constructor is created by default we do not need to define it for simple programs
        /*Point (Point &h)
        {
            this->x_cord=h.x_cord;
            this->y_cord=h.y_cord;
        }*/
};

int main()
{
    Point p1(1,1);
    Point p2=p1;
    Point p3(p2);
    cout<<p3.getModulus();
    return 0;

}

