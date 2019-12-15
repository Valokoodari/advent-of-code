#include <iostream>
#include "../ICC/intCodeComputer.h"
#include <fstream>
#include <string>
#include <vector>
#include <map>

typedef long long int ll;
typedef std::vector<long long int> intCode;
typedef std::vector<std::vector<int> > intVec2D;
typedef std::vector<std::pair<int,int> > pointVec;
typedef std::map<std::pair<int,int>, int> pointMap;

intCode readFile() {
    std::fstream file("15-input", std::fstream::in);
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
    std::fstream file("15-output", std::fstream::out);
    file << "Part 1: " << a << "\n";
    file << "Part 2: " << b;
    file.close();
}

int nextDirection(std::map<std::pair<int,int>, int> map, std::pair<int,int> pos, int prevDir) {
    int north = map[std::pair<int,int>(pos.first+1,pos.second)];
    int south = map[std::pair<int,int>(pos.first-1,pos.second)];
    int west = map[std::pair<int,int>(pos.first,pos.second-1)];
    int east = map[std::pair<int,int>(pos.first,pos.second+1)];

    if (prevDir == 1) {
        if (west != 3)
            return 3;
        if (north != 3)
            return 1;
        if (east != 3)
            return 4;
        return 2;
    } else if (prevDir == 2) {
        if (east != 3)
            return 4;
        if (south != 3)
            return 2;
        if (west != 3)
            return 3;
        return 1;
    } else if (prevDir == 3) {
        if (south != 3)
            return 2;
        if (west != 3)
            return 3;
        if (north != 3)
            return 1;
        return 4;
    } else if (prevDir == 4) {
        if (north != 3)
            return 1;
        if (east != 3)
            return 4;
        if (south != 3)
            return 2;
        return 3;
    }

    return -1;
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
        if (point.first == 0 && point.second == 0)
            mapped[y][x] = 5;
        else
            mapped[y][x] = tiles[point];
    }

    return mapped;
}

int main() {
    intCode code = readFile();

    intCodeComputer droid(code);
    droid.addInput(1);

    std::pair<int,int> droidPos(0,0);
    std::map<std::pair<int,int>,int> map;
    int prevDirection = 1;
    ll prevOutput = 0;
    int prevOp = 0;
    int count = 0;
    while(count < 10000000 && prevOutput != (ll)2) {
        prevOp = droid.step();
        
        if (prevOp == 4) {
            int prevOutput = droid.getOutput();

            if (prevOutput == 0) {
                switch (prevDirection) {
                    case 1: 
                        map[std::pair<int,int>(droidPos.first+1,droidPos.second)] = 3;
                        break;
                    case 2:
                        map[std::pair<int,int>(droidPos.first-1,droidPos.second)] = 3;
                        break;
                    case 3:
                        map[std::pair<int,int>(droidPos.first,droidPos.second-1)] = 3;
                        break;
                    case 4:
                        map[std::pair<int,int>(droidPos.first,droidPos.second+1)] = 3;
                        break;
                }
            } else {
                switch (prevDirection) {
                    case 1:
                        droidPos.first++;
                        break;
                    case 2:
                        droidPos.first--;
                        break;
                    case 3:
                        droidPos.second--;
                        break;
                    case 4:
                        droidPos.second++;
                        break;
                }
                if (map.find(std::pair<int,int>(droidPos.first,droidPos.second)) == map.end())
                    map[std::pair<int,int>(droidPos.first,droidPos.second)] = prevOutput;
            }

            prevDirection = nextDirection(map, droidPos, prevDirection);
            droid.addInput(prevDirection);
        }
        count++;
    }

    intVec2D mapped = mapTiles(map);
    for (int i = 0; i < mapped.size(); i++) {
        for (int j = 0; j < mapped[i].size(); j++) {
            std::cout << ((mapped[j][i] == 3)? " # " : (mapped[j][i] == 2)? " o " : (mapped[j][i] == 0)? "   " : (mapped[j][i] == 5)? " x " : " . ");
        }
        std::cout << "\n";
    }
    std::cout << "\n";

    int solA = 0;
    int solB = 0;

    //std::cout << solA << " " << solB << "\n";
    //writeFile(solA, solB);

    return 0;
}