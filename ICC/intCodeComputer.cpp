#include "intCodeComputer.h"

intCodeComputer::intCodeComputer(std::vector<ll> startCode) {
    PC = 0;                             // Initialize program counter as 0
    RB = 0;                             // Initialize relative base as 0

    MEM = startCode;                    // Initialize memory as program code
    for (int i = 0; i < 1000; i++) {    // Expand memory by 1000 words.
        MEM.push_back(0);
    }
}

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
    std::vector<int> modes = getModes(std::to_string(MEM[PC]));

    parameters.push_back(MEM[(modes[0] == 0)? MEM[PC+1] : (modes[0] == 1)? PC+1 : RB + MEM[PC+1]]);
    parameters.push_back(MEM[(modes[1] == 0)? MEM[PC+2] : (modes[1] == 1)? PC+2 : RB + MEM[PC+2]]);
    parameters.push_back((modes[2] == 0)? MEM[PC+3] : MEM[PC+3]+RB);

    return parameters;
}

int intCodeComputer::step() {
    if (MEM[PC] == 99)
        return 99;

    std::string ins = std::to_string(MEM[PC]);
    std::vector<int> modes = getModes(ins);
    std::vector<ll> params = getParameters();
    int opCode = std::stoi((ins.size() > 1) ? ins.substr(ins.size() - 2, 2) : ins);

    if (opCode == 1) { // ADD
        MEM[params[2]] = params[0] + params[1];
        PC += 4;
    } else if (opCode == 2) { // MUL
        MEM[params[2]] = params[0] * params[1];
        PC += 4;
    } else if (opCode == 3) { // INPUT
        if (!input.empty()) {
            if (modes[0] == 2) {
                MEM[RB + MEM[PC+1]] = input.front();
            } else {
                MEM[MEM[PC+1]] = input.front();
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
        MEM[params[2]] = (params[0] < params[1])? 1 : 0;
        PC += 4;
    } else if (opCode == 8) { // IF EQUAL TO
        MEM[params[2]] = (params[0] == params[1])? 1 : 0;
        PC += 4;
    } else if (opCode == 9) { // Change Relative Base
        RB += params[0];
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