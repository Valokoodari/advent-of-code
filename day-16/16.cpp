#include <numeric>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>

std::vector<int> readFile() {
    std::fstream file("16-input", std::fstream::in);
    std::string line;
    getline(file, line);

    std::vector<int> signal;
    for (int i = 0; i < line.size(); i++) {
        signal.push_back(std::stoi(line.substr(i, 1)));
    }

    return signal;
}

void writeFile(int a, int b) {
    std::fstream file("16-output", std::fstream::out);
    file << "Part 1: " << a << "\n";
    file << "Part 2: " << b;
    file.close();
}

std::vector<int> phaseA(std::vector<int> signal) {
    std::vector<int> phased;

    int base[] = {0,1,0,-1};

    for (int i = 0; i < signal.size(); i++) {
        int sum = 0;

        for (int j = 0; j < signal.size(); j++) {
            sum += signal[j] * base[(int)(std::ceil((j+2.0) / (i+1))-1)%4];
        }

        phased.push_back(abs(sum % 10));
    }

    return phased;
}

std::vector<int> phaseB(std::vector<int> signal, int offset) {
    int sum = std::accumulate(signal.begin()+offset, signal.end(), 0);

    for (int i = offset; i < signal.size(); i++) {
        sum -= signal[i];

        signal[i] = abs((sum + signal[i]) % 10);
    }

    return signal;
}

int main() {
    std::vector signal = readFile();

    std::vector<int> sigB;
    for (int i = 0; i < 10000; i++) {
        for (int j = 0; j < signal.size(); j++) {
            sigB.push_back(signal[j]);
        }
    }

    int offset = 0;
    for (int i = 0; i < 7; i++) {
        offset += std::pow(10,6-i) * signal[i];
    }

    for (int i = 0; i < 100; i++) {
        signal = phaseA(signal);
        sigB = phaseB(sigB, offset);
    }

    int solA = 0;
    int solB = 0;
    for (int i = 0; i < 8; i++) {
        solA += std::pow(10,7-i) * signal[i];
        solB += std::pow(10,7-i) * sigB[i+offset];
    }

    writeFile(solA, solB);

    return 0;
}