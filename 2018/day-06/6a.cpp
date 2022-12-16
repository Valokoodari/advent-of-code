#include <iostream>
#include <string>
#include <vector>

int a, s, sc;
int size = 360;
std::string c;
std::vector<int> d, e;
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
        cs.push_back({stoi(c.substr(0, a)), stoi(c.substr(a + 1, c.size() - a - 1))});
    }

    for (int i = 0; i < map.size(); i++) {
        for (int j = 0; j < map[i].size(); j++) {
            d = {};
            s = size * 2;
            sc = 0;

            for (int k = 0; k < cs.size(); k++) {
                d.push_back(abs(i-cs[k][0]) + abs(j-cs[k][1]));
                if (d[k] < s) {
                    s = d[k];
                    sc = k + 1;
                }
            }
            for (int k = 0; k < d.size(); k++) {
                if (k == sc - 1)
                    continue;
                if (d[k] == s) {
                    sc = 0;
                    break;
                }
            }

            map[i][j] = sc;
        }
    }

    for (int i = 0; i <= cs.size(); i++) {
        e.push_back(0);
    }
    d = e;
    for (int i = 0; i < map.size(); i++) {
        for (int j = 0; j < map[i].size(); j++) {
            if (i > 1 && j > 1 && i < map.size() - 1 && j < map[i].size() - 1) {
                d[map[i][j]]++;
            }
            e[map[i][j]]++;
        }
    }

    s = 0;
    for (int i = 1; i < d.size(); i++) {
        if (d[i] != e[i])
            d[i] = 0;
        if (s < d[i])
            s = d[i];
    }

    std::cout << s << "\n";

    return 0;
}