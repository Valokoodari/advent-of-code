#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>
#include <map>

typedef std::map<std::string,std::vector<std::pair<std::string,int> > > recipeList;
typedef std::vector<std::pair<std::string,int> > recipe;
typedef long long int ll;

std::map<std::string, int> g_storage;
recipeList g_recipes;

void readFile() {
    std::fstream file("../../inputs/2019/14.txt", std::fstream::in);

    std::string line;
    while(std::getline(file, line)) {
        std::string productStr = line.substr(line.find("=>") + 3, line.length() - line.find("=>") - 3);
        std::string product = productStr.substr(productStr.find(" ")+1,productStr.length()-productStr.find(" ")-1);
        int quantity = std::stoi(productStr.substr(0,productStr.find(" ")));

        g_recipes[product] = std::vector<std::pair<std::string,int> >(0);
        g_recipes[product].push_back(std::pair<std::string,int>{product,quantity});
        
        line = line.substr(0, line.find("=>")-1);

        while (line.length() > 0) {
            int c = line.find(",");
            if (c == -1) {
                c = line.length();
            }
            std::string chemicalStr = line.substr(0, c);
            int s = chemicalStr.find(" ");
            std::string chemical = chemicalStr.substr(s + 1, chemicalStr.length() - s - 1);
            quantity = std::stoi(chemicalStr.substr(0, s));
            g_recipes[product].push_back(std::pair<std::string,int>{chemical,quantity});
            line.erase(0, (c != line.length())? c+2 : line.length());
        }
    }
}

void writeFile(int a, int b) {
    std::cout << "Part 1: " << a << "\n";
    std::cout << "Part 2: " << b << "\n";
}

ll calcOre(std::string product, ll amount) {
    amount = ceil((double)amount / g_recipes[product][0].second);

    recipe recipe = g_recipes[product];
    ll ore = 0;

    if (recipe[1].first == "ORE") {
        ore += recipe[1].second * amount;
    } else {
        for (int i = 1; i < recipe.size(); i++) {
            std::string chemical = recipe[i].first;
            ll required = recipe[i].second * amount;
            ore += calcOre(chemical, required - g_storage[chemical]);
            g_storage[chemical] -= required;
        }
    }
    g_storage[product] += recipe[0].second * amount;

    return ore;
}

int main() {
    readFile();

    ll solA = calcOre("FUEL", 1);
    
    g_storage.clear();

    int low = 0;
    int high = 20000000;
    while (low < high) {
        int middle = (low + high) / 2;
        if (calcOre("FUEL", middle) < 1000000000000)
            low = middle;
        else
            high = middle-1;
    }

    writeFile(solA, high);

    return 0;
}