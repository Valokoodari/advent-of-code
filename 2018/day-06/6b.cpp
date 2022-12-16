#include <iostream>
#include <string>
#include <vector>

int a;
int size = 360;
std::string c;
std::vector<std::vector<int>> cs;
std::vector<std::vector<int>> map(size);

int main() {
    freopen("../../inputs/2018/06.txt", "r", stdin);

    for (int i = 0; i < map.size(); i++) {
        map[i].resize(size);
        for (int j = 0; j < map[i].size(); j++) {
            map[i][j] = 0;
        }
    }

    while (std::getline(std::cin, c)) {
        a = c.find(",");
        cs.push_back({stoi(c.substr(0, a)), stoi(c.substr(a+1, c.size()-a-1))});
    }

    for (int i = 0; i < map.size(); i++) {
        for (int j = 0; j < map[i].size(); j++) {
            a = 0;
            for (int k = 0; k < cs.size(); k++) 
                a += abs(i-cs[k][0]) + abs(j-cs[k][1]);
            map[i][j] = a;
        }
    }

    a = 0;
    for (int i = 0; i < map.size(); i++) {
        for (int j = 0; j < map[i].size(); j++) {
            if (map[i][j] < 10000) {
                a++;
            }
        }
    }

    std::cout << a << "\n";

    return 0;
}