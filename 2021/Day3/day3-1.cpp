#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(){
    ifstream file("input.txt");
    string line;

    vector<int> oneCounts;
    
    int total = 0;
    while (getline(file, line)) {
        if(oneCounts.size() == 0)
            oneCounts.resize(line.length(), 0);
        int i = 0;
        for(auto bit: line){
            if(bit == '1')
                oneCounts[i] ++;
            i ++;
        }
        total ++;
    }

    string gamma = "";
    string eps = "";
    for(auto x: oneCounts)
        if(x > total-x){
            gamma += "1";
            eps += "0";
        }
        else{
            gamma += "0";
            eps += "1";
        }
    
    cout << stoi(gamma, nullptr, 2) * stoi(eps, nullptr, 2) << endl;
    return 0;
}
