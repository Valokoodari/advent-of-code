#include "moon.h"
#include <numeric>

moon::moon(int startX, int startY, int startZ) {
    pos[0] = startX;
    pos[1] = startY;
    pos[2] = startZ;
}

void moon::calcVelocity(moon other) {
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

void moon::calcPosition() {
    pos[0] += vel[0];
    pos[1] += vel[1];
    pos[2] += vel[2];
}

int moon::getEnergy() {
    int potE = abs(pos[0]) + abs(pos[1]) + abs(pos[2]);
    int kinE = abs(vel[0]) + abs(vel[1]) + abs(vel[2]);

    return potE * kinE;
}