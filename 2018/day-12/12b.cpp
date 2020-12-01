#include <iostream>
#include <string>
#include <vector>

int generations = 200;
int generation;
long long int igens = 50000000000;
long long int flowers;
std::string input;
std::vector<int> flower(2);
std::vector<std::string> test(2);
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
    freopen("12_input", "r", stdin);
    freopen("12b_output", "w", stdout);

    std::getline(std::cin, input);
    combinations.push_back(decode(input.substr(input.find(": ") + 2)));
    for(int i = 0; i < generations * 5; i++) {
        combinations[0].insert(combinations[0].begin(), 0);
        combinations[0].push_back(0);
    }
    combinations.push_back(combinations[0]);
    while(std::getline(std::cin, input)) {
        if (input.substr(input.size()-1,1) == "#")
            combinations.push_back(decode(input.substr(0,5)));
    }
    
    for (int i = 0; i <= generations; i++) {
        flower[1] = flower[0];
        test[1] = test[0];
        test[0] = "";
        for (int j = 0; j < combinations[0].size(); j++) {
            test[0] += (combinations[0][j])? "X" : " ";
            combinations[0][j] = 0;
        }
        flower[0] = test[0].find_first_of("X");
        test[0] = test[0].substr(test[0].find_first_of("X") - 1);
        test[0] = test[0].substr(0, test[0].find_last_of("X") + 1);
        if (test[0] == test[1]) {
            generation = i;
            break;
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

    flowers = 0;
    for (int i = 0; i < test[0].size(); i++) {
        flowers += (i + flower[0] - generations * 5 + igens - generation - 1)*((test[0].substr(i,1) == "X")? 1 : 0);
    }

    std::cout << flowers;

    return 0;
}