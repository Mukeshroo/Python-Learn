#include <iostream>
using namespace std;
#include <string>

class Student {
public:
    string name;
    int roll_no;

    void display() {
        cout << "Name: " << name << endl;
        cout << "Roll No: " << roll_no << endl;
    }
};

int main() {
    Student a;

    a.name = "MSK Singh";
    a.roll_no = 101;

    a.display();

    return 0;
}