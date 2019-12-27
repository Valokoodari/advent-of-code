#include "../ICC/intCodeComputer.h"
#include <fstream>
#include <string>
#include <vector>
#include <map>

typedef long long int ll;
typedef std::vector<long long int> intCode;

intCode readFile() {
    std::fstream file("19-input", std::fstream::in);
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
    std::fstream file("19-output", std::fstream::out);
    file << "Part 1: " << a << "\n";
    file << "Part 2: " << b;
    file.close();
}

int main() {
    intCode code = readFile();

    int solA = 0;

    for (int i = 0; i < 50; i++) {
        for (int j = 0; j < 50; j++) {
            intCodeComputer drone(code);
            drone.addInput(j);
            drone.addInput(i);

            int prevOp = 0;
            while (prevOp != 4) {
                prevOp = drone.step();
                if (prevOp == 4)
                    solA += drone.getOutput();
            }
        }
    }

    int corners = 0;
    std::pair<int,int> pos(100,100);
    while (corners < 4) {
        corners = 0;
        std::vector<intCodeComputer> drones;
        for (int i = 0; i < 4; i++) {
            drones.push_back(intCodeComputer(code));
        }

        drones[0].addInput(pos.first+99);
        drones[0].addInput(pos.second);
        drones[1].addInput(pos.first);
        drones[1].addInput(pos.second);
        drones[2].addInput(pos.first);
        drones[2].addInput(pos.second+99);
        drones[3].addInput(pos.first+99);
        drones[3].addInput(pos.second+99);

        for (int i = 0; i < drones.size(); i++) {
            int prevOp = 0;
            while (prevOp != 4) {
                prevOp = drones[i].step();
                if (prevOp == 4) {
                    corners += drones[i].getOutput();
                    if (i == 0) {
                        if (corners == 0)
                            pos.second++;
                        else
                            pos.first++;
                    }
                }
            }
        }
    }
    
    int solB = 10000 * (pos.first - 1) + pos.second;

    writeFile(solA, solB);

    return 0;
}