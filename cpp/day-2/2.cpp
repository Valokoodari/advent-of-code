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

int func(std::vector<int> code, int noun, int verb) {
    code[1] = noun;
    code[2] = verb;

    for (int i = 0; i < code.size(); i+=4) {
        if (code[i] == 1) {
            code[code[i+3]] = code[code[i+1]] + code[code[i+2]];
        } else if (code[i] == 2) {
            code[code[i+3]] = code[code[i+1]] * code[code[i+2]];
        } else {
            break;
        }
    }

    return code[0];
} 

int main() {
    freopen("2-input", "r", stdin);
    freopen("2-output", "w", stdout);

    int result = 19690720;
    std::vector<int> code = readInput();

    std::cout << "Part 1: " << func(code, 12, 2) << "\n";

    for (int noun = 0; noun < 100; noun++) {
        int verb = result - func(code, noun, 0);
        if (verb >= 0 && verb < 100) {
            std::cout << "Part 2: " << 100 * noun + verb;
            break;
        } 
    }
}