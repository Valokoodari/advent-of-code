#include "../ICC/intCodeComputer.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

typedef long long int ll;
typedef std::vector<long long int> intCode;

intCode readFile() {
    std::fstream file("23-input", std::fstream::in);
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
    std::fstream file("23-output", std::fstream::out);
    file << "Part 1: " << a << "\n";
    file << "Part 2: " << b;
    file.close();
}

int main() {
    intCode code = readFile();

    std::vector<intCodeComputer> computers;
    for (int i = 0; i < 50; i++) {
        intCodeComputer icc(code);
        computers.push_back(icc);
        computers[i].addInput(i);
    }

    ll solA = 0;
    ll solB = 0;

    std::map<ll,std::vector<ll> > natData;
    int natPointer = 0;
    int idleCounter = 0;
    std::map<ll,std::vector<ll> > outputs;
    while (solB == 0) {
        for (int i = 0; i < computers.size(); i++) {
            int prevOp = computers[i].step();
            if (prevOp == 4) {
                ll output = computers[i].getOutput();
                outputs[i].push_back(output);
                if (outputs[i].size() == 3) {
                    idleCounter = 0;
                    if (outputs[i][0] < 50 && outputs[i][0] >= 0) {
                        computers[outputs[i][0]].addInput(outputs[i][1]);
                        computers[outputs[i][0]].addInput(outputs[i][2]);
                    }
                    if (outputs[i][0] == 255) {
                        natData[natPointer] = std::vector<ll>{ outputs[i][1], outputs[i][2] };
                        if (solA == 0)
                            solA = outputs[i][2];
                    }
                    outputs[i].clear();
                }
            }
            if (prevOp == -3) {
                idleCounter++;
                computers[i].addInput(-1);
            }
        }

        if (idleCounter > 10000 && !natData[natPointer].empty()) {
            idleCounter = 0;
            computers[0].addInput(natData[natPointer][0]);
            computers[0].addInput(natData[natPointer][1]);
            if (natPointer > 0)
                if (natData[natPointer][1] == natData[natPointer-1][1])
                    solB = natData[natPointer][1];
            natPointer++;
            natData[natPointer] = std::vector<ll>(0);
        }
    }

    writeFile(solA, solB);

    return 0;
}