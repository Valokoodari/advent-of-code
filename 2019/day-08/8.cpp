#include<iostream>
#include<fstream>
#include<vector>
#include<string>

typedef std::vector<int> intVec;
typedef std::vector<std::string> strVec;
typedef std::vector<std::vector<int> > intVec2D;

strVec readFile() {
    strVec layerData;

    std::string data;
    std::fstream file("8-input", std::fstream::in);
    getline(file, data);
    file.close();

    for (int y = 0; y < data.length()/(25*6); y++) {
        layerData.push_back(data.substr(y*25*6, 25*6));
    }

    return layerData;
}

void writeFile(int a, intVec2D b) {
    std::fstream file("8-output", std::fstream::out);
    
    file << "Part 1: " << a << "\n";
    
    file << "Part 2:\n";
    for (int y = 0; y < b.size(); y++) {
        for (int x = 0; x < b[y].size(); x++)
            file << ((b[y][x] == 0)? " " : "#");
        if (y + 1 < b.size())
            file << "\n";
    }
}

int main() {
    strVec layerData = readFile();

    int solA = 0;
    int leastZeros = 100001;
    intVec2D image(6, intVec(25, 2));

    for (int i = 0; i < layerData.size(); i++) {
        intVec data(3,0);

        for (int y = 0; y < 6; y++) {
            for (int x = 0; x < 25; x++) {
                int color = std::stoi(layerData[i].substr(25*y+x, 1));
                if (image[y][x] == 2)
                    image[y][x] = color;
                data[color]++;
            }
        }

        if (data[0] < leastZeros) {
            solA = data[1] * data[2];
            leastZeros = data[0];
        }
    }

    writeFile(solA, image);

    return 0;
}