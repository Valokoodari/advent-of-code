#include <iostream>
#include <fstream>
#include <numeric>
#include <string>
#include <vector>
#include <map>

typedef long long int ll;

class point3D {
    public:
        int x;
        int y;
        int z;

        point3D(int sx, int sy, int sz) {
            x = sx;
            y = sy;
            z = sz;
        }

        bool equals(point3D other) {
            return (x == other.x && y == other.y && z == other.z);
        }
};

class point4D {
    public:
        int a;
        int b;
        int c;
        int d;

        point4D(int sa, int sb, int sc, int sd) {
            a = sa;
            b = sb;
            c = sc;
            d = sd;
        }

        bool operator < (const point4D &other) const {
            return (a < other.a || b < other.b || c < other.c || d < other.d);
        }
};

class moon {
    public:
        int pos[3];
        int vel[3] = {0,0,0};

        moon(int startX, int startY, int startZ) {
            pos[0] = startX;
            pos[1] = startY;
            pos[2] = startZ;
        }

        void calcVel(moon other) {
            if (other.pos[0] < pos[0])
                vel[0]--;
            if (other.pos[0] > pos[0])
                vel[0]++;
            if (other.pos[1] < pos[1])
                vel[1]--;
            if (other.pos[1] > pos[1])
                vel[1]++;
            if (other.pos[2] < pos[2])
                vel[2]--;
            if (other.pos[2] > pos[2])
                vel[2]++;
        }

        void calcPos() {
            pos[0] += vel[0];
            pos[1] += vel[1];
            pos[2] += vel[2];
        }

        point3D getPos() {
            return point3D(pos[0], pos[1], pos[2]);
        }

        int getEnergy() {
            int potE = abs(pos[0]) + abs(pos[1]) + abs(pos[2]);
            int kinE = abs(vel[0]) + abs(vel[1]) + abs(vel[2]);

            return potE * kinE;
        }
};


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

int main() {
    std::vector<moon> moons = readFile();
    std::map<point4D, int> prevPosX;
    std::map<point4D, int> prevPosY;
    std::map<point4D, int> prevPosZ;
    std::map<point4D, int> prevVelX;
    std::map<point4D, int> prevVelY;
    std::map<point4D, int> prevVelZ;

    int solA = 0;

    int step = 0;
    int steps[3] = {0,0,0};
    while (steps[0] == 0 || steps[1] == 0 || steps[2] == 0) {
        point4D posX(moons[0].pos[0],moons[1].pos[0],moons[2].pos[0],moons[3].pos[0]);
        point4D posY(moons[0].pos[1],moons[1].pos[1],moons[2].pos[1],moons[3].pos[1]);
        point4D posZ(moons[0].pos[2],moons[1].pos[2],moons[2].pos[2],moons[3].pos[2]);

        point4D velX(moons[0].vel[0],moons[1].vel[0],moons[2].vel[0],moons[3].vel[0]);
        point4D velY(moons[0].vel[1],moons[1].vel[1],moons[2].vel[1],moons[3].vel[1]);
        point4D velZ(moons[0].vel[2],moons[1].vel[2],moons[2].vel[2],moons[3].vel[2]);

        if (prevPosX.find(posX) != prevPosX.end() && prevVelX.find(velX) != prevVelX.end() && steps[0] == 0)
            steps[0] = step;
        if (prevPosY.find(posY) != prevPosY.end() && prevVelY.find(velY) != prevVelY.end() && steps[1] == 0)
            steps[1] = step;
        if (prevPosZ.find(posZ) != prevPosZ.end() && prevVelZ.find(velZ) != prevVelZ.end() && steps[2] == 0)
            steps[2] = step;

        prevPosX[posX] = step;
        prevPosY[posY] = step;
        prevPosZ[posZ] = step;
        prevVelX[velX] = step;
        prevVelY[velY] = step;
        prevVelZ[velZ] = step;

        for (int i = 0; i < moons.size(); i++) {
            for (int j = 0; j < moons.size(); j++) {
                if (i == j)
                    continue;
                moons[i].calcVel(moons[j]);
            }
        }
        for (int i = 0; i < moons.size(); i++) {
            moons[i].calcPos();
        }

        step++;

        if (step == 1000) {
            for (int i = 0; i < moons.size(); i++) {
                solA += moons[i].getEnergy();
            }
        }
    }

    ll solB = std::lcm((ll)steps[0], std::lcm((ll)steps[1], (ll)steps[2]));

    writeFile(solA, solB);
}