#include <fstream>
#include <string>
#include <vector>
#include <map>

typedef std::pair<int,int> point;
typedef std::vector<std::pair<int,int> > pointVec;
typedef std::map<std::pair<int,int>,int> pointMap;

pointMap readFile(const char path[]) {
    std::fstream file(path, std::fstream::in);

    pointMap points;

    std::string cLine;
    std::string pLine;
    int lineNumber = 0;
    while (getline(file, cLine)) {
        for (int i = 0; i < cLine.size(); i++) {
            if (cLine[i] == '.' && points.find(point(i-2,lineNumber-2)) == points.end())
                points[point(i-2,lineNumber-2)] = 1;
            if ((int)cLine[i] >= 65 && i > 0 && lineNumber > 0) {
                if ((int)pLine[i] >= 65)
                    points[point(i-2,((lineNumber > 2 && lineNumber < cLine.size()/2) || lineNumber > cLine.size()-6)? lineNumber-4 : lineNumber-1)] = (int)pLine[i]*100 + (int)cLine[i];
                if ((int)cLine[i-1] >= 65)
                    points[point(((i > 2 && i < cLine.size()/2) || i > cLine.size()-6)? i-4 : i-1,lineNumber-2)] = (int)cLine[i-1]*100 + (int)cLine[i];
            }
        }

        lineNumber++;
        pLine = cLine;
    }

    return points;
}

void writeFile(const char path[], int a, int b) {
    std::fstream file(path, std::fstream::out);
    file << "Part 1: " << a << "\n";
    file << "Part 2: " << b;
    file.close();
}

pointMap simplify(pointMap points) {
    int erased = 1;
    while (erased > 0) {
        erased = 0;
        for (pointMap::iterator it = points.begin(); it != points.end(); it++) {
            if (it->second == 1) {
                int neighbors = 0;
                if (points.find(point(it->first.first-1,it->first.second)) != points.end())
                    neighbors++;
                if (points.find(point(it->first.first+1,it->first.second)) != points.end())
                    neighbors++;
                if (points.find(point(it->first.first,it->first.second-1)) != points.end())
                    neighbors++;
                if (points.find(point(it->first.first,it->first.second+1)) != points.end())
                    neighbors++;
                if (neighbors < 2) {
                    points.erase(it->first);
                    it--;
                    erased++;
                }
            }
        }
    }

    return points;
}

std::map<point,point> findPaths(pointMap points) {
    int largestX = 0;
    int largestY = 0;
    for (pointMap::iterator it = points.begin(); it != points.end(); it++) {
        if (it->first.first > largestX)
            largestX = it->first.first;
        if (it->first.second > largestY)
            largestY = it->first.second;
    }

    std::map<point,point> paths;

    for (pointMap::iterator it = points.begin(); it != points.end(); it++) {
        if (it->second > 100) {
            int firstDir = -1;
            pointMap visited;
            pointMap currPoints;
            currPoints[it->first] = 0;
            visited[it->first] = 1;
            while (!currPoints.empty()) {
                pointMap nextPoints;
                for (pointMap::iterator jt = currPoints.begin(); jt != currPoints.end(); jt++) {
                    visited[jt->first] = 1;
                    if (points[jt->first] > 100 && jt->second != 0) {
                        int layerChange = 0;
                        int lastDir;

                        point p0(jt->first.first-1,jt->first.second);
                        point p1(jt->first.first+1,jt->first.second);
                        point p2(jt->first.first,jt->first.second-1);

                        if (points.find(p0) != points.end())
                            lastDir = 0;
                        else if (points.find(p1) != points.end())
                            lastDir = 1;
                        else if (points.find(p2) != points.end())
                            lastDir = 2;
                        else
                            lastDir = 3;
                        
                        if (lastDir == firstDir) {
                            layerChange = 0;
                        } else if (firstDir < 2) {
                            if (jt->first.first < largestX / 2) {
                                layerChange = (firstDir == 0)? 1 : -1;
                            } else {
                                layerChange = (firstDir == 0)? -1 : 1;
                            }
                        } else {
                            if (jt->first.second < largestY / 2) {
                                layerChange = (firstDir == 2)? 1 : -1;
                            } else {
                                layerChange = (firstDir == 2)? -1 : 1;
                            }
                        }
                        paths[point(it->second,points[jt->first])] = point(jt-> second,layerChange);
                        continue;
                    }

                    point p0(jt->first.first-1,jt->first.second);
                    point p1(jt->first.first+1,jt->first.second);
                    point p2(jt->first.first,jt->first.second-1);
                    point p3(jt->first.first,jt->first.second+1);

                    if (visited.find(p0) == visited.end() && points.find(p0) != points.end()) {
                        if (firstDir == -1)
                            firstDir = 0;
                        nextPoints[p0] = jt->second + 1;
                    }
                    if (visited.find(p1) == visited.end() && points.find(p1) != points.end()) {
                        if (firstDir == -1)
                            firstDir = 1;
                        nextPoints[p1] = jt->second + 1;
                    }
                    if (visited.find(p2) == visited.end() && points.find(p2) != points.end()) {
                        if (firstDir == -1)
                            firstDir = 2;
                        nextPoints[p2] = jt->second + 1;
                    }
                    if (visited.find(p3) == visited.end() && points.find(p3) != points.end()) {
                        if (firstDir == -1)
                            firstDir = 3;
                        nextPoints[p3] = jt->second + 1;
                    }
                }
                currPoints = nextPoints;
            }
        }
    }

    return paths;
}

std::map<int,int> findPathA(std::map<point,point> paths, std::map<int,int> portals, int portal) {
    for (std::map<point,point>::iterator it = paths.begin(); it != paths.end(); it++) {
        if (it->first.first == portal) {
            if (portals.find(it->first.second) == portals.end() || portals[it->first.second] > portals[portal] + it->second.first + 1) {
                portals[it->first.second] = portals[portal] + it->second.first + 1;
                portals = findPathA(paths, portals, it->first.second);
            }
        }
    }

    return portals;
}

pointMap findPathB(std::map<point,point> paths, pointMap portals, int portal, int layer = 0) {
    for (std::map<point,point>::iterator it = paths.begin(); it != paths.end(); it++) {
        if (layer < -32)
            break;
        if (it->first.first == portal) {
            if (portals.find(point(it->first.second,layer+it->second.second)) == portals.end() || portals[point(it->first.second,layer+it->second.second)] > portals[point(portal,layer)] + it->second.first + 1) {
                if ((layer + it->second.second < 0 && it->first.second != (int)'Z'*100+(int)'Z') || (it->first.second == (int)'Z'*100+(int)'Z' && layer+it->second.second == 0)) {
                    portals[point(it->first.second,layer+it->second.second)] = portals[point(portal,layer)] + it->second.first + 1;
                    portals = findPathB(paths, portals, it->first.second, layer+it->second.second);
                }
            }
        }
    }

    return portals;
}

int main() {
    pointMap points = simplify(readFile("20-input"));

    std::map<point,point> paths = findPaths(points);
    std::map<int,int> distancesA = findPathA(paths, std::map<int,int>(), (int)'A'*100+(int)'A');
    pointMap distancesB = findPathB(paths, pointMap(), (int)'A'*100+(int)'A');

    int solA = distancesA[(int)'Z'*100+(int)'Z'] - 1;
    int solB = distancesB[std::pair<int,int>((int)'Z'*100+(int)'Z',0)] - 1;

    writeFile("20-output", solA, solB);

    return 0;
}