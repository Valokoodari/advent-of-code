#include <iostream>
#include <string>
#include <vector>

int t,ne;
std::string in;
std::vector<int> c,d;
std::vector<std::vector<int>> o(26);
std::vector<std::vector<int>> e(5);

bool contains(std::vector<int> ar, int n) {
    for (int i = 0; i < ar.size(); i++) {
        if (ar[i] == n) {
            return true;
        }
    }
    return false;
}

int next(std::vector<std::vector<int>> o, std::vector<int> c, std::vector<int> d) {
    for (int i = 0; i < o.size(); i++) {
        if (!contains(d, i)) {
            if (o[i].size() == 0) {
                return i;
            }
            if (o[i].size() <= c.size()) {
                int m = 0;
                for (int j = 0; j < o[i].size(); j++) {
                    if (contains(c, o[i][j])) {
                        m++;
                    }
                }
                if (m == o[i].size()) {
                    return i;
                }
            }
        }
    }
    return -1;
}

int main() {
    freopen("7_input", "r", stdin);
    freopen("7b_output", "w", stdout);

    while (std::getline(std::cin, in)) {
        o[(int)in.substr(36,1)[0] - 65].push_back((int)in.substr(5, 1)[0] - 65);
    }

    for (int i = 0; i < e.size(); i++) {
        e[i] = {-1, -1};
    }

    t = 0;
    while (c.size() < o.size()) {
        for (int i = 0; i < e.size(); i++) {
            if (e[i][0] == -1) {
                ne = next(o,c,d);
                if (ne != -1) {
                    d.push_back(ne);
                    e[i] = {60 + ne, ne};
                }
                continue;
            } else if (e[i][0] == 0) {
                c.push_back(e[i][1]);
                e[i] = {-1, -1};
                i = -1;
                continue;
            }
            e[i][0]--;
        }
        t++;
    }

    std::cout << t << "\n";

    return 0;
}