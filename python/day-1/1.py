inputFile = "1-input"
outputFile = "1-output"

def readFile():
    file = open(inputFile, "r")
    if (file.mode != 'r'): exit()
    lines = file.readlines()
    file.close()
    return lines

def writeFile(a, b):
    file = open(outputFile, "w+")
    file.write("Part 1: " + str(a) + "\n")
    file.write("Part 2: " + str(b))
    file.close()

def massToFuel(mass):
    return mass // 3 - 2

def smartMassToFuel(mass):
    fuel = 0
    add = massToFuel(mass)
    
    while (add > 0):
        fuel += add
        add = massToFuel(add)
    
    return fuel

def main():
    fuelA, fuelB = 0, 0

    lines = readFile()

    for line in lines:
        fuelA += massToFuel(int(line))
        fuelB += smartMassToFuel(int(line))

    writeFile(fuelA, fuelB)

if __name__ == '__main__': main()