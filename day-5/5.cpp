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

std::vector<int> intCodeComputer(std::vector<int> code, int input) {
    std::vector<int> output;
    int counter = 0;
    while (code[counter] != 99) {
        int A = 0;
        int B = 0;
        int C = 0;
        int opCode = 0;
        std::string ins = std::to_string(code[counter]);

        if (ins.size() > 1) {
            opCode = std::stoi(ins.substr(ins.size() - 2, 2));
        } else {
            opCode = std::stoi(ins);
        }
        
        if (ins.length() == 3) {
            C = std::stoi(ins.substr(0,1));
        } else if (ins.length() == 4) {
            B = std::stoi(ins.substr(0,1));
            C = std::stoi(ins.substr(1,1));
        } else if (ins.length() == 5) {
            A = std::stoi(ins.substr(0,1));
            B = std::stoi(ins.substr(1,1));
            C = std::stoi(ins.substr(2,1));
        }

        if (opCode == 1) { // ADD
            int c, b;
            if (C == 0) {
                c = code[code[counter+1]];
            } else {
                c = code[counter+1];
            }
            if (B == 0) {
                b = code[code[counter+2]];
            } else {
                b = code[counter+2];
            }
            code[code[counter+3]] = c + b;
            counter += 4;
        } else if (opCode == 2) { // MUL
            int c, b;
            if (C == 0) {
                c = code[code[counter+1]];
            } else {
                c = code[counter+1];
            }
            if (B == 0) {
                b = code[code[counter+2]];
            } else {
                b = code[counter+2];
            }
            code[code[counter+3]] = c * b;
            counter += 4;
        } else if (opCode == 3) { // INPUT
            code[code[counter+1]] = input;
            counter += 2;
        } else if (opCode == 4) { // OUTPUT
            output.push_back(code[code[counter+1]]);
            counter += 2;
        } else if (opCode == 5) { // JUMP IF TRUE (NOT ZERO)
            int c = code[counter+1];
            int b = code[counter+2];
            if (C == 0)
                c = code[c];
            if (B == 0)
                b = code[b];
            if (c != 0)
                counter = b;
            else
                counter += 3;
        } else if (opCode == 6) { // JUMP IF FALSE (ZERO)
            int c = code[counter+1];
            int b = code[counter+2];
            if (C == 0)
                c = code[c];
            if (B == 0)
                b = code[b];
            if (c == 0)
                counter = b;
            else
                counter += 3;
        } else if (opCode == 7) { // IF LESS THAN
            int c = code[counter+1];
            int b = code[counter+2];
            int a = code[counter+3];
            if (C == 0) {
                c = code[c];
            }
            if (B == 0) {
                b = code[b];
            }
            code[a] = (c < b)? 1 : 0;
            counter += 4;
        } else if (opCode == 8) { // IF EQUAL TO
            int c = code[counter+1];
            int b = code[counter+2];
            int a = code[counter+3];
            if (C == 0) {
                c = code[c];
            }
            if (B == 0) {
                b = code[b];
            }
            code[a] = (c == b)? 1 : 0;
            counter += 4;
        } else {
            std::cout << "Error\n";
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
}