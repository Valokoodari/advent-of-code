#include <iostream>
#include <string>
#include <vector>

int s = 10000000;
std::string p,pc;

std::string react(std::string p) {
    for (int i = 0; i < p.size(); i++) {
        if (abs((int)p[i] - (int)p[i-1]) == 32) {
            p.erase(i-1, 2);
            i -= 2;
        }
    }
    return p;
}

int main() {
    freopen("5_input", "r", stdin);
    freopen("5b_output", "w", stdout);

    std::cin >> p;

    p = react(p);

    for (int i = 0; i < 26; i++) {
        pc = "";

        for (int j = 0; j < p.size(); j++) {
            if ((int)p[j] != i+65 && (int)p[j] != i+97) {
                pc += p[j];
            }
        }

        pc = react(pc);

        if (pc.size() < s)
            s = pc.size();
    }

    std::cout << s << "\n";

    return 0;
}