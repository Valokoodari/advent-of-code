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

std::vector<ll> intCodeComputer::getParameters() {
    std::vector<ll> parameters;
    std::vector<int> modes = getModes(std::to_string(code[PC]));

    parameters.push_back(code[(modes[0] == 0)? code[PC+1] : (modes[0] == 1)? PC+1 : relBase + code[PC+1]]);
    parameters.push_back(code[(modes[1] == 0)? code[PC+2] : (modes[1] == 1)? PC+2 : relBase + code[PC+2]]);
    parameters.push_back((modes[2] == 0)? code[PC+3] : code[PC+3]+relBase);

    return parameters;
}


intCodeComputer::intCodeComputer(std::vector<ll> startCode) {
    code = startCode;
    relBase = 0;
    PC = 0;

    for (int i = 0; i < 1000; i++) {
        code.push_back(0);
    }
}

int intCodeComputer::step() {
    if (code[PC] == 99)
        return 99;

    std::string ins = std::to_string(code[PC]);
    std::vector<int> modes = getModes(ins);
    std::vector<ll> params = getParameters();
    int opCode = std::stoi((ins.size() > 1) ? ins.substr(ins.size() - 2, 2) : ins);

    if (opCode == 1) { // ADD
        code[params[2]] = params[0] + params[1];
        PC += 4;
    } else if (opCode == 2) { // MUL
        code[params[2]] = params[0] * params[1];
        PC += 4;
    } else if (opCode == 3) { // INPUT
        if (!input.empty()) {
            if (modes[0] == 2) {
                code[relBase + code[PC+1]] = input.front();
            } else {
                code[code[PC+1]] = input.front();
            }
            input.pop_front();
            PC += 2;
        } else {
            return -3; // Error: input not found
        }
    } else if (opCode == 4) { // OUTPUT
        output.push_back(params[0]);
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
    } else if (opCode == 9) { // Change Relative Base
        relBase += params[0];
        PC += 2;
    } else {
        return -99; // Error: opCode not recognized
    }

    return opCode;
}

void intCodeComputer::addInput(ll number) {
    input.push_back(number);
}

ll intCodeComputer::getOutput() {
    ll out = output.front();
    output.pop_front();
    return out;
}
