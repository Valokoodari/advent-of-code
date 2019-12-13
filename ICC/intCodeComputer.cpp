#include "intCodeComputer.h"

intCodeComputer::intCodeComputer(std::vector<ll> initialMemory) {
    programCounter = 0;                 // Initialize program counter as 0
    relativeBase = 0;                   // Initialize relative base as 0

    memory = initialMemory;             // Initialize memory
    for (int i = 0; i < 20000; i++) {   // Expand memory by 20000 words.
        memory.push_back(0);
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

std::vector<ll> intCodeComputer::getParameters(int opCode) {
    std::vector<ll> parameters;
    std::vector<int> modes = getModes(std::to_string(memory[programCounter]));

    if (opCode == 3) {
        parameters.push_back(memory[programCounter+1] + ((modes[0] == 2)? relativeBase : 0));
    } else {
        parameters.push_back(memory[(modes[0] == 0)? memory[programCounter+1] : (modes[0] == 1)? programCounter+1 : relativeBase + memory[programCounter+1]]);
    }
    parameters.push_back(memory[(modes[1] == 0)? memory[programCounter+2] : (modes[1] == 1)? programCounter+2 : relativeBase + memory[programCounter+2]]);
    parameters.push_back((modes[2] == 0)? memory[programCounter+3] : memory[programCounter+3]+relativeBase);

    return parameters;
}

int intCodeComputer::step() {
    if (memory[programCounter] == 99) return 99;

    std::string ins = std::to_string(memory[programCounter]);
    int opCode = std::stoi((ins.size() > 1) ? ins.substr(ins.size() - 2, 2) : ins);

    std::vector<int> modes = getModes(ins);
    std::vector<ll> params = getParameters(opCode);

    switch(opCode) {
        case 1:                         // Addition
            memory[params[2]] = params[0] + params[1];
            programCounter += 4;
            break;
        case 2:                         // Multiplication
            memory[params[2]] = params[0] * params[1];
            programCounter += 4;
            break;
        case 3:                         // Read input
            if (input.size() > 0) {
                memory[params[0]] = input.front();
                input.pop_front();
            } else {
                return -3;
            }
            programCounter += 2;
            break;
        case 4:                         // Write output
            output.push_back(params[0]);
            programCounter += 2;
            break;
        case 5:                         // Jump if true (not zero)
            programCounter = (params[0] != 0)? params[1] : programCounter+3;
            break;
        case 6:                         // Jump if false (zero)
            programCounter = (params[0] == 0)? params[1] : programCounter+3;
            break;
        case 7:                         // If less than 
            memory[params[2]] = (params[0] < params[1])? 1 : 0;
            programCounter += 4;
            break;
        case 8:                         // If equal to
            memory[params[2]] = (params[0] == params[1])? 1 : 0;
            programCounter += 4;
            break;
        case 9:                         // Increase relative base
            relativeBase += params[0];
            programCounter += 2;
            break;
        default:
            return -99;                 // Error: unrecognized operation code
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

void intCodeComputer::setWord(int address, ll word) {
    memory[address] = word;
}