#include<iostream>
#include<vector>
#include<string>

#define FIND(PL, P) std::find(PL.begin(), PL.end(), P)

typedef std::pair<int, int> intPair;
typedef std::pair<std::vector<int>,std::vector<int> > vecPair;

vecPair readFile() {
    std::string line;
    std::cin >> line;

    vecPair range(std::vector<int>(0), std::vector<int>(0));
    for (int i = 0; i < line.size() / 2; i++) {
        range.first.push_back(line[i] - '0');
        range.second.push_back(line[i+line.size()/2+1] - '0');
    }

    return range;
}

void writeFile(int a, int b) {
    std::cout << "Part 1: " << a << "\n";
    std::cout << "Part 2: " << b;
}

std::vector<int> increase(std::vector<int> a) {
    a[a.size()-1]++;
    for (int i = a.size() - 1; i >= 0; i--) {
        if (a[i] == 10) {
            a[i] = 0;
            a[i-1]++;
        }
    }
    return a;
}

bool testA(std::vector<int> pass) {
    bool hasDouble = false;

    for (int i = 0; i < pass.size() - 1; i++) {
        if (pass[i] > pass[i+1]) return false;
        if (pass[i] == pass[i+1]) hasDouble = true;
    }

    return hasDouble;
}

bool testB(std::vector<int> pass) {
    std::vector<int> count(10, 0);

    for (int i = 0; i < pass.size(); i++) {
        count[pass[i]]++;
    }

    return (FIND(count, 2) != count.end());
}

intPair solve(vecPair range) {
    intPair count(0, 0);

    while (range.first != range.second) {
        if (testA(range.first)) {
            count.first++;
            if (testB(range.first))
                count.second++;
        }
        range.first = increase(range.first);
    }

    return count;
}

int main() {
    freopen("4-input", "r", stdin);
    freopen("4-output", "w", stdout);

    vecPair range = readFile();

    intPair solutions = solve(range);

    writeFile(solutions.first, solutions.second);

    return 0;
}