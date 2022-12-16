#include <iostream>
#include <vector>
#include <string>

std::string x;
std::vector<int> h(26);
int a,b = 0;
bool c,d;

int main() {
    freopen("../../inputs/2018/02.txt", "r", stdin);

    while (std::cin >> x) {
        for (int i = 0; i < x.size(); i++) {
            h[(int)x[i] - 97]++;
        }

        c = false;
        d = false;
        for (int i = 0; i < h.size(); i++) {
            if (h[i] == 2 && !c) {
                a++;
                c = true;
            } else if (h[i] == 3 && !d) {
                b++;
                d = true;
            }
            h[i] = 0;
        }
    }

    std::cout << a * b << "\n";

    return 0;
}