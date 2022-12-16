#include <iostream>
#include <string>
#include <vector>

int marble = 0;
int player,marbles;
std::string input;
std::vector<int> players;
std::vector<int> table(1);

int highest(std::vector<int> scores) {
    int h = 0;

    for (int i = 0; i < scores.size(); i++) {
        if (scores[i] > h)
            h = scores[i];
    }

    return h;
}

int main() {
    freopen("../../inputs/2018/09.txt", "r", stdin);

    std::getline(std::cin, input);
    players.resize(stoi(input.substr(0, input.find(" "))));
    input = input.substr(input.find(" ") + 31);
    marbles = stoi(input.substr(0, input.find(" ")));

    for (int i = 1; i <= marbles; i++) {
        if (i % 23 == 0) {
            player = i % players.size();
            marble -= 7;
            if (marble < 0) {
                marble += table.size();
            }
            players[player] += i + table[marble];
            table.erase(table.begin() + marble);
        } else {
            marble++;
            marble %= table.size();
            marble++;
            if (marble == 0) {
                table.push_back(i);
            } else {
                table.insert(table.begin() + marble, i);
            }
        }
    }

    std::cout << highest(players);

    return 0;
}