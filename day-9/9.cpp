#include "../ICC/intCodeComputer.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

#include <thread>
#include <future>

typedef long long int ll;

std::vector<ll> readFile() {
    std::ifstream file("9-input");;

    std::vector<ll> code;
    std::string line;
    std::getline(file, line);
    file.close();

    while (line.length() > 0) {
        int c = line.find(",");
        if (c == -1) { // There is no comma at the end of the input
            code.push_back(std::stoll(line.substr(0, line.length())));
            break;
        }
        code.push_back(std::stoll(line.substr(0, c)));
        line.erase(0, c+1);
    }

    return code;
}

void writeFile(ll a, ll b) {
    std::fstream file("9-output", std::fstream::out);
    file << "Part 1: " << a << "\n";
    file << "Part 2: " << b << "\n";
    file.close();
}

ll solve(std::vector<ll> code, ll input) {
    intCodeComputer boost(code);
    boost.addInput(input);

    while (boost.step() != 99);

    return boost.getOutput();
}

int main() {
    std::vector<ll> code = readFile();

    auto solA = std::async(solve, code, 1);
    auto solB = std::async(solve, code, 2);

    writeFile(solA.get(), solB.get());

    return 0;
}