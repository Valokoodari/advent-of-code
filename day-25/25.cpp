#include "../ICC/intCodeComputer.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

typedef long long int ll;
typedef std::vector<long long int> intCode;

intCode readFile() {
    std::fstream file("25-input", std::fstream::in);
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

int main() {
    intCode code = readFile();

    intCodeComputer computer(code);

    int prevOp = 0;
    while (prevOp != 99) {
        prevOp = computer.step();

        if (prevOp == 4) {
            std::cout << (char)computer.getOutput();
        }

        if (prevOp == -3) {
            std::string input;
            getline(std::cin, input);
            for (char c : input)
                computer.addInput((int)c);
            computer.addInput((int)'\n');
        }
    }

    return 0;
}