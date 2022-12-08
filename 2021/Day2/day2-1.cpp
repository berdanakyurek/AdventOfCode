#include <iostream>
#include <fstream>
using namespace std;

int main(){
    ifstream file("input.txt");

    string line;

    int x = 0;
    int y = 0;


    while (getline(file, line)) {
        string str1 = "";
        string str2 = "";
        bool s2 = false;
        for(char c: line)
            if(c == ' ')
                s2 = true;
            else if(!s2)
                str1 += c;
            else
                str2 += c;
        if(str1 == "forward")
            x += stoi(str2);
        else if(str1 == "up")
            y -= stoi(str2);
        else if(str1 == "down")
            y += stoi(str2);
        else
            cout << "error" << endl;
    }

    cout << x * y << endl;
    return 0;
}
