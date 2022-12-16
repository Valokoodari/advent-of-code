#include <iostream>

int c,m;

int read_node(int n_child, int n_meta) {
    int sum = 0;
    for (int i = 0; i < n_child; i++) {
        std::cin >> c >> m;
        sum += read_node(c, m);
    }
    for (int i = 0; i < n_meta; i++) {
        std::cin >> m;
        sum += m;
    }

    return sum;
}

int main() {
    freopen("../../inputs/2018/08.txt", "r", stdin);

    std::cin >> c >> m;
    std::cout << read_node(c, m);

    return 0;
}