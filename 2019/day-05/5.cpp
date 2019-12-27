#include "../ICC/intCodeComputer.h"
#include <iostream>
#include <vector>
#include <string>

typedef long long int ll;

std::vector<ll> readFile() {
    std::vector<ll> code;
    std::string input;
    std::cin >> input;

    while (input.length() > 0) {
        int c = input.find(",");
        if (c == -1) { // There is no comma at the end of the input
            code.push_back(std::stoll(input.substr(0, input.length())));
            break;
        }
        code.push_back(std::stoll(input.substr(0, c)));
        input.erase(0, c+1);
    }

    return code;
}

void writeFile(int a, int b) {
    std::cout << "Part 1: " << a << "\n";
    std::cout << "Part 2: " << b;
}

int main() {
    freopen("5-input", "r", stdin);
    freopen("5-output", "w", stdout);

    std::vector<ll> code = readFile();

    ll test1 = 0;
    int prevOp = 0;
    intCodeComputer comp1(code);
    comp1.addInput(1);
    
    while (prevOp != 99) {
        prevOp = comp1.step();

        if (prevOp == 4)
            test1 = comp1.getOutput();
    }

    ll test5 = 0;
    prevOp = 0;
    intCodeComputer comp5(code);
    comp5.addInput(5);

    while (prevOp != 99) {
        prevOp = comp5.step();

        if (prevOp == 4)
            test5 = comp5.getOutput();
    }

    int solA = test1;
    int solB = test5;

    writeFile(solA, solB);

    return 0;
}