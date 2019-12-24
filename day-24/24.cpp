#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>
#include <map>

typedef std::vector<std::vector<int> > intMap2D;
typedef std::map<int, std::vector<std::vector<int> > > mapPile;
typedef std::map<std::vector<std::vector<int> >,int> intMapHist;

int solveA(intMap2D eris) {
    intMapHist history;
    history[eris] = 1;

    bool noRepeat = true;
    while (noRepeat) {
        intMap2D next(5,std::vector<int>(5,0));

        for (int i = 0; i < eris.size(); i++) {
            for (int j = 0; j < eris[i].size(); j++) {
                int neighbors = 0;
                if (i-1 >= 0)
                    if (eris[i-1][j])
                        neighbors++;
                if (j-1 >= 0)
                    if (eris[i][j-1])
                        neighbors++;
                if (i+1 < eris.size())
                    if (eris[i+1][j])
                        neighbors++;
                if (j+1 < eris[i].size())
                    if (eris[i][j+1])
                        neighbors++;

                if (neighbors == 1 || (neighbors == 2 && eris[i][j] == 0))
                    next[i][j] = 1;
                else
                    next[i][j] = 0;
            }
        }

        if (history.find(next) != history.end())
            noRepeat = false;

        history[next] = 1;
        eris = next;
    }

    int biodiv = 0;
    int power = 0;
    for (int i = 0; i < eris.size(); i++) {
        for (int j = 0; j < eris[i].size(); j++) {
            if (eris[i][j])
                biodiv += std::pow(2,power);
            power++;
        }
    }

    return biodiv;
}

int solveB(intMap2D eris) {
    mapPile space;
    for (int i = -128; i <= 128; i++)
        space[i] = std::vector<std::vector<int> >(5,std::vector<int>(5,0));

    space[0] = eris;

    for (int step = 0; step < 200; step++) {
        mapPile next = space;
        for (int l = -127; l <= 127; l++) {
            for (int i = 0; i < 5; i++) {
                for (int j = 0; j < 5; j++) {
                    if (i == 2 && j == 2)
                        continue;

                    int neighbors = 0;

                    // Outer neighbors
                    if (i == 0)
                        neighbors += space[l+1][1][2];
                    if (i == 4)
                        neighbors += space[l+1][3][2];
                    if (j == 0)
                        neighbors += space[l+1][2][1];
                    if (j == 4)
                        neighbors += space[l+1][2][3];

                    // Inner neighbors
                    if (i == 1 && j == 2)
                        for (int k = 0; k < 5; k++)
                            neighbors += space[l-1][0][k];
                    if (i == 3 && j == 2)
                        for (int k = 0; k < 5; k++)
                            neighbors += space[l-1][4][k];
                    if (i == 2 && j == 1)
                        for (int k = 0; k < 5; k++)
                            neighbors += space[l-1][k][0];
                    if (i == 2 && j == 3)
                        for (int k = 0; k < 5; k++)
                            neighbors += space[l-1][k][4];

                    // Normal neighbors
                    if (i-1 >= 0)
                        neighbors += space[l][i-1][j];
                    if (j-1 >= 0)
                        neighbors += space[l][i][j-1];
                    if (i+1 < eris.size())
                        neighbors += space[l][i+1][j];
                    if (j+1 < eris[i].size())
                        neighbors += space[l][i][j+1];

                    if (neighbors == 1 || (space[l][i][j] == 0 && neighbors == 2))
                        next[l][i][j] = 1;
                    else
                        next[l][i][j] = 0;
                }
            }
        }
        space = next;
    }

    int bugs = 0;
    for (int l = -100; l <= 100; l++) {
        for (int i = 0; i < space[l].size(); i++) {
            for (int j = 0; j < space[l][i].size(); j++) {
                bugs += space[l][i][j];
            }
        }
    }

    return bugs;
}

int main() {
    std::fstream file("24-input", std::fstream::in);

    intMap2D eris;
    std::string line;
    while (getline(file, line)) {
        eris.push_back(std::vector<int>(0));
        for (int i = 0; i < line.size(); i++)
            eris[eris.size()-1].push_back((line[i] == '#')? 1 : 0);
    }
    file.close();

    int solA = solveA(eris);
    int solB = solveB(eris);

    std::cout << solA << " " << solB << "\n";

    file.open("24-output", std::fstream::out);
    file << "Part 1: " << solA << "\n";
    file << "Part 2: " << solB << "\n";
    file.close();

    return 0;
}