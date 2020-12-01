#include <iostream>
#include <vector>
#include <string>

int recipes;
std::string current;
std::vector<int> elves = {0, 1};
std::vector<int> scores = {3, 7};

int main() {
    freopen("14_input", "r", stdin);
    freopen("14a_output", "w", stdout);

    std::cin >> recipes;

    while (true) {
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