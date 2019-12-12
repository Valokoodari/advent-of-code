#include <fstream>
#include <numeric>
#include <string>
#include <vector>
#include <array>
#include <map>

#include "moon.h"

typedef long long int ll;

std::vector<moon> readFile() {
    std::vector<moon> moons;

    std::fstream file("12-input", std::fstream::in);

    std::string line;
    while (std::getline(file, line)) {
        int eq = line.find("=");
        int c = line.find(",");
        int x = std::stoi(line.substr(eq+1,c-eq));
        line = line.substr(c+1, line.size()-c-1);

        eq = line.find("=");
        c = line.find(",");
        int y = std::stoi(line.substr(eq+1, c-eq));
        line = line.substr(c+1, line.size()-c-1);

        eq = line.find("=");
        c = line.find(">");
        int z = std::stoi(line.substr(eq+1, c-eq));

        moons.push_back(moon(x,y,z));
    }
    file.close();

    return moons;
}

void writeFile(int a, ll b) {
    std::fstream file("12-output", std::fstream::out);
    file << "Part 1: " << a << "\n";
    file << "Part 2: " << b;
    file.close();
}

std::array<int,8> getState(std::vector<moon> moons, int axis) {
    std::array<int,8> state;

    for (int i = 0; i < moons.size(); i++) {
        state[i] = moons[i].pos[axis];
        state[i+moons.size()] = moons[i].vel[axis];
    }

    return state;
}

int main() {
    std::vector<moon> moons = readFile();

    int solA = 0;
    int step = 0;
    int steps[3] = {0,0,0};
    std::map<std::array<int,8>, int> history[3];

    while (steps[0] == 0 || steps[1] == 0 || steps[2] == 0) {
        // Check if an axis repeats a previous state
        for (int i = 0; i < 3; i++) {
            std::array<int,8> currentState = getState(moons, i);

            if (history[i].find(currentState) != history[i].end() && steps[i] == 0)
                steps[i] = step;

            history[i][currentState] = step;
        }

        // Update velocities of the moons
        for (int i = 0; i < moons.size(); i++) {
            for (int j = 0; j < moons.size(); j++) {
                if (i == j)
                    continue;
                moons[i].calcVelocity(moons[j]);
            }
        }

        // Update positions of the moons
        for (int i = 0; i < moons.size(); i++) {
            moons[i].calcPosition();
        }

        step++;

        // Record total energy of the system on time step 1000
        if (step == 1000) {
            for (int i = 0; i < moons.size(); i++) {
                solA += moons[i].getEnergy();
            }
        }
    }

    // Calculate the point in time where every axis repeats a previous state at the same time
    ll solB = std::lcm((ll)steps[0], std::lcm((ll)steps[1], (ll)steps[2]));

    writeFile(solA, solB);
}