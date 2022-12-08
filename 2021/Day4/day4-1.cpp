#include <iostream>
#include <fstream>
#include <map>
#include <vector>

using namespace std;

int main(){
    ifstream file("input.txt");
    string line;
    
    string firstLine;
    getline(file, firstLine);
    getline(file, line);
    
    int cardNo = 0;
    int row = 0;
    
    vector<map<string, pair<int, int>>> dictList;
    map<string, pair<int, int>> d;

    vector<vector<string>> rows;
    vector<vector<string>> cols;
    vector<string> v1;
    vector<string> v2;
    rows.push_back(v1);
    cols.push_back(v2);
    
    dictList.push_back(d);
    while (getline(file, line)) {
        if(line == ""){
            cardNo += 1;
            row = 0;
            map<string, pair<int, int>> new_d;
            dictList.push_back(new_d);
            vector<string> v1;
            vector<string> v2;
            rows.push_back(v1);
            cols.push_back(v2);
            continue;
        }

        rows[cardNo].push_back("11111");
        cols[cardNo].push_back("11111");
        int start = 0;
        int end = line.find(" ");
        int col = 0;
        line += " ";
        while (end != -1) {
            string val = line.substr(start, end - start);
            start = end + 1;
            end = line.find(" ", start);
            if(val == "")
                continue;
            pair<int,int> p;
            p.first = row;
            p.second = col;
            dictList.at(cardNo).insert(pair<string, pair<int, int>>(val, p));
            col ++;
        }
        row ++ ;
                
    }

    cout << rows.size() << " " << cols.size() << endl;
    line = firstLine;
    int start = 0;
    int end = line.find(",");
    int col = 0;
    line += ",";

    int score = 0;
    while (end != -1) {
        string val = line.substr(start, end - start);
        start = end + 1;
        end = line.find(",", start);

        cout << val << endl;
        int i = 0;
        for(auto card: dictList) {
            //cout << "ho" << endl;
            if(card.find(val) != card.end()){
                pair<int, int> p2 = card[val];
                //cout << p2.first << "-" << p2.second << endl;
                rows[i][p2.first][p2.second] = '0';
                cols[i][p2.second][p2.first] = '0';

                if(stoi(rows[i][p2.first]) == 0 or stoi(cols[i][p2.second]) == 0){
                    cout << "card " << i << endl;
                    return 0;
                }
                    
            }
                
            i ++;
        }
    }
    return 0;
}
