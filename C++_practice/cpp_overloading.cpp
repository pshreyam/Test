#include<iostream>
using namespace std;
class Point
{
    private:
        float x_cord,y_cord;
    public:
        Point(){this->x_cord=0;this->y_cord=0;} //default constructor
        Point(float x_cord,float y_cord){this->x_cord=x_cord;this->y_cord=y_cord;} //parameterized constructor
        ~Point(){} //destructor


        void get_x_cord()
        {
            cout<<this->x_cord<<endl;
        }

        void get_y_cord()
        {
            cout<<this->y_cord<<endl;
        }

        void get_both_cord()
        {
            this->get_x_cord(); // or simply get_x_cord()
            this->get_y_cord(); // or simply get_y_cord()
        }


        Point operator+(Point p)
        {
            Point temp;
            temp.x_cord=this->x_cord+p.x_cord;
            temp.y_cord=this->y_cord+p.y_cord;
            return temp;
        }


        Point operator-(Point p)
        {
            Point temp;
            temp.x_cord=this->x_cord-p.x_cord;
            temp.y_cord=this->y_cord-p.y_cord;
            return temp;
        }


        Point operator*(Point p)
        {
            Point temp;
            temp.x_cord=this->x_cord*p.x_cord;
            temp.y_cord=this->y_cord*p.y_cord;
            return temp;
        }


        Point operator/(Point p)
        {
            Point temp;
            temp.x_cord=this->x_cord/p.x_cord;
            temp.y_cord=this->y_cord/p.y_cord;
            return temp;
        }








        /*
        friend Point operator+(Point temp1,Point temp2);
        friend Point operator-(Point temp1,Point temp2);
        friend Point operator*(Point temp1,Point temp2);
        friend Point operator/(Point temp1,Point temp2);
        */
        friend ostream& operator<<(ostream &out,Point temp);

};
/*
Point operator+(Point temp1,Point temp2)
{
    Point result;
    result.x_cord=temp1.x_cord+temp2.x_cord;
    result.y_cord=temp1.y_cord+temp2.y_cord;
    return result;
}
Point operator-(Point temp1,Point temp2)
{
    Point result;
    result.x_cord=temp1.x_cord-temp2.x_cord;
    result.y_cord=temp1.y_cord-temp2.y_cord;
    return result;
}
Point operator*(Point temp1,Point temp2)
{
    Point result;
    result.x_cord=temp1.x_cord*temp2.x_cord;
    result.y_cord=temp1.y_cord*temp2.y_cord;
    return result;
}
Point operator/(Point temp1,Point temp2)
{
    Point result;
    result.x_cord=temp1.x_cord/temp2.x_cord;
    result.y_cord=temp1.y_cord/temp2.y_cord;
    return result;
}

*/
ostream& operator<<(ostream &out,Point temp)
{
    out<<"("<<temp.x_cord<<","<<temp.y_cord<<")"<<endl;
    return out;
}



int main()
{
    Point p1(1,2),p2(3,4);
    Point p3=p1+p2;
    cout<<p3<<p1<<p2;
    return 0;
}
