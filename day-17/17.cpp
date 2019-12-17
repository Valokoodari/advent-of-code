#include "../ICC/intCodeComputer.h"
#include <fstream>
#include <string>
#include <vector>
#include <map>

typedef long long int ll;
typedef std::vector<long long int> intCode;

intCode readFile() {
    std::fstream file("17-input", std::fstream::in);
    std::string line;
    std::getline(file, line);
    file.close();

    intCode code;
    while (line.length() > 0) {
        int c = line.find(",");
        if (c == -1) { // There is no comma at the end of the input
            code.push_back(std::stoll(line.substr(0, line.length())));
            break;
        }
        code.push_back(std::stoll(line.substr(0, c)));
        line.erase(0, c+1);
    }

    return code;
}

void writeFile(int a, int b) {
    std::fstream file("15-output", std::fstream::out);
    file << "Part 1: " << a << "\n";
    file << "Part 2: " << b;
    file.close();
}

int main() {
    intCode code = readFile();
    intCodeComputer pc(code);
    pc.setWord(0,2);

    int solA = 0;
    int solB = 0;

    std::string output = "";
    std::string input = "A,C,A,B,A,B,C,B,B,C\nL,4,L,4,L,10,R,4\nR,4,L,10,R,10\nR,4,L,4,L,4,R,8,R,10\nn\n";
    for (int i = 0; i < input.size(); i++) {
        pc.addInput((int)input[i]);
        std::cout << (int)input[i] << "\n";
    }

    int asd = 0;

    int prevOp = 0;
    while (prevOp != 99) {
        prevOp = pc.step();

        if (prevOp == 4) {
            asd = pc.getOutput();
            if (asd < 200)
                output += (char)asd;
            std::cout << output << "\n";
        }
    }

    std::cout << asd << "\n";
    
    std::cout << solA << " " << solB;

    return 0;
}