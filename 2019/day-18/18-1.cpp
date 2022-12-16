#include <iostream>
#include <fstream>
#include <string>
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
    intVec2D map = readFile("../../inputs/2019/18.txt");

    point p = findChar(map, '@');
    map[p.second-1][p.first] = -3;
    map[p.second+1][p.first] = -3;

    int solA = func2(map, '@');

    std::cout << solA << "\n";
    
    return 0;
}