#include <iostream>
#include <vector>
#include <string>

int serial;
int size = 300;
std::vector<int> power = {0, 0, 0, 0};
std::vector<std::vector<int>> cells(size);

int main() {
    freopen("../../inputs/2018/11.txt", "r", stdin);

    std::cin >> serial;

    for (int i = 0; i < cells.size(); i++) {
        cells[i].resize(size);
        for (int j = 0; j < cells[i].size(); j++) {
            cells[i][j] = (i + 11) * (i * (j + 1) + 11 * j + serial + 11);
            cells[i][j] = stoi(std::to_string(cells[i][j]).substr(std::to_string(cells[i][j]).size()-3,1));
            cells[i][j] -= 5;
        }
    }

    for (int i = 0; i < cells.size() - 2; i++) {
        for (int j = 0; j < cells[i].size() - 2; j++) {
            power[0] = 0;
            for (int a = 0; a < 3; a++) {
                for (int b = 0; b < 3; b++) {
                    power[0] += cells[i+a][j+b];
                }
            }
            if (power[0] > power[1]) {
                power = {power[0], power[0], i, j};
            }
        }
    }

    std::cout << power[2] + 1 << "," << power[3] + 1;

    return 0;
}