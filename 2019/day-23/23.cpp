#include "../ICC/intCodeComputer.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

typedef long long int ll;
typedef std::vector<long long int> intCode;

intCode readFile() {
    std::fstream file("../../inputs/2019/23.txt", std::fstream::in);
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

    std::vector<intCodeComputer> computers;
    for (int i = 0; i < 50; i++)
        computers.push_back(intCodeComputer(code, i));

    ll solA = 0;
    ll solB = 0;

    int natPointer = 0;
    int idleCounter = 0;
    std::map<ll,std::vector<ll> > natData;

    while (solB == 0) {
        for (int i = 0; i < computers.size(); i++) {
            std::vector<ll> outputs;
            bool ioActivity = false;

            while (!ioActivity) {
                int prevOp = computers[i].step();

                if (prevOp == 4) {
                    ll output = computers[i].getOutput();
                    outputs.push_back(output);
                    
                    if (outputs.size() == 3) {
                        if (outputs[0] < 50 && outputs[0] >= 0)
                            computers[outputs[0]].addInput({ outputs[1], outputs[2] });
                        else if (outputs[0] == 255) {
                            natData[natPointer] = std::vector<ll>{ outputs[1], outputs[2] };
                            if (solA == 0)
                                solA = outputs[2];
                        }

                        ioActivity = true;
                        idleCounter = 0;
                    }
                }

                if (prevOp == -3) {
                    idleCounter++;
                    ioActivity = true;
                    computers[i].addInput(-1);
                }
            }
        }

        if (idleCounter > 6000 && !natData[natPointer].empty()) {
            computers[0].addInput(natData[natPointer]);

            if (natPointer > 0) {
                if (natData[natPointer][1] == natData[natPointer-1][1])
                    solB = natData[natPointer][1];
                natData[natPointer-1] = natData[natPointer];
                natData[natPointer].clear();
                natPointer--;
            }

            natPointer++;
        }
    }

    writeFile(solA, solB);

    return 0;
}