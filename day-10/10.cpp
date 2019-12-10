#define _USE_MATH_DEFINES

#include <algorithm>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>

typedef std::vector<std::vector<int> > intVec2D;

intVec2D readFile() {
    std::fstream file("10-input", std::fstream::in);

    intVec2D map;
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

int countDetects(int x, int y, intVec2D map) {
    intVec2D scanner(map.size(), std::vector<int>(map[0].size(), 0));
    int count = 0;

    for (int i = -30; i <= 30; i++) {
        for (int j = -30; j <= 30; j++) {
            if (i == 0 && j == 0)
                continue;
            if (y+i < 0 || x+j < 0 || y+i >= map.size() || x+j >= map[y].size())
                continue;

            if (map[y+i][x+j] != 0) {
                int gcd;
                if (j == 0)
                    gcd = abs(std::__algo_gcd(j,i));
                else
                    gcd = abs(std::__algo_gcd(i,j));
                if (scanner[y+i/gcd][x+j/gcd] == 0) {
                    scanner[y+i/gcd][x+j/gcd]++;
                    count++;
                }
            }
        }
    }

    return count;
}

std::vector<int> solveA(intVec2D map) {
    std::vector<int> data(3,0); // detects, x, y

    for (int i = 0; i < map.size(); i++) {
        for (int j = 0; j < map[i].size(); j++) {
            if (map[i][j] != 0) {
                int detects = countDetects(j, i, map);
                if (detects > data[0]) {
                    data[0] = detects;
                    data[1] = j;
                    data[2] = i;
                }
            }
        }
    }

    return data;
}

int solveB(intVec2D map, int x, int y) {
    std::vector<std::vector<double> > asteroids; // angle, distance, x, y

    for (int i = 0; i < map.size(); i++) {
        for (int j = 0; j < map[i].size(); j++) {
            if (j == x && i == y)
                continue;
            if (map[i][j] != 0) {
                double distance = std::sqrt((j-x)*(j-x) + (i-y)*(i-y));
                double angle = abs(std::atan2((j-x),(i-y)) * 180 / M_PI - 180);
                asteroids.push_back(std::vector<double>{ angle, distance, (double)j, (double)i });
            }
        }
    }

    std::vector<int> data(3,0); // destroyed, x, y
    double laserAngle = -0.000000001;

    while (data[0] < 200) {
        double smallest = 360;
        int indexSmallest = 0;

        for (int i = 0; i < asteroids.size(); i++) {
            if (asteroids[i][0] > laserAngle) {
                if (asteroids[i][0] < smallest) {
                    smallest = asteroids[i][0];
                    indexSmallest = i;
                } else if (asteroids[i][0] == asteroids[indexSmallest][0]) {
                    if (asteroids[i][1] < asteroids[indexSmallest][1]) {
                        indexSmallest = i;
                    }
                }
            }
        }

        if (smallest == 360) {
            laserAngle = -0.000000001;
            continue;
        }

        data[1] = asteroids[indexSmallest][2];
        data[2] = asteroids[indexSmallest][3];
        laserAngle = asteroids[indexSmallest][0];
        asteroids.erase(asteroids.begin() + indexSmallest);
        data[0]++;
    }

    return 100 * data[1] + data[2];
}

int main() {
    intVec2D map = readFile();

    std::vector<int> solA = solveA(map);
    int solB = solveB(map, solA[1], solA[2]);

    writeFile(solA[0], solB);

    return 0;
}