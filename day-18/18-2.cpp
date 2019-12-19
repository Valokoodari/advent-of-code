#include <iostream>
#include <fstream>
#include <future>
#include <string>
#include <thread>
#include <vector>
#include <map>

typedef std::pair<int,int> point;
typedef std::vector<std::vector<int> > intVec2D;
typedef std::vector<std::vector<std::vector<int> > > intVec3D;

intVec2D readFile(const char path[]) {
    std::fstream file(path, std::fstream::in);

    intVec2D map;
    std::string line;
    while (getline(file, line)) {
        map.push_back(std::vector<int>(0));
        for (char c : line) {
            map[map.size()-1].push_back((c == '#')? -3 : (c == '.')? 0 : (int)c);
        }
    }
    file.close();

    return map;
}

void printMap(intVec2D map) {
    for (int i = 0; i < map.size(); i++) {
        for (int j = 0; j < map[i].size(); j++) {
            std::cout << ((map[j][i] == -3)? '#' : (map[j][i] == 0)? '.' : (char)map[j][i]);
        }
        std::cout << "\n";
    }
}

intVec2D fix(intVec2D map, point p) {
    map[p.second][p.first] = -3;
    map[p.second-1][p.first] = -3;
    map[p.second+1][p.first] = -3;
    map[p.second][p.first-1] = -3;
    map[p.second][p.first+1] = -3;
    map[p.second-1][p.first-1] = (int)'@';
    map[p.second-1][p.first+1] = (int)'@';
    map[p.second+1][p.first-1] = (int)'@';
    map[p.second+1][p.first+1] = (int)'@';

    return map;
}

intVec3D split(intVec2D map, point p) {
    map = fix(map, p);

    intVec3D maps(4,intVec2D(1,std::vector<int>()));
    for (int i = 0; i <= p.second; i++) {
        for (int j = 0; j <= p.first; j++) {
            maps[0][maps[0].size()-1].push_back(map[j][i]);
            maps[1][maps[1].size()-1].push_back(map[j][i+40]);
        }
        for (int j = p.first; j < map[i].size(); j++) {
            maps[2][maps[2].size()-1].push_back(map[j][i]);
            maps[3][maps[3].size()-1].push_back(map[j][i+40]);
        }
        maps[0].push_back(std::vector<int>());
        maps[1].push_back(std::vector<int>());
        maps[2].push_back(std::vector<int>());
        maps[3].push_back(std::vector<int>());
    }
    return maps;
}

point findChar(intVec2D map, char c) {
    for (int i = 0; i < map.size(); i++) {
        for (int j = 0; j < map[i].size(); j++) {
            if (map[i][j] == c) {
                return point(j, i);
            }
        }
    }
    return point(-1,-1);
}

intVec2D clearMap(intVec2D map) {
    std::vector<int> keys;
    std::vector<int> doors;
    for (int i = 0; i < map.size(); i++) {
        for (int j = 0; j < map[i].size(); j++) {
            if (map[i][j] > 94)
                keys.push_back((int)map[i][j]);
            else if (map[i][j] > 64)
                doors.push_back((int)map[i][j]);
        }
    }

    for (int i = 0; i < doors.size(); i++) {
        if (std::find(keys.begin(), keys.end(), doors[i]+32) == keys.end()) {
            point p = findChar(map, (char)doors[i]);
            map[p.second][p.first] = 0;
        }
    }

    return map;
}

std::map<char,int> findDistances(intVec2D map, point pos, int dir, int dist = 0, std::map<char,int> distances = std::map<char,int>()) {
    if (map[pos.second][pos.first] > 0) {
        distances[map[pos.second][pos.first]] = dist;
        return distances;
    }
    if (map[pos.second][pos.first] != -3) {
        if (dir != 1)
            distances = findDistances(map, point(pos.first,pos.second-1), 2, dist+1, distances);
        if (dir != 2)
            distances = findDistances(map, point(pos.first,pos.second+1), 1, dist+1, distances);
        if (dir != 3)
            distances = findDistances(map, point(pos.first-1,pos.second), 4, dist+1, distances);
        if (dir != 4)
            distances = findDistances(map, point(pos.first+1,pos.second), 3, dist+1, distances);
    }
    return distances;
}

int func2(intVec2D map, char currChar, int dist = 0) {
    point posDoor = findChar(map, (char)(currChar-32));
    if (posDoor != point(-1,-1))
        map[posDoor.second][posDoor.first] = 0;
    point posChar = findChar(map, currChar);
    map[posChar.second][posChar.first] = 0;

    std::map<char,int> distances = findDistances(map, posChar, 0, dist);

    if (distances.size() == 0) {
        return dist;
    }

    std::vector<int> asd;
    for (std::map<char,int>::iterator it = distances.begin(); it != distances.end(); it++) {
        if (it->first > 94)
            asd.push_back(func2(map, it->first, it->second));
    }

    std::sort(asd.begin(), asd.end());
    return asd[0];
}

int main() {
    intVec2D map = readFile("18-input");

    // Fix map for part 2
    point p = findChar(map, '@');
    intVec3D maps = split(map, p);
    for (int i = 0; i < maps.size(); i++) {
        maps[i] = clearMap(maps[i]);
    }

    auto q0 = std::async(func2, maps[0], '@', 0);
    auto q1 = std::async(func2, maps[1], '@', 0);
    auto q2 = std::async(func2, maps[2], '@', 0);
    auto q3 = std::async(func2, maps[3], '@', 0);

    int solB = q0.get() + q1.get() + q2.get() + q3.get();

    std::cout << solB << "\n";
    
    return 0;
}