#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

std::map<int, int> readFile() {
    std::string line;
    std::map<int, int> ns;
    std::fstream file("../inputs/13.in", std::fstream::in);

    getline(file, line);
    ns.insert(std::pair<int,int>(-1, std::stoi(line)));

    std::string part;
    getline(file, line);
    file.close();

    int t = 0;
    while (line.length() > 0) {
        int c = line.find(",");
        if (c == -1) {
            part = line.substr(0, line.length());
            ns.insert(std::pair<int,int>(t, std::stoi(part)));
            break;
        } else {
            part = line.substr(0, c);
        }

        if (part != "x") {
            ns.insert(std::pair<int,int>(t, std::stoi(part)));
        }

        line.erase(0, c+1);
        t++;
    }

    return ns;
}

long long int part1(std::map<int,int> bs) {
    int st = bs[-1];

    std::vector<int> bus;
    for (std::map<int,int>::iterator it = bs.begin(); it != bs.end(); ++it) {
        bus.push_back(it->second);
    }

    for (int t = st; t < st*2; t++) {
        for (int i = 1; i < bus.size(); i++) {
            if (t % bus[i] == 0) {
                return bus[i] * (t - st);
            }
        }
    }

    return -1;
}

long long int part2(std::vector<int> k, std::vector<int> v) {
    long long int t = v[1];
    while (true) {
        long long int inc = 1, c = 0;

        for (int i = 1; i < k.size(); i++) {
            int b = k[i];
            
            if ((t+b) % v[i] == 0) {
                inc *= v[i];
                c++;
            }
        }

        if (c == k.size()-1) {
            break;
        }

        t += inc;
    }

    return t;
}

int main() {
    std::map<int,int> bs = readFile();

    std::vector<int> key;
    std::vector<int> value;
    for (std::map<int,int>::iterator it = bs.begin(); it != bs.end(); ++it) {
        key.push_back(it->first);
        value.push_back(it->second);
    }

    std::cout << part1(bs) << std::endl;
    std::cout << part2(key, value) << std::endl;

    return 0;
}