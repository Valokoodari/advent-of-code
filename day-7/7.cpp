#include "../ICC/intCodeComputer.h"
#include <fstream>
#include <vector>
#include <string>

typedef std::string string;

std::vector<int> readFile() {
    std::ifstream file("7-input");

    std::vector<int> code;
    std::string line;
    std::getline(file, line);
    file.close();

    while (line.length() > 0) {
        int c = line.find(",");
        if (c == -1) { // There is no comma at the end of the input
            code.push_back(std::stoi(line.substr(0, line.length())));
            break;
        }
        code.push_back(std::stoi(line.substr(0, c)));
        line.erase(0, c+1);
    }

    return code;
}

void writeFile(int a, int b) {
    std::ofstream file("7-output");
    file << "Part 1: " << a << "\n";
    file << "Part 2: " << b;
    file.close();
}

int solve(std::vector<int> ampCode, int settings[]) {
    int max = 0;

    do {
        std::vector<intCodeComputer> amps;
        std::vector<int> prevOpCode(5,0);
        std::vector<int> prevOutput(5,0);

        for (int i = 0; i < 5; i++) {
            amps.push_back(intCodeComputer(ampCode));
            amps[i].addInput(settings[i]);
        }

        amps[0].addInput(0);

        while (prevOpCode[4] != 99) {
            for (int i = 0; i < amps.size(); i++) {
                prevOpCode[i] = amps[i].step();
                if (prevOpCode[i] == 4) {
                    prevOutput[i] = amps[i].getOutput();
                    amps[(i == 4)? 0 : i+1].addInput(prevOutput[i]);
                }
            }
        }
        int output = prevOutput[4];

        if (max < output)
            max = output;
    } while (std::next_permutation(settings, settings + 5));

    return max;
}

int main() {
    std::vector<int> ampCode = readFile();

    int settingsA[] = {0,1,2,3,4};
    int settingsB[] = {5,6,7,8,9};

    int solA = solve(ampCode, settingsA);
    int solB = solve(ampCode, settingsB);

    writeFile(solA, solB);
}