#include <iostream>
#include <string>
#include <vector>

std::string c;
std::vector<std::vector<int>> f(1100);
std::vector<std::vector<int>> cs;
int a,b,d,x,y,w,h;

int main() {
    freopen("../../inputs/2018/03.txt", "r", stdin);

    for (int i = 0; i < f.size(); i++) {
        f[i].reserve(1100);
        for (int j = 0; j < f[i].size(); i++) {
            f[i][j] = 0;
        }
    }

    while (std::getline(std::cin, c)) {
        a = c.find("@");
        b = c.find(",");
        x = std::stoi(c.substr(a+2, b-a));
        
        a = c.find(":");
        y = std::stoi(c.substr(b+1, a-b));

        b = c.find("x");
        w = std::stoi(c.substr(a+2, b-a));
        h = std::stoi(c.substr(b+1, c.size()-b));

        for (int i = x; i < x + w; i++) {
            for (int j = y; j < y + h; j++) {
                f[i][j]++;
            }
        }

        cs.push_back({x,y,w,h});
    }

    for (int i = 0; i < cs.size(); i++) {
        d = 0;
        for (a = cs[i][0]; a < cs[i][0] + cs[i][2]; a++) {
            for (b = cs[i][1]; b < cs[i][1] + cs[i][3]; b++) {
                if (f[a][b] != 1)
                    d++;
            }
        }

        if (d == 0) {
            d = i + 1;
            break;
        }
    }

    std::cout << d << "\n";

    return 0;
}