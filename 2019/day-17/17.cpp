#include "../ICC/intCodeComputer.h"
#include <fstream>
#include <string>
#include <vector>
#include <map>

typedef long long int ll;
typedef std::vector<long long int> intCode;
typedef std::vector<std::vector<int> > intVec2D;

intCode readFile() {
    std::fstream file("17-input", std::fstream::in);
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
    std::fstream file("17-output", std::fstream::out);
    file << "Part 1: " << a << "\n";
    file << "Part 2: " << b;
    file.close();
}

intVec2D createMap(std::string display) {
    intVec2D map(1,std::vector<int>(0));

    int y = 0;
    for (int i = 0; i < display.length()-1; i++) {
        if (display[i] == '\n') {
            map.push_back(std::vector<int>(0));
            y++;
        } else {
            map[y].push_back((display[i] == '.')? 0 : (display[i] == '#')? 1 : 2);
        }
    }

    return map;
}

int calibrate(intVec2D map) {
    int sum = 0;
    for (int i = 1; i < map.size()-1; i++)
        for (int j = 1; j < map[i].size()-1; j++)
            if (map[i][j] != 0 && map[i-1][j] != 0 && map[i+1][j] != 0)
                if (map[i][j-1] != 0 && map[i][j+1] != 0)
                    sum += i*j;

    return sum;
}

std::string findPath(intVec2D map) {
    // TODO
    return "A,C,A,B,A,B,C,B,B,C\nL,4,L,4,L,10,R,4\nR,4,L,10,R,10\nR,4,L,4,L,4,R,8,R,10\nn\n";
}

int main() {
    intCode code = readFile();
    intCodeComputer robot(code);
    robot.setWord(0,2);

    std::string display = "";
    int solA = 0;
    int solB = 0;
    int prevOp = 0;
    while (prevOp != 99) {
        prevOp = robot.step();

        if (prevOp == 4) {
            int currChar = robot.getOutput();
            if (solB == 10 && currChar == 10 && solA == 0) {
                intVec2D map = createMap(display);
                solA = calibrate(map);
                std::string path = findPath(map);
                for (char c : path)
                    robot.addInput((int)c);
            }
            if (currChar < 200)
                display += (char)currChar;
            solB = currChar;
        }
    }

    //std::cout << display << "\n";
    //std::cout << solA << " " << solB << "\n";

    writeFile(solA, solB);

    return 0;
}