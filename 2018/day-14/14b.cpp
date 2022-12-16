#include <iostream>
#include <vector>
#include <string>

std::string current, input;
std::vector<int> elves = {0, 1};
std::vector<int> scores = {3, 7};

int main() {
    freopen("../../inputs/2018/14.txt", "r", stdin);

    std::cin >> input;

    while (true) {
        for (int i = 0; i < input.size() && scores.size() >= input.size(); i++) {
            if (std::stoi(input.substr(i, 1)) - scores[scores.size() - input.size() + i]) {
                break;
            }
            if (i + 1 == input.size()) {
                std::cout << scores.size() - input.size() - 1;
                return 0;
            }
        }
        for (int i = 0; i < input.size() && scores.size() > input.size(); i++) {
            if (std::stoi(input.substr(i, 1)) - scores[scores.size() - input.size() - 1 + i]) {
                break;
            }
            if (i + 1 == input.size()) {
                std::cout << scores.size() - input.size() - 1;
                return 0;
            }
        }

        current = std::to_string(scores[elves[0]] + scores[elves[1]]);
        for (int i = 0; i < current.size(); i++)
            scores.push_back(std::stoi(current.substr(i, 1)));

        for (int i = 0; i < elves.size(); i++) {
            elves[i] += 1 + scores[elves[i]];
            elves[i] %= scores.size();
        }
    }
}