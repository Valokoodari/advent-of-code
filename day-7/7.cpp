#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<thread>

typedef std::string string;

std::vector<int> readFile() {
    std::ifstream file("7-input");

    std::vector<int> code;
    std::string line;
    std::getline(file, line);
    file.close();

    while (line.length() > 0) {
        int c = line.find(",");
        if (c == -1) { // There is no comma at the end of the input
            code.push_back(std::stoi(line.substr(0, line.length())));
            break;
        }
        code.push_back(std::stoi(line.substr(0, c)));
        line.erase(0, c+1);
    }

    return code;
}

void writeFile(int a, int b) {
    std::ofstream file("7-output");
    file << "Part 1: " << a << "\n";
    file << "Part 2: " << b;
    file.close();
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

    parameters.push_back(code[(modes[0] == 0)? code[counter+1] : counter+1]);
    parameters.push_back(code[(modes[1] == 0)? code[counter+2] : counter+2]);
    parameters.push_back(code[counter+3]);

    return parameters;
}

std::vector<int> intCodeComputer(std::vector<int> code, std::vector<int> input) {
    std::vector<int> output;
    int inputCounter = 0;
    int counter = 0;
    while (code[counter] != 99) {
        std::string ins = std::to_string(code[counter]);
        std::vector<int> params = getParameters(code, counter);
        int opCode = std::stoi((ins.size() > 1) ? ins.substr(ins.size() - 2, 2) : ins);

        if (opCode == 1) { // ADD
            code[params[2]] = params[0] + params[1];
            counter += 4;
        } else if (opCode == 2) { // MUL
            code[params[2]] = params[0] * params[1];
            counter += 4;
        } else if (opCode == 3) { // INPUT
            code[code[counter+1]] = input[inputCounter];
            inputCounter++;
            counter += 2;
        } else if (opCode == 4) { // OUTPUT
            output.push_back(code[code[counter+1]]);
            counter += 2;
        } else if (opCode == 5) { // JUMP IF TRUE (NOT ZERO)
            counter = (params[0] != 0)? params[1] : counter+3;
        } else if (opCode == 6) { // JUMP IF FALSE (ZERO)
            counter = (params[0] == 0)? params[1] : counter+3;
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

int intCodeAmp(std::vector<int> code, string inputStr, string outputStr) {
    std::fstream file;
    const char* input = inputStr.c_str();
    const char* output = outputStr.c_str();
    int counter = 0;
    while (code[counter] != 99) {
        string ins = std::to_string(code[counter]);
        std::vector<int> params = getParameters(code, counter);
        int opCode = std::stoi((ins.size() > 1) ? ins.substr(ins.size() - 2, 2) : ins);

        if (opCode == 1) { // ADD
            code[params[2]] = params[0] + params[1];
            counter += 4;
        } else if (opCode == 2) { // MUL
            code[params[2]] = params[0] * params[1];
            counter += 4;
        } else if (opCode == 3) { // INPUT
            std::vector<string> lines;
            while(lines.size() < 1) {
                file.open(input, std::fstream::in);
                string line;
                while (std::getline(file, line)) {
                    lines.push_back(line);
                }
                file.close();
            }
            file.open(input, std::fstream::out);
            for (int i = 1; i < lines.size(); i++) {
                file << lines[i] << "\n";
            }
            file.close();
            code[code[counter+1]] = std::stoi(lines[0]);
            counter += 2;
        } else if (opCode == 4) { // OUTPUT
            file.open(output, std::fstream::out | std::fstream::app);
            file << code[code[counter+1]] << "\n";
            file.close();
            counter += 2;
        } else if (opCode == 5) { // JUMP IF TRUE (NOT ZERO)
            counter = (params[0] != 0)? params[1] : counter+3;
        } else if (opCode == 6) { // JUMP IF FALSE (ZERO)
            counter = (params[0] == 0)? params[1] : counter+3;
        } else if (opCode == 7) { // IF LESS THAN
            code[params[2]] = (params[0] < params[1])? 1 : 0;
            counter += 4;
        } else if (opCode == 8) { // IF EQUAL TO
            code[params[2]] = (params[0] == params[1])? 1 : 0;
            counter += 4;
        } else { // ERROR
            return 1;
        }
    }

    return 0;
} 

int main() {
    std::vector<int> ampCode = readFile();

    int settingsA[] = {0,1,2,3,4};
    int solA = 0;
    do {
        int amp1 = intCodeComputer(ampCode, std::vector<int>{settingsA[0], 0})[0];
        int amp2 = intCodeComputer(ampCode, std::vector<int>{settingsA[1], amp1})[0];
        int amp3 = intCodeComputer(ampCode, std::vector<int>{settingsA[2], amp2})[0];
        int amp4 = intCodeComputer(ampCode, std::vector<int>{settingsA[3], amp3})[0];
        int amp5 = intCodeComputer(ampCode, std::vector<int>{settingsA[4], amp4})[0];
        
        if (amp5 > solA) {
            solA = amp5;
        }
    } while (std::next_permutation(settingsA, settingsA + 5));

    string files[] = {"amp0","amp1","amp2","amp3","amp4"};
    int settingsB[] = {5,6,7,8,9};
    int solB = 0;
    do {
        std::fstream file;
        for (int i = 0; i < 5; i++) {
            const char* name = files[i].c_str();
            file.open(name, std::fstream::out);
            file << settingsB[i] << "\n";
            if (i == 0)
                file << 0 << "\n";
            file.close();
        }

        std::thread thread0(intCodeAmp, ampCode, "amp0", "amp1");
        std::thread thread1(intCodeAmp, ampCode, "amp1", "amp2");
        std::thread thread2(intCodeAmp, ampCode, "amp2", "amp3");
        std::thread thread3(intCodeAmp, ampCode, "amp3", "amp4");
        std::thread thread4(intCodeAmp, ampCode, "amp4", "amp0");

        thread0.join();
        thread1.join();
        thread2.join();
        thread3.join();
        thread4.join();

        file.open("amp0", std::fstream::in);
        string resultStr;
        std::getline(file, resultStr);
        int result = std::stoi(resultStr);
        if (result > solB)
            solB = result;
    } while (std::next_permutation(settingsB, settingsB + 5));

    writeFile(solA, solB);
}