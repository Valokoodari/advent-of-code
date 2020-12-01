#include <iostream>
#include <string>
#include <vector>

std::string r;
std::vector<std::string> rs;
std::vector<std::vector<int>> gs(5000);
int g,f,t,sg,st;

int main() {
    freopen("4_input", "r", stdin);
    freopen("4b_output", "w", stdout);

    for (int i = 0; i < gs.size(); i++) {
        gs[i].resize(60);
        for (int j = 0; j < gs[i].size(); j++) {
            gs[i][j] = 0;
        }
    }

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
            for (int j = f; j < std::stoi(rs[i].substr(15,2)); j++) {
                gs[g][j]++;
            }
        }
    }

    t = 0;
    for (int i = 0; i < gs.size(); i++) {
        for (int j = 0; j < gs[i].size(); j++) {
            if (gs[i][j] > t) {
                t = gs[i][j];
                sg = i;
                st = j;
            }
        }
    }

    std::cout << sg * st << "\n";

    return 0;
}