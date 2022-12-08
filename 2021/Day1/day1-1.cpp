#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(){
    ifstream file("input.txt");

    string line;
    bool first = true;
    int prev = 0;
    int count = 0;
    
    while (getline(file, line)) {

        if(!first && stoi(line) > prev )
            count ++;
        prev = stoi(line);
        first = false;
    }
    cout << count << endl;
    return 0;
}
