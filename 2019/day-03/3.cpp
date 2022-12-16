#include<iostream>
#include<vector>
#include<string>

#define FIND(PL, P) std::find(PL.begin(), PL.end(), P)

typedef std::pair<int, int> point2D;
typedef std::vector<point2D> pointVec;
typedef std::vector<std::vector<int> > vector2D;

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

vector2D mapPoints(pointVec points) {
    vector2D map(20000, std::vector<int> (20000, 0));

    for (point2D point : points) {
        map[point.first+10000][point.second+10000]++;
    }

    return map;
}

pointVec getIntersects(pointVec pointsA, pointVec pointsB) {
    pointVec intersects;

    vector2D map = mapPoints(pointsA);
    for (point2D point : pointsB) {
        if (map[point.first+10000][point.second+10000] != 0) {
            intersects.push_back(point);
        }
    }

    return intersects;
}

int getSteps(pointVec points, point2D point) {
    return distance(points.begin(), FIND(points, point)) + 1;
}

int closestToCenter(pointVec points) {
    int minDist = abs(points[0].first) + abs(points[0].second);

    for (point2D point : points) {
        int dist = abs(point.first) + abs(point.second);
        if (minDist > dist) minDist = dist;
    }

    return minDist;
}

int leastSteps(pointVec intersects, pointVec pointsA, pointVec pointsB) {
    int minSteps = pointsA.size() + pointsB.size();

    for (point2D intersect : intersects) {
        int steps = getSteps(pointsA, intersect);
        steps += getSteps(pointsB, intersect);
        if (minSteps > steps) minSteps = steps;
    }

    return minSteps;
}

int main() {
    freopen("../../inputs/2019/03.txt", "r", stdin);

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