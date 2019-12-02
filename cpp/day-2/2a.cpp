#include<iostream>
#include<vector>
#include<string>

std::vector<int> readInput() {
    std::vector<int> code;
    std::string input;
    std::cin >> input;

    while (input.length() > 0) {
        int c = input.find(",");
        if (c == -1) { // There is no comma at the end of the input
            code.push_back(std::stoi(input.substr(0, input.length())));
            break;
        }
        code.push_back(std::stoi(input.substr(0, c)));
        input.erase(0, c+1);
    }

    return code;
}

int main() {
    freopen("2-input", "r", stdin);
    freopen("2a-output", "w", stdout);

    std::vector<int> intCode = readInput();

    intCode[1] = 12;
    intCode[2] = 2;

    for (int i = 0; i < intCode.size(); i+=4) {
        if (intCode[i] == 1) {
            intCode[intCode[i+3]] = intCode[intCode[i+1]] + intCode[intCode[i+2]];
        } else if (intCode[i] == 2) {
            intCode[intCode[i+3]] = intCode[intCode[i+1]] * intCode[intCode[i+2]];
        } else {
            break;
        }
    }

    std::cout << intCode[0];
}