#include <iostream>
#include <sstream>
#include <vector>
#include <tuple>
#include <map>

typedef long long int ll;

ll a, b;
std::string s, nums, n;
std::vector<int> ns;
std::map<std::tuple<int, int, int>, ll> cache;

ll fs(int i, int hc, int c) {
    std::tuple k = std::make_tuple(i, hc, c);
    if (cache.find(k) != cache.end())
        return cache[k];

    ll a = 0;
    if (c == ns.size())
        a = (s.find('#', i) == std::string::npos)? 1 : 0;
    else if (i == s.size())
        a = (ns.size() == (hc == ns[c] ? c + 1 : 0)) ? 1 : 0;
    else if (s[i] == '#')
        a = (hc < ns[c]) ? fs(i + 1, hc + 1, c) : 0;
    else {
        a = hc == ns[c] ? fs(i + 1, 0, c + 1) : (hc == 0 ? fs(i + 1, 0, c) : 0);
        a += (s[i] == '.') ? 0 : fs(i + 1, hc + 1, c);
    }
    cache[k] = a;
    return a;
}

int main() {
    freopen("../../inputs/2023/12.txt", "r", stdin);
    while (std::cin >> s >> nums) {
        std::istringstream nss(nums);
        ns.clear();
        cache.clear();
        while (std::getline(nss, n, ',')) {
            ns.push_back(std::stoi(n));
        }
        a += fs(0, 0, 0);

        cache.clear();
        int nsl = ns.size();
        std::string sc = s;
        for (int i = 0; i < 4; i++) {
            s += "?" + sc;
            for (int j = 0; j < nsl; j++)
                ns.push_back(ns[j]);
        }
        b += fs(0, 0, 0);
    }

    std::cout << "Day 12: Hot Springs" << std::endl;
    std::cout << "  Part 1: " << a << std::endl;
    std::cout << "  Part 2: " << b << std::endl;
}
