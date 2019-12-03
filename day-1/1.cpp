#include<iostream>
#include<string>
#include<cmath>

std::string g_mass;
int g_fuel1, g_fuel2;

int massToFuel(int mass) {
    int fuel = floor(mass / 3.0) - 2;

    return (fuel > 0)? fuel : 0;
}

int smartMassToFuel(int mass) {
    int fuel = 0;
    int addFuel = massToFuel(mass);

    while (addFuel > 0) {
        fuel += addFuel;
        addFuel = massToFuel(addFuel);
    }

    return fuel;
}

int main() {
    freopen("1-input", "r", stdin);
    freopen("1-output", "w", stdout);

    while (std::cin >> g_mass) {
        g_fuel1 += massToFuel(std::stoi(g_mass));
        g_fuel2 += smartMassToFuel(std::stoi(g_mass));
    }

    std::cout << "Part 1: " << g_fuel1 << "\n";
    std::cout << "Part 2: " << g_fuel2;

    return 0;
}