#include <iostream>
#include <fstream>
#include <vector>
#include <map>

int main() {
    std::vector<int> ts = std::vector<int>(30000000, -1);
    
    std::string line;
    std::fstream file("../../inputs/2020/15.txt", std::fstream::in);
    getline(file, line);
    file.close();

    int len = 0;
    std::string part;
    while (line.length() > 0) {
        int c = line.find(",");
        if (c == -1) {
            part = line.substr(0, line.length());
            ts[std::stoi(part)] = len++;
            break;
        }

        part = line.substr(0, c);
        ts[std::stoi(part)] = len++;
        line.erase(0, c+1);
    }

    int l = 3, a1 = 0;
    for (int i = 5; i < 30000000-1; i++) {
        int a = 0;
        if (ts[l] != -1) {
            a = i - ts[l];
        }

        ts[l] = i;
        l = a;

        if (i+2 == 2020) {
            a1 = l;
        }
    }

    std::cout << "Part 1: " << a1 << "\n";
    std::cout << "Part 2: " << l << "\n";
}