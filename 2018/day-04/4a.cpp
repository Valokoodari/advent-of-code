#include <iostream>
#include <string>
#include <vector>

std::string r;
std::vector<std::string> rs;
std::vector<int> gs(5000);
std::vector<int> t(60);
int g,f,sg,st;

int main() {
    freopen("../../inputs/2018/04.txt", "r", stdin);

    while(std::getline(std::cin, r)) {
        rs.push_back(r);
    }
    std::sort(rs.begin(), rs.end());

    for (int i = 0; i < rs.size(); i++) {
        if (rs[i].find("#") == 25) {
            g = std::stoi(rs[i].substr(26, rs[i].substr(26,6).find(" ")));
        } else if (rs[i].find("falls") == 19) {
            f = std::stoi(rs[i].substr(15,2));
        } else {
            gs[g] += std::stoi(rs[i].substr(15,2)) - f;
        }
    }

    f = 0;
    for (int i = 0; i < gs.size(); i++) {
        if (gs[i] > f) {
            sg = i;
            f = gs[i];
        }
    }

    for (int i = 0; i < rs.size(); i++) {
        if (rs[i].find("#") == 25) {
            g = std::stoi(rs[i].substr(26, rs[i].substr(26,6).find(" ")));
        }
        if (g != sg)
            continue;
            
        if (rs[i].find("falls") == 19) {
            f = std::stoi(rs[i].substr(15,2));
        } else {
            for(int j = f; j < std::stoi(rs[i].substr(15,2)); j++) {
                t[j]++;
            }
        }
    }

    f = 0;
    for (int i = 0; i < t.size(); i++) {
        if (t[i] > f) {
            st = i;
            f = t[i];
        }
    }

    std::cout << sg * st << "\n";

    return 0;
}