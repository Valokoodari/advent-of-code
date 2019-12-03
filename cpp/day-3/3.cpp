#include<iostream>
#include<vector>
#include<string>

#define FIND(PL, P) std::find(PL.begin(), PL.end(), P)

typedef std::pair<int, int> point2D;
typedef std::vector<point2D> pointVec;

std::vector<std::string> getPath(std::string line) {
    std::vector<std::string> path;

    while (line.length() > 0) {
        int c = line.find(",");
        if (c == -1) { // There is no comma at the end of the line
            path.push_back(line.substr(0, line.length()));
            break;
        }
        path.push_back(line.substr(0, c));
        line.erase(0, c+1);
    }

    return path;
}

pointVec getPoints(std::string line) {
    std::vector<std::string> path = getPath(line);
    pointVec points;

    int cx = 0;
    int cy = 0;
    for (int i = 0; i < path.size(); i++) {
        std::string dir = path[i].substr(0,1);
        int dist = stoi(path[i].substr(1, path[i].size()-1));
        for (int j = 0; j < dist; j++) {
            if (dir == "R") cx += 1;
            if (dir == "L") cx -= 1;
            if (dir == "U") cy += 1;
            if (dir == "D") cy -= 1;
            point2D point(cx, cy);
            points.push_back(point);
        }
    }

    return points;
}

pointVec getIntersects(pointVec pointsA, pointVec pointsB) {
    pointVec intersects;

    for (int i = 0; i < pointsA.size(); i++) {
        if (FIND(pointsB, pointsA[i]) != pointsB.end()) {
            intersects.push_back(point2D(pointsA[i].first, pointsA[i].second));
        }
    }

    return intersects;
}

int getSteps(pointVec points, point2D point) {
    return distance(points.begin(), FIND(points, point)) + 1;
}

int closestToCenter(pointVec points) {
    int minDist = abs(points[0].first) + abs(points[0].second);

    for (int i = 1; i < points.size(); i++) {
        int dist = abs(points[i].first) + abs(points[i].second);
        if (minDist > dist) minDist = dist;
    }

    return minDist;
}

int leastSteps(pointVec intersects, pointVec pointsA, pointVec pointsB) {
    int minSteps = pointsA.size() + pointsB.size();

    for (int i = 0; i < intersects.size(); i++) {
        int steps = getSteps(pointsA, intersects[i]);
        steps += getSteps(pointsB, intersects[i]);
        if (minSteps > steps) minSteps = steps;
    }

    return minSteps;
}

int main() {
    freopen("3-input", "r", stdin);
    freopen("3-output", "w", stdout);

    std::string line1, line2;
    std::cin >> line1 >> line2;

    pointVec points1 = getPoints(line1);
    pointVec points2 = getPoints(line2);

    pointVec intersects = getIntersects(points1, points2);

    int solA = closestToCenter(intersects);
    int solB = leastSteps(intersects, points1, points2);
    
    std::cout << "Part 1: " << solA << "\n";
    std::cout << "Part 2: " << solB << "\n";

    return 0;
}