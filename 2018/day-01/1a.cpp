#include <iostream>
#include <string>

int total;
std::string c;

int main() {
    freopen("../../inputs/2018/01.txt", "r", stdin);

    while (std::cin >> c) {
        total += std::stoi(c);
    }

    std::cout << total;

    return 0;
}