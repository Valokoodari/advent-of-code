#include <iostream>
#include <string>

std::string p;

int main() {
    freopen("5_input", "r", stdin);
    freopen("5a_output", "w", stdout);

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