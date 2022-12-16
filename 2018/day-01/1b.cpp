#include <iostream>
#include <vector>
#include <string>

int total;
bool d = false;
std::string c;
std::vector<int> input;
std::vector<int> h = {0};

int main() {
    freopen("../../inputs/2018/01.txt", "r", stdin);

    while (std::cin >> c) {
        input.push_back(std::stoi(c));
    }

    while(!d) {
        for (int i = 0; i < input.size() && !d; i++) {
            total += input[i];

            for (int j = 0; j < h.size(); j++) {
                if (h[j] == total) {
                    d = true;
                    break;
                }
            }

            h.push_back(total);
        }
    }

    std::cout << total;

    return 0;
}