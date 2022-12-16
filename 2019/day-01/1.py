inputFile = "../../inputs/2019/01.txt"

def readFile():
    file = open(inputFile, "r")
    if (file.mode != 'r'): exit()
    lines = file.readlines()
    file.close()
    return lines

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

    print("Part 1: " + str(fuelA))
    print("Part 2: " + str(fuelB))

if __name__ == '__main__': main()