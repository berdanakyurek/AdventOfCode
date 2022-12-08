#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

string most(vector<string> inp, int index){
    
    vector<string> ones;
    vector<string> zeros;
    
    for(auto x: inp)
        if(x[index] == '1')
            ones.push_back(x);
        else
            zeros.push_back(x);
    if(ones.size() >= zeros.size())
        if(ones.size() == 1)
            return ones.at(0);
        else
            return most(ones, index + 1);
    else
        if(zeros.size() == 1)
            return zeros.at(0);
        else
            return most(zeros, index + 1);
}

string least(vector<string> inp, int index){
    
    vector<string> ones;
    vector<string> zeros;
    
    for(auto x: inp)
        if(x[index] == '1')
            ones.push_back(x);
        else
            zeros.push_back(x);
    if(ones.size() < zeros.size())
        if(ones.size() == 1)
            return ones.at(0);
        else
            return least(ones, index + 1);
    else
        if(zeros.size() == 1)
            return zeros.at(0);
        else
            return least(zeros, index + 1);
}



int main(){
    ifstream file("input.txt");
    string line;
    
    vector<string> init;
    
    while (getline(file, line))
        init.push_back(line);


    string ox = most(init,0);
    string co = least(init,0);

    cout << stoi(ox, nullptr, 2) * stoi(co, nullptr, 2) <<endl;
    return 0;
}
