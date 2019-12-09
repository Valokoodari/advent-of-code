#include <vector>
#include <string>
#include <list>

typedef long long int ll;

class intCodeComputer {
    private:
        int PC;
        int relBase;

        std::vector<int> getModes(std::string ins);
        std::vector<ll> getParameters();

    public:
        std::vector<ll> code;
        std::list<ll> input;
        std::list<ll> output;

        intCodeComputer(std::vector<ll> startCode);
        
        int step();
        void addInput(ll number);
        ll getOutput();
};