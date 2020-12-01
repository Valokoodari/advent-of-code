#include <iostream>
#include <vector>

int c,m;

int read_node(int n_child, int n_meta) {
    int sum = 0;
    std::vector<int> child_nodes;

    if (n_child == 0) {
        for (int i = 0; i < n_meta; i++) {
            std::cin >> m;
            sum += m;
        }
    } else {
        for (int i = 0; i < n_child; i++) {
            std::cin >> c >> m;
            child_nodes.push_back(read_node(c, m));
        }
        for (int i = 0; i < n_meta; i++) {
            std::cin >> m;
            if (m <= child_nodes.size()) {
                sum += child_nodes[m-1];
            }
        }
    }

    return sum;
}

int main() {
    freopen("8_input", "r", stdin);
    freopen("8b_output", "w", stdout);

    std::cin >> c >> m;
    std::cout << read_node(c, m);

    return 0;
}