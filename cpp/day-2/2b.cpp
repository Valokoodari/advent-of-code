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
    freopen("2b-output", "w", stdout);

    int result = 19690720;
    std::vector<int> code = readInput();

    for (int noun = 0; noun < 100; noun++) {
        std::vector<int> intCode = code;

        intCode[1] = noun;
        intCode[2] = 1;

        for (int i = 0; i < intCode.size(); i+=4) {
            if (intCode[i] == 1) {
                intCode[intCode[i+3]] = intCode[intCode[i+1]] + intCode[intCode[i+2]];
            } else if (intCode[i] == 2) {
                intCode[intCode[i+3]] = intCode[intCode[i+1]] * intCode[intCode[i+2]];
            } else {
                break;
            }
        }

        int verb = result - intCode[0];
        if (verb >= 0 && verb < 100) {
            std::cout << 100*noun + verb + 1;
            break;
        } 
    }
}