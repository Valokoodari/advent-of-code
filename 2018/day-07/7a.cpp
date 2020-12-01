#include <iostream>
#include <string>
#include <vector>

int l,m;
std::string in;
std::vector<int> c;
std::vector<std::vector<int>> o(26);

int left(std::vector<std::vector<int>> o) {
    int s = 0;
    for (int i = 0; i < o.size(); i++) {
        s += o[i].size();
    }

    return s;
}

bool contains(std::vector<int> t, int n) {
    for (int i = 0; i < t.size(); i++) {
        if (t[i] == n) {
            return true;
        }
    }
    return false;
}

int main() {
    freopen("7_input", "r", stdin);
    freopen("7a_output", "w", stdout);

    while (std::getline(std::cin, in)) {
        o[(int)in.substr(36,1)[0] - 65].push_back((int)in.substr(5, 1)[0] - 65);
    }

    while (left(o)) {
        for (int i = 0; i < o.size(); i++) {
            if (!contains(c, i)) {
                if (o[i].size() == 0) {
                    c.push_back(i);
                    break;
                }
                if (o[i].size() <= c.size()) {
                    m = 0;
                    for (int j = 0; j < o[i].size(); j++) {
                        if (contains(c, o[i][j])) {
                            m++;
                        }
                    }
                    if (m == o[i].size()) {
                        c.push_back(i);
                        o[i] = {};
                        break;;
                    }
                }
            }
        }
    }

    for (int i = 0; i < c.size(); i++) {
        std::cout << (char)(c[i] + 65);
    }

    return 0;
}