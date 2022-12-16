#include <iostream>
#include <vector>
#include <string>

int recipes;
std::string current;
std::vector<int> elves = {0, 1};
std::vector<int> scores = {3, 7};

int main() {
    freopen("../../inputs/2018/14.txt", "r", stdin);

    std::cin >> recipes;

    while (scores.size() < recipes + 10) {
        current = std::to_string(scores[elves[0]] + scores[elves[1]]);
        for (int i = 0; i < current.size(); i++)
            scores.push_back(std::stoi(current.substr(i, 1)));

        for (int i = 0; i < elves.size(); i++) {
            elves[i] += 1 + scores[elves[i]];
            elves[i] %= scores.size();
        }
    }

    for (int i = 0; i < 10; i++) {
        std::cout << scores[i + recipes];
    }

    return 0;
}