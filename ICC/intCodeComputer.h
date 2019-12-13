#include <vector>
#include <string>
#include <list>

#include <iostream>

typedef long long int ll;

class intCodeComputer {
    private:
        int programCounter;
        int relativeBase;

        std::vector<int> getModes(std::string ins);
        std::vector<ll> getParameters(int opCode);

    public:
        std::vector<ll> memory;
        std::list<ll> input;
        std::list<ll> output;

        intCodeComputer(std::vector<ll> startCode);
        
        int step();
        void addInput(ll number);
        ll getOutput();

        void setWord(int address, ll word);
};