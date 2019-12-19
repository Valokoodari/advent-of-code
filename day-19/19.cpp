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

   // std::vector<std::vector<int> > map;

    int solA = 0;

    std::vector<intCodeComputer> drones;
    for (int i = 1067; i < 1167; i+=99) {
        for (int j = 1712; j < 1812; j+=99) {
            intCodeComputer drone(code);
            drone.addInput(i);
            drone.addInput(j);
            int prevOp = 0;
            while (prevOp != 99) {
                prevOp = drone.step();
                if (prevOp == 4) {
                    int output = drone.getOutput();
                    std::cout << ((output == 1)? "#" : ".");
                    solA += output;
                }
            }
        }
        std::cout << "\n";
    }

    int solB = 0;
    
    
    std::cout << solA << " " << solB << "\n";

    //writeFile(solA, solB);

    return 0;
}