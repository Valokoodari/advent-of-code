#include <iostream>
#include <string>

std::string p;

int main() {
    freopen("../../inputs/2018/05.txt", "r", stdin);

    std::cin >> p;

    for (int i = 1; i+1 < p.size(); i++) {
        if (abs((int)p[i] - (int)p[i-1]) == 32) {
            p.erase(i-1, 2);
            i -= 2;
        }
    }

    std::cout << p.size() << "\n";

    return 0;
}