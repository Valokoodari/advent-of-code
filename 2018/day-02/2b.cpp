#include <iostream>
#include <vector>
#include <string>

std::string x;
std::vector<std::string> ids;
int a,s;
bool d = false;

int main() {
    freopen("2_input", "r", stdin);
    freopen("2b_output", "w", stdout);

    while (std::cin >> x && !d) {
        for (int i = 0; i < ids.size(); i++) {
            s = 0;
            for (int j = 0; j < x.size(); j++) {
                if (x[j] != ids[i][j])
                    s++;
            }
            if (s == 1) {
                d = true;
                a = i;
                break;
            }
        }

        ids.push_back(x);
    }

    std::cout << ids[ids.size() - 1] << "\n";
    std::cout << ids[a] << "\n";

    return 0;
}