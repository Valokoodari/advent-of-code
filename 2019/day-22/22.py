inputFile = "../../inputs/2019/22.txt"

def readFile():
    file = open(inputFile, "r")
    if (file.mode != 'r'): exit()
    lines = file.readlines()
    file.close()
    return lines

def getDeck(lines, cards, times = 0):
    offset, increment = 0, 1
    for line in lines:
        if line.startswith("deal into new stack"):
            increment = (-1*increment) % cards
            offset = (offset + increment) % cards
        elif line.startswith("cut "):
            _, cutPos = line.split(" ")
            offset = (offset + int(cutPos) * increment) % cards
        elif line.startswith("deal with increment "):
            *_, inc = line.split(" ")
            increment = (increment * pow(int(inc), cards-2, cards)) % cards

    if times > 0:
        oldIncrement = increment
        increment = pow(increment, times, cards)
        offset = (offset * (1 - increment) * pow((1-oldIncrement) % cards, cards-2, cards)) % cards

    return offset, increment

def main():
    lines = readFile()

    cards = 119315717514047
    times = 101741582076661

    offsetA, incrementA = getDeck(lines, 10007)
    offsetB, incrementB = getDeck(lines, cards, times)

    for i in range(0, 10007):
        if (offsetA + i * incrementA) % 10007 == 2019:
            solA = i
            break

    solB = (offsetB + 2020 * incrementB) % cards

    print("Part 1: " + str(solA))
    print("Part 2: " + str(solB))

if __name__ == '__main__': main()