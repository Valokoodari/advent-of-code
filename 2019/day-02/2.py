inputFile = "../../inputs/2019/02.txt"

def readFile():
    file = open(inputFile, "r")
    code = list(map(int, file.readline().split(",")))
    file.close
    return code

def func(code, noun, verb):
    code[1] = noun
    code[2] = verb

    for i in range(0, len(code), 4):
        if (code[i] == 1):
            code[code[i+3]] = code[code[i+1]] + code[code[i+2]]
        elif (code[i] == 2):
            code[code[i+3]] = code[code[i+1]] * code[code[i+2]]
        else:
            break
    
    return code[0]

def main():
    result = 19690720
    intCode = readFile()
    
    solA = func(intCode[:], 12, 2)

    solB = 0
    for i in range(0, 100, 1):
        verb = result - func(intCode[:], i, 0)
        if (0 < verb < 100):
            solB = 100 * i + verb
            break

    print("Part 1: " + str(solA))
    print("Part 2: " + str(solB))

if __name__ == '__main__': main()