#include <iostream>
#include <string>

int total;
std::string c;

int main() {
    // Input and output files
    freopen("1_input", "r", stdin);
    freopen("1a_output", "w", stdout);

    while (std::cin >> c) {
        total += std::stoi(c);
    }

    std::cout << total;

    return 0;
}