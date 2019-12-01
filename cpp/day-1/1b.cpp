#include<iostream>
#include<string>
#include<cmath>

std::string g_mass;
int g_fuel;

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
    freopen("1b-output", "w", stdout);

    while (std::cin >> g_mass) {
        g_fuel += smartMassToFuel(std::stoi(g_mass));
    }

    std::cout << g_fuel;

    return 0;
}