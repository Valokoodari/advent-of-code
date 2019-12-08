#include <vector>
#include <string>
#include <list>

class intCodeComputer {
    private:
        int PC;

        std::vector<int> getModes(std::string ins);
        std::vector<int> getParameters();

    public:
        std::vector<int> code;
        std::list<int> input;
        std::list<int> output;

        intCodeComputer(std::vector<int> startCode);
        
        int step();
        void addInput(int number);
        int getOutput();
};