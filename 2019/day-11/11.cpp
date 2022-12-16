#include "../ICC/intCodeComputer.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

typedef std::vector<long long int> intCode;
typedef std::vector<std::vector<int> > intVec2D;
typedef std::vector<std::pair<int,int> > pointVec;
typedef std::map<std::pair<int,int>, int> pointMap;

intCode readFile() {
    std::ifstream file("../../inputs/2019/11.txt");;

    intCode code;
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

void writeFile(int a, intVec2D b) {
    std::cout << "Part 1: " << a << "\n";
    std::cout << "Part 2:\n";
    for (int i = 0; i < b.size(); i++) {
        for (int j = 0; j < b[i].size(); j++) {
            std::cout << ((b[i][j] == 1)? "##" : "  ");
        }
        std::cout << "\n";
    }
}

pointMap runRobot(intCode code, int startTile) {
    pointMap hull;

    auto robot = intCodeComputer(code);
    robot.addInput(startTile);

    std::vector<int> outputs;
    std::pair<int, int> robotPos; // x, y
    int robotData[] = {0, 0, 0}; // orientation, prevOp, tiles painted

    while (robotData[1] != 99) {
        robotData[1] = robot.step();

        if (robotData[1] == -3) {
            if (hull.find(robotPos) == hull.end())
                robot.addInput(0);
            else
                robot.addInput(hull[robotPos]);
        } else if (robotData[1] == 4) {
            outputs.push_back(robot.getOutput());
        }

        if (outputs.size() == 2) {
            hull[robotPos] = outputs[0];

            robotData[0] += (outputs[1])? -1 : 1;
            robotData[0] = (robotData[0] + 4) % 4;

            outputs.pop_back();
            outputs.pop_back();

            robotPos.first += (robotData[0] == 0)? 1 : (robotData[0] == 2)? -1 : 0;
            robotPos.second += (robotData[0] == 1)? 1 : (robotData[0] == 3)? -1 : 0;
        }
    }

    return hull;
}

intVec2D mapTiles(pointMap tiles) {
    int minMaxPos[] = {100, -100, 100, -100}; // minY, maxY, minX, maxX
    pointVec painted;
    for(pointMap::iterator it = tiles.begin(); it != tiles.end(); ++it) {
        if (tiles[it->first] == 0)
            continue;
        std::pair<int,int> point = it->first;
        painted.push_back(point);
        if (point.first < minMaxPos[0])
            minMaxPos[0] = point.first;
        if (point.first > minMaxPos[1])
            minMaxPos[1] = point.first;
        if (point.second < minMaxPos[2])
            minMaxPos[2] = point.second;
        if (point.second > minMaxPos[3])
            minMaxPos[3] = point.second;
    }

    intVec2D mapped(abs(minMaxPos[0] - minMaxPos[1])+1, std::vector<int>(abs(minMaxPos[2] - minMaxPos[3])+1, 0));
    for (int i = 0; i < painted.size(); i++) {
        std::pair<int,int> point = painted[i];
        int x = mapped[0].size() - 1 - (point.second + ((minMaxPos[2] < 0)? abs(minMaxPos[2]) : 0));
        int y = mapped.size() - 1 - (point.first + ((minMaxPos[0] < 0)? abs(minMaxPos[0]) : 0));
        mapped[y][x] = 1;
    }

    return mapped;
}

int main() {
    intCode code = readFile();

    pointMap tilesA = runRobot(code, 0);
    int solA = tilesA.size();

    pointMap tilesB = runRobot(code, 1);
    intVec2D hullB = mapTiles(tilesB);

    writeFile(solA, hullB);

    return 0;
}