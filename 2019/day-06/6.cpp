#include<iostream>
#include<vector>
#include<string>
#include<thread>
#include<future>
#include<map>

#define FIND(PL, P) std::find(PL.begin(), PL.end(), P)

typedef std::pair<std::map<std::string,std::string>,std::vector<std::string> > mapAndKeys;
typedef std::map<std::string, std::string> stringMap;
typedef std::map<std::string, int> strIntMap;
typedef std::vector<std::string> stringVec;
typedef std::string string;

mapAndKeys readFile() {
    stringVec keys;
    stringMap orbits;
    freopen("../../inputs/2019/06.txt", "r", stdin);

    string link;
    while(std::cin >> link) {
        keys.push_back(link.substr(4,3));
        orbits[link.substr(4,3)] = link.substr(0,3);
    }

    return mapAndKeys(orbits, keys);
}

void writeFile(int a, int b) {
    std::cout << "Part 1: " << a << "\n";
    std::cout << "Part 2: " << b << "\n";
}

int countAllOrbits(mapAndKeys mapKeys) {
    stringMap orbits = mapKeys.first;
    stringVec keys = mapKeys.second;

    strIntMap test;
    int allOrbits = 0;

    for (int i = 0; i < keys.size(); i++) {
        string key = keys[i];
        int curOrbits = 0;

        while(orbits.find(key) != orbits.end()) {
            key = orbits[key];
            if (test.find(key) != test.end()) {
                curOrbits += test[key] + 1;
                break;
            }
            curOrbits++;
        }
        test[keys[i]] = curOrbits;
        allOrbits += curOrbits;
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
    mapAndKeys mapKeys = readFile();

    auto solA = std::async(countAllOrbits, mapKeys);
    int solB = distanceBetween(mapKeys, "YOU", "SAN");

    writeFile(solA.get(), solB);

    return 0;
}