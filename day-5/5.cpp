#include<iostream>
#include<vector>
#include<string>

std::vector<int> readFile() {
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

void writeFile(int a, int b) {
    std::cout << "Part 1: " << a << "\n";
    std::cout << "Part 2: " << b;
}

std::vector<int> getModes(std::string ins) {
    std::vector<int> modes;

    if (ins.size() >= 5) 
        modes.push_back(std::stoi(ins.substr(2,1)));
    if (ins.size() >= 4)
        modes.push_back(std::stoi(ins.substr(1,1)));
    if (ins.size() >= 3)
        modes.push_back(std::stoi(ins.substr(0,1)));
    while (modes.size() < 3)
        modes.push_back(0);

    return modes;
}

std::vector<int> getParameters(std::vector<int> code, int counter) {
    std::vector<int> parameters;
    std::vector<int> modes = getModes(std::to_string(code[counter]));

    parameters.push_back(code[((modes[0] == 0)? code[counter+1] : counter+1)]);
    parameters.push_back(code[((modes[1] == 0)? code[counter+2] : counter+2)]);
    parameters.push_back(code[counter+3]);

    return parameters;
}

std::vector<int> intCodeComputer(std::vector<int> code, int input) {
    std::vector<int> output;
    int counter = 0;
    while (code[counter] != 99) {
        std::string ins = std::to_string(code[counter]);
        std::vector<int> params = getParameters(code, counter);
        int opCode = std::stoi(((ins.size() > 1) ? ins.substr(ins.size() - 2, 2) : ins));

        if (opCode == 1) { // ADD
            code[params[2]] = params[0] + params[1];
            counter += 4;
        } else if (opCode == 2) { // MUL
            code[params[2]] = params[0] * params[1];
            counter += 4;
        } else if (opCode == 3) { // INPUT
            code[code[counter+1]] = input;
            counter += 2;
        } else if (opCode == 4) { // OUTPUT
            output.push_back(code[code[counter+1]]);
            counter += 2;
        } else if (opCode == 5) { // JUMP IF TRUE (NOT ZERO)
            counter = ((params[0] != 0)? params[1] : counter + 3);
        } else if (opCode == 6) { // JUMP IF FALSE (ZERO)
            counter = ((params[0] == 0)? params[1] : counter + 3);
        } else if (opCode == 7) { // IF LESS THAN
            code[params[2]] = (params[0] < params[1])? 1 : 0;
            counter += 4;
        } else if (opCode == 8) { // IF EQUAL TO
            code[params[2]] = (params[0] == params[1])? 1 : 0;
            counter += 4;
        } else { // ERROR
            break;
        }
    }

    return output;
} 

int main() {
    freopen("5-input", "r", stdin);
    freopen("5-output", "w", stdout);

    std::vector<int> code = readFile();

    std::vector<int> test1 = intCodeComputer(code, 1);
    std::vector<int> test5 = intCodeComputer(code, 5);

    int solA = test1.back();
    int solB = test5.back();

    writeFile(solA, solB);

    return 0;
}