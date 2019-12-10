#define _USE_MATH_DEFINES

#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>

typedef std::vector<std::vector<int> > intVec2D;

intVec2D readFile() {
    intVec2D map;
    
    std::fstream file("10-input", std::fstream::in);

    std::string line;
    while (std::getline(file, line)) {
        map.push_back(std::vector<int>(0));
        for (char s : line) {
            map[map.size()-1].push_back((s == '.')? 0 : -1);
        }
    }
    file.close();

    return map;
}

void writeFile(int a, int b) {
    std::fstream file("10-output", std::fstream::out);
    file << "Part 1: " << a << "\n";
    file << "Part 2: " << b;
    file.close();
}

int count(int x, int y, intVec2D map) {
    intVec2D scanner(map.size(), std::vector<int>(map[0].size(), 0));
    int count = 0;

    for (int i = -30; i <= 30; i++) {
        for (int j = -30; j <= 30; j++) {
            if (i == 0 && j == 0) {
                continue;
            }
            if (x+i < 0 || y+j < 0 || x+i >= map.size() || y+j >= map[x].size())
                continue;

            if (map[x+i][y+j] != 0) {
                int gcd;
                if (j == 0)
                    gcd = std::__algo_gcd(j,i);
                else
                    gcd = std::__algo_gcd(i,j);
                gcd = abs(gcd);
                int di = i/gcd;
                int dj = j/gcd;
                if (scanner[x+di][y+dj] == 0) {
                    scanner[x+di][y+dj]++;
                    count++;
                }
            }
        }
    }

    return count;
}

std::vector<int> solveA(intVec2D map) {
    for (int i = 0; i < map.size(); i++) {
        for (int j = 0; j < map[i].size(); j++) {
            if (map[i][j] == -1)
                map[i][j] = count(i, j, map);
        }
    }

    int max = 0;
    int x = 0;
    int y = 0;
    for (int i = 0; i < map.size(); i++) {
        for (int j = 0; j < map[i].size(); j++) {
            if (map[i][j] > max) {
                max = map[i][j];
                x = i;
                y = j;
            }
        }
    }

    return std::vector<int>{ max, x, y };
}

int solveB(intVec2D map, int x, int y) {
    std::vector<std::vector<double> > angles;

    for (int i = 0; i < map.size(); i++) {
        for (int j = 0; j < map[i].size(); j++) {
            if (j == x && i == y)
                continue;
            if (map[i][j] != 0) {
                double length = std::sqrt((j-x)*(j-x)+(i-y)*(i-y));
                double angle = std::atan2((j-x),(i-y)) * 180 / M_PI - 180;
                if (angle < 0) {
                    angle = abs(angle);
                }
                angles.push_back(std::vector<double>{ angle, length, (double)j, (double)i });
            }
        }
    }

    int destroyed = 0;
    int px = 0;
    int py = 0;
    double laser = -0.000000001;
    while (destroyed < 200) {
        double small = 360;
        int si = 0;
        for (int i = 0; i < angles.size(); i++) {
            if (angles[i][0] > laser) {
                if (angles[i][0] < small) {
                    small = angles[i][0];
                    si = i;
                } else if (abs(angles[i][0] - angles[si][0]) < 0.0001) {
                    if (angles[i][1] < angles[si][1]) {
                        si = i;
                    }
                }
            }
        }
        if (small == 360) {
            laser = -0.000000001;
            continue;
        }
        px = angles[si][2];
        py = angles[si][3];
        laser = angles[si][0];
        angles.erase(angles.begin() + si);
        destroyed++;
    }

    return 100*px+py;
}

int main() {
    intVec2D map = readFile();

    std::vector<int> solA = solveA(map);
    int solB = solveB(map, solA[2], solA[1]);

    writeFile(solA[0], solB);

    return 0;
}