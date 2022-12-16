#include <iostream>
#include <vector>
#include <string>

int t = 0;
int size = 60000;
int xd, yd, x, y;
std::string input;
std::vector<int> limits(4);
std::vector<int> prev = {-size, size, -size, size};
std::vector<std::vector<int>> points;
std::vector<std::vector<int>> result;

int main() {
    freopen("../../inputs/2018/10.txt", "r", stdin);

    while (std::getline(std::cin, input)) {
        points.push_back({
            stoi(input.substr(10, 6)),
            stoi(input.substr(18, 6)),
            stoi(input.substr(36 ,2)),
            stoi(input.substr(40 ,2))
        });
    }

    while (result.size() == 0) {
        limits = {-size, size, -size, size};

        for (int i = 0; i < points.size(); i++) {
            if (points[i][0] > limits[0])
                limits[0] = points[i][0];
            if (points[i][0] < limits[1])
                limits[1] = points[i][0];
            if (points[i][1] > limits[2])
                limits[2] = points[i][1];
            if (points[i][1] < limits[3])
                limits[3] = points[i][1];
            points[i][0] += points[i][2];
            points[i][1] += points[i][3];
        }

        if (t == 0) {
            prev = limits;
        }

        xd = prev[1] - prev[0];
        yd = prev[3] - prev[2];

        if (abs(xd) < abs(limits[1] - limits[0]) || abs(yd) < abs(limits[3] - limits[2])) {
            result.resize(abs(yd) + 1);
            for (int i = 0; i < result.size(); i++) {
                result[i].resize(abs(xd) + 1);
                for (int j = 0; j < result[i].size(); j++) {
                    result[i][j] = 0;
                }
            }

            for (int i = 0; i < points.size(); i++) {
                x = points[i][0] - 2 * points[i][2] - prev[1];
                y = points[i][1] - 2 * points[i][3] - prev[3];
                result[y][x] = 1;
            }

            break;
        }

        prev = limits;

        t++;
    }

    for (int i = 0; i < result.size(); i++) {
        for (int j = 0; j < result[i].size(); j++) {
            if (result[i][j] == 0) {
                std::cout << " ";
            } else {
                std::cout << "#";
            }
        }
        std::cout << "\n";
    }

    std::cout << "\n" << "Seconds: " << t - 1;

    return 0;
}