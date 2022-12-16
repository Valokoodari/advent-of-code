#include <iostream>
#include <string>
#include <vector>

std::string c;
std::vector<std::vector<int>> f(1100);
int a,b,d,x,y,w,h;

int main() {
    freopen("../../inputs/2018/03.txt", "r", stdin);

    for (int i = 0; i < f.size(); i++) {
        f[i].reserve(1100);
        for (int j = 0; j < f[i].size(); i++) {
            f[i][j] = 0;
        }
    }

    d = 0;
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
                if (f[i][j] == 1) 
                    d++;
                f[i][j]++;
            }
        }
    }

    std::cout << d << "\n";

    return 0;
}