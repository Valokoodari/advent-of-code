#include <iostream>
#include <vector>
#include <string>

int serial, max;
int size = 300;
std::vector<int> current;
std::vector<int> power = {0, 0, 0, 0};
std::vector<std::vector<int>> cells(size);

std::vector<int> power_square(std::vector<std::vector<int>> fuel_grid, int length) {
    int sum;
    std::vector<int> result(3);
    
    for (int i = 0; i < fuel_grid.size() - (length - 1); i++) {
        for (int j = 0; j < fuel_grid[i].size() - (length - 1); j++) {
            sum = 0;
            for (int a = 0; a < length; a++) {
                for (int b = 0; b < length; b++) {
                    sum += fuel_grid[i+a][j+b];
                }
            }
            if (sum > result[0]) {
                result = {sum, i, j};
            }
        }
    }

    return result;
}

int main() {
    freopen("11_input", "r", stdin);
    freopen("11b_output", "w", stdout);

    std::cin >> serial;

    for (int i = 0; i < cells.size(); i++) {
        cells[i].resize(size);
        for (int j = 0; j < cells[i].size(); j++) {
            cells[i][j] = (i + 11) * (i * (j + 1) + 11 * j + serial + 11);
            cells[i][j] = stoi(std::to_string(cells[i][j]).substr(std::to_string(cells[i][j]).size()-3,1));
            cells[i][j] -= 5;
        }
    }

    for (int i = 1; i < 300; i++) {
        current = power_square(cells, i);
        if (current[0] > power[0]) {
            power = {current[0], i, current[1], current[2]};
        }
    }

    std::cout << power[2] + 1 << "," << power[3] + 1 << "," << power[1];

    return 0;
}