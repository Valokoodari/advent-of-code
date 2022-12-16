#include <iostream>
#include <string>
#include <vector>

int generations = 20;
int flowers = 0;
std::string input;
std::vector<std::vector<int>> combinations;

std::vector<int> decode(std::string row) {
    std::vector<int> result;
    for (int i = 0; i < row.size(); i++) {
        if (row.substr(i,1) == "#")
            result.push_back(1);
        else
            result.push_back(0);
    }

    return result;
}

int main() {
    freopen("../../inputs/2018/12.txt", "r", stdin);

    std::getline(std::cin, input);
    combinations.push_back(decode(input.substr(input.find(": ") + 2)));
    for(int i = 0; i < generations + 5; i++) {
        combinations[0].insert(combinations[0].begin(), 0);
        combinations[0].push_back(0);
    }
    combinations.push_back(combinations[0]);
    while(std::getline(std::cin, input)) {
        if (input.substr(input.size()-1,1) == "#")
            combinations.push_back(decode(input.substr(0,5)));
    }
    
    for (int i = 0; i <= generations; i++) {
        flowers = 0;
        for (int j = 0; j < combinations[0].size(); j++) {
            flowers += combinations[0][j]*(j-generations-5);
            combinations[0][j] = 0;
        }

        for (int j = 2; j < combinations[1].size() - 2; j++) {
            std::vector<int> compare(combinations[1].begin() + j - 2, combinations[1].begin() + j + 3);
            for (int k = 2; k < combinations.size(); k++) {
                if (compare == combinations[k]) {
                    combinations[0][j] = 1;
                    break;
                }
            }
        }
        combinations[1] = combinations[0];
    }

    std::cout << flowers << "\n";

    return 0;
}