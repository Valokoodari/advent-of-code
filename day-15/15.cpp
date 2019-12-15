#include "../ICC/intCodeComputer.h"
#include <fstream>
#include <string>
#include <vector>
#include <map>

typedef long long int ll;
typedef std::pair<int,int> point;
typedef std::vector<long long int> intCode;
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

int nextDirection(pointMap map, point pos, int prevDir) {
    int north = map[point(pos.first+1,pos.second)];
    int south = map[point(pos.first-1,pos.second)];
    int west = map[point(pos.first,pos.second-1)];
    int east = map[point(pos.first,pos.second+1)];

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

pointMap explore(intCode droidCode) {
    intCodeComputer droid(droidCode);
    int prevDirection = 1;
    droid.addInput(1);

    pointMap map;
    point droidPos(0,0);
    map[droidPos] = 2;

    for (int i = 0; i < 2000000; i++) {
        int prevOp = droid.step();
        
        if (prevOp == 4) {
            int prevOutput = droid.getOutput();

            int a = (prevDirection == 1)? 1 : (prevDirection == 2)? -1 : 0;
            int b = (prevDirection == 3)? -1 : (prevDirection == 4)? 1 : 0;

            if (prevOutput == 0) {
                map[point(droidPos.first+a,droidPos.second+b)] = 3;
            } else {
                droidPos.first += a;
                droidPos.second += b;

                if (map.find(point(droidPos.first,droidPos.second)) == map.end())
                    map[point(droidPos.first,droidPos.second)] = (prevOutput == 2)? -1 : 1;
            }

            prevDirection = nextDirection(map, droidPos, prevDirection);
            droid.addInput(prevDirection);
        }
    }

    return map;
}

point fill(pointMap map) {
    int toStart;
    int filled = 1;
    int time = -1;

    while (filled != 0) {
        filled = 0;

        for (pointMap::iterator it = map.begin(); it != map.end(); ++it) {
            point curr = it->first;
            if (map[curr] == time) {
                for (pointMap::iterator jt = map.begin(); jt != map.end(); ++jt) {
                    point next = jt->first;
                    if (map[next] == 2)
                        toStart = abs(time);
                    if (map[next] > 0 && map[next] != 3) {
                        if (curr.first == next.first && abs(curr.second - next.second) == 1) {
                            map[next] = time - 1;
                            filled++;
                        } else if (curr.second == next.second && abs(curr.first - next.first) == 1) {
                            map[next] = time - 1;
                            filled++;
                        }
                    }
                }
            }
        }
        time--;
    }

    return point(toStart, abs(time + 2));
}

int main() {
    intCode code = readFile();
    pointMap map = explore(code);
    point solutions = fill(map);

    writeFile(solutions.first, solutions.second);

    return 0;
}