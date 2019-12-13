#include "../ICC/intCodeComputer.h"
#include <iostream>
#include <vector>
#include <string>

typedef long long int ll;

std::vector<ll> readInput() {
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

ll func(std::vector<ll> code, int noun, int verb) {
    intCodeComputer computer(code);
    computer.setWord(1, noun);
    computer.setWord(2, verb);

    while (computer.step() != 99);

    return computer.getWord(0);
}

int main() {
    freopen("2-input", "r", stdin);
    freopen("2-output", "w", stdout);

    std::vector<ll> code = readInput();

    std::cout << "Part 1: " << func(code, 12, 2) << "\n";

    int result = 19690720;
    for (int noun = 0; noun < 100; noun++) {
        int verb = result - func(code, noun, 0);
        if (verb >= 0 && verb < 100) {
            std::cout << "Part 2: " << 100 * noun + verb;
            break;
        } 
    }
}