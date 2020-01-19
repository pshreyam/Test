#include<iostream>
using namespace std;

class Id{
private:
    int roll_num;
    int symbol_num;
public:
    Id(int roll_num,int symbol_num){this->roll_num=roll_num;this->symbol_num=symbol_num;}
    ~Id(){}
    void get_id()
    {
        cout<<"Roll no.: "<<this->roll_num<<endl;
        cout<<"Symbol no.: "<<this->symbol_num<<endl;
    }
};

int main(int argc,const char * argv[])
{
    Id i(14,3435343);
    i.get_id();
    return 0;
}
