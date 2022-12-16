#include "../ICC/intCodeComputer.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

typedef long long int ll;
typedef std::vector<long long int> intCode;

intCode readFile() {
    std::fstream file("../../inputs/2019/21.txt", std::fstream::in);
    std::string line;
    std::getline(file, line);
    file.close();

    intCode code;
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

void writeFile(int a, int b) {
    std::cout << "Part 1: " << a << "\n";
    std::cout << "Part 2: " << b << "\n";
}

int main() {
    intCode code = readFile();

    intCodeComputer droidA(code);
    intCodeComputer droidB(code);

    std::string scriptA = "NOT A J\nNOT B T\nOR T J\nNOT C T\nOR T J\nAND D J\nWALK\n";
    std::string scriptB = "NOT A J\nNOT B T\nOR T J\nNOT C T\nOR T J\nAND D J\nNOT E T\nNOT T T\nOR H T\nAND T J\nRUN\n";

    for (char c : scriptA)
        droidA.addInput(c);
    for (char c : scriptB)
        droidB.addInput(c);

    int solA = 0;
    while (solA == 0) {
        if (droidA.step() == 4) {
            int output = droidA.getOutput();
            if (output > 120)
                solA = output;
        }
    }

    int solB = 0;
    while (solB == 0) {
        if (droidB.step() == 4) {
            int output = droidB.getOutput();
            if (output > 120)
                solB = output;
        }
    }

    writeFile(solA, solB);

    return 0;
}