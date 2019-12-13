#include "../ICC/intCodeComputer.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

typedef long long int ll;
typedef std::vector<long long int> intCode;
typedef std::map<std::pair<int,int>,int> pointMap;

intCode readFile() {
    std::fstream file("13-input", std::fstream::in);
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
    std::fstream file("13-output", std::fstream::out);
    file << "Part 1: " << a << "\n";
    file << "Part 2: " << b;
    file.close();
}

std::pair<int,int> solve (intCode gameCode) {
    int prevOp = 0;
    pointMap tiles;
    int ballPosX = 0;
    int paddlePos = 0;
    std::vector<int> outputs;
    std::pair<int,int> solutions(0,0);

    // Initialize the intCode Conputer
    intCodeComputer gameComputer(gameCode);
    gameComputer.setWord(0,2);

    // Run the program until it halts.
    while (prevOp != 99) {
        prevOp = gameComputer.step();

        if (prevOp == 4) {
            outputs.push_back(gameComputer.getOutput());
            if (outputs.size() == 3) {
                if (outputs[0] == -1 && outputs[1] == 0) {
                    solutions.second = outputs[2];
                } else {
                    tiles[std::pair<int,int>(outputs[0],outputs[1])] = outputs[2];
                }
                if (outputs[2] == 3)
                    paddlePos = outputs[0];
                if (outputs[2] == 4)
                    ballPosX = outputs[0];
                outputs.clear();
            }
        }

        if (prevOp == -3) {
            // Count block tiles for part one from first frame
            if (solutions.first == 0) {
                for(pointMap::iterator it = tiles.begin(); it != tiles.end(); ++it) {
                    if(it->second == 2) {
                        solutions.first++;
                    }
                }
            }

            // Send the correct joystick input to not lose
            if (ballPosX < paddlePos)
                gameComputer.addInput(-1);
            else if (ballPosX > paddlePos)
                gameComputer.addInput(1);
            else
                gameComputer.addInput(0);
        }
    }

    return solutions;
}

int main() {
    intCode gameCode = readFile();

    std::pair<int,int> solutions = solve(gameCode);

    writeFile(solutions.first, solutions.second);

    return 0;
}