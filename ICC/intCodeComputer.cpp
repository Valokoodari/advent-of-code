#include "intCodeComputer.h"

std::vector<int> intCodeComputer::getModes(std::string ins) {
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

std::vector<int> intCodeComputer::getParameters() {
    std::vector<int> parameters;
    std::vector<int> modes = getModes(std::to_string(code[PC]));

    parameters.push_back(code[(modes[0] == 0)? code[PC+1] : PC+1]);
    parameters.push_back(code[(modes[1] == 0)? code[PC+2] : PC+2]);
    parameters.push_back(code[PC+3]);

    return parameters;
}


intCodeComputer::intCodeComputer(std::vector<int> startCode) {
    code = startCode;
    PC = 0;
}

int intCodeComputer::step() {
    if (code[PC] == 99)
        return 99;

    std::string ins = std::to_string(code[PC]);
    std::vector<int> params = getParameters();
    int opCode = std::stoi((ins.size() > 1) ? ins.substr(ins.size() - 2, 2) : ins);

    if (opCode == 1) { // ADD
        code[params[2]] = params[0] + params[1];
        PC += 4;
    } else if (opCode == 2) { // MUL
        code[params[2]] = params[0] * params[1];
        PC += 4;
    } else if (opCode == 3) { // INPUT
        if (!input.empty()) {
            code[code[PC+1]] = input.front();
            input.pop_front();
            PC += 2;
        } else {
            return -3; // Error: input not found
        }
    } else if (opCode == 4) { // OUTPUT
        output.push_back(code[code[PC+1]]);
        PC += 2;
    } else if (opCode == 5) { // JUMP IF TRUE (NOT ZERO)
        PC = (params[0] != 0)? params[1] : PC+3;
    } else if (opCode == 6) { // JUMP IF FALSE (ZERO)
        PC = (params[0] == 0)? params[1] : PC+3;
    } else if (opCode == 7) { // IF LESS THAN
        code[params[2]] = (params[0] < params[1])? 1 : 0;
        PC += 4;
    } else if (opCode == 8) { // IF EQUAL TO
        code[params[2]] = (params[0] == params[1])? 1 : 0;
        PC += 4;
    } else {
        return -99; // Error: opCode not recognized
    }

    return opCode;
}

void intCodeComputer::addInput(int number) {
    input.push_back(number);
}

int intCodeComputer::getOutput() {
    int out = output.front();
    output.pop_front();
    return out;
}
