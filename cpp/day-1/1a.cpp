#include<iostream>
#include<string>
#include<cmath>

int g_fuel;
std::string g_mass;

int main() {
    freopen("1-input", "r", stdin);
    freopen("1a-output", "w", stdout);

    while(std::cin >> g_mass) {
        g_fuel += floor(std::stoi(g_mass)/3.0) - 2;
    }

    std::cout << g_fuel;

    return 0;
}