#include <iostream>
#include <string>
#include <vector>

int x, y, dir;
std::string input;
std::vector<int> collision;
std::string cart_symbols = "<^>v";
std::string rail_symbols = " -|/\\+";
std::vector<std::vector<int>> carts;
std::vector<std::vector<int>> map;
std::vector<std::vector<int>> moves = {{-1,0}, {0,-1}, {1,0}, {0,1}};

int main() {
    freopen("../../inputs/2018/13.txt", "r", stdin);

    while (std::getline(std::cin, input)) {
        map.push_back({});
        for (int i = 0; i < input.size(); i++) {
            map[y].push_back((rail_symbols.find(input[i]) + 1)?
                rail_symbols.find(input[i]) : cart_symbols.find(input[i]) % 2 + 1);
            if (cart_symbols.find(input[i]) + 1)
                carts.push_back({y, i, (int)cart_symbols.find(input[i]), 0});
        }
        y++;
    }

    while (!collision.size()) {
        sort(carts.begin(), carts.end());

        for (int i = 0; i < carts.size(); i++) {
            carts[i][0] += moves[carts[i][2]][1];
            carts[i][1] += moves[carts[i][2]][0];

            x = carts[i][1];
            y = carts[i][0];
            dir = carts[i][2];

            if (map[y][x] == 3) {
                carts[i][2] += (dir % 2)? 1 : -1;
            } else if (map[y][x] == 4) {
                carts[i][2] += (dir % 2)? -1 : 1;
            } else if (map[y][x] == 5) {
                carts[i][2] += carts[i][3] - 1;
                carts[i][3]++;
            }

            if (carts[i][2] < 0) carts[i][2] = 3;
            carts[i][2] %= 4;
            carts[i][3] %= 3;

            for (int j = 0; j < carts.size(); j++) {
                if (i == j) continue;
                if (y == carts[j][0] && x == carts[j][1]) {
                    collision = {x, y};
                    break;
                }
            }
            if (collision.size()) break;
        }
    }

    std::cout << collision[0] <<  "," << collision[1]; 
}