#include<iostream>
#include<vector>
#include<string>
#include<map>

#define FIND(PL, P) std::find(PL.begin(), PL.end(), P)

typedef std::pair<std::map<std::string,std::string>,std::vector<std::string> > mapAndKeys;
typedef std::map<std::string, std::string> stringMap;
typedef std::vector<std::string> stringVec;
typedef std::string string;

mapAndKeys readFile() {
    stringVec keys;
    stringMap orbits;
    freopen("6-input", "r", stdin);

    string link;
    while(std::cin >> link) {
        keys.push_back(link.substr(4,3));
        orbits[link.substr(4,3)] = link.substr(0,3);
    }

    return mapAndKeys(orbits, keys);
}

void writeFile(int a, int b) {
    freopen("6-output", "w", stdout);
    std::cout << "Part 1: " << a << "\n";
    std::cout << "Part 2: " << b;
}

int countAllOrbits(mapAndKeys mapKeys) {
    stringMap orbits = mapKeys.first;
    stringVec keys = mapKeys.second;

    int allOrbits = 0;
    for (int i = 0; i < keys.size(); i++) {
        string key = keys[i];

        while(orbits.find(key) != orbits.end()) {
            key = orbits[key];
            allOrbits++;
        }
    }

    return allOrbits;
}

int distanceBetween(mapAndKeys mapKeys, string key1, string key2) {
    stringMap orbits = mapKeys.first;
    stringVec keys = mapKeys.second;

    stringVec route;
    while (orbits.find(key1) != orbits.end()) {
        key1 = orbits[key1];
        route.push_back(key1);
    }

    int distance = -1;
    while (FIND(route, key2) == route.end()) {
        key2 = orbits[key2];
        distance++;
    }

    return distance + std::distance(route.begin(), FIND(route, key2));
}

int main() {
    freopen("6-input", "r", stdin);

    mapAndKeys mapKeys = readFile();

    int solA = countAllOrbits(mapKeys);;
    int solB = distanceBetween(mapKeys, "YOU", "SAN");

    writeFile(solA, solB);

    return 0;
}