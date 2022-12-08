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
    int window[3] = {0, 0, 0};
    int i = 0;
    while (getline(file, line)) {
        window[0] = window[1];
        window[1] = window[2];
        window[2] = stoi(line);

        int sum = 0;
        for(int x: window)
            sum += x;
        
        
        if(!first && sum > prev )
            count ++;
        prev = sum;
        if(i == 2)
            first = false;
        i ++;
    }
    cout << count << endl;
    return 0;
}
