#include "../ICC/intCodeComputer.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

typedef long long int ll;
typedef std::pair<int,int> point;
typedef std::vector<long long int> intCode;
typedef std::map<std::pair<int,int>, int> pointMap;

intCode readFile() {
    std::fstream file("../../inputs/2019/15.txt", std::fstream::in);
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

pointMap explore(intCode droidCode) {
    pointMap map;
    map[point(0,0)] = 2;

    std::vector<std::tuple<intCodeComputer,point,int> > droids;
    for (int i = 1; i <= 4; i++) {
        intCodeComputer droid(droidCode);
        droid.addInput(i);
        point pos(0,0);
        droids.push_back(std::tuple<intCodeComputer,point,int>(droid,pos,i));
    }
    
    while (!droids.empty()) {
        for (int i = 0; i < droids.size(); i++) {
            intCodeComputer droid = std::get<0>(droids[i]);
            point pos = std::get<1>(droids[i]);
            int dir = std::get<2>(droids[i]);

            int operation = droid.step();

            if (operation == 4) {
                int output = droid.getOutput();

                pos.first += (dir == 1)? 1 : (dir == 2)? -1 : 0;
                pos.second += (dir == 3)? -1 : (dir == 4)? 1 : 0;

                if (output == 0) {
                    map[point(pos.first,pos.second)] = 3;
                    droids.erase(droids.begin()+i);
                    i--;
                    continue;
                }

                map[point(pos.first,pos.second)] = (output == 2)? -1 : 1;

                int dirs[2] = {(dir == 1 || dir == 2)? 3 : 1, (dir == 1 || dir == 2)? 4 : 2};
                for (int j = 0; j < 2; j++) {
                    intCodeComputer nDroid = droid;
                    nDroid.addInput(dirs[j]);
                    droids.push_back(std::tuple<intCodeComputer,point,int>(nDroid,pos,dirs[j]));
                }
                droid.addInput(dir);
            }

            droids[i] = std::tuple<intCodeComputer,point,int>(droid,pos,dir);
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