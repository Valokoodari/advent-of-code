inputFile = "3-input"
outputFile = "3-output"

dir = {'L': [-1,0],'R': [1,0],'U': [0,1],'D': [0,-1]}

def readFile():
    file = open(inputFile, "r")

    A,B = file.readlines()
    A,B = [line.split(",") for line in [A,B]]

    file.close()
    return A,B

def writeFile(a, b):
    file = open(outputFile, "w+")
    file.write("Part 1: " + a + "\n")
    file.write("Part 2: " + b)
    file.close()

def mapCommands(A):
    cx, cy, step = 0, 0, 0
    mapped = [[0]*20000 for _ in range(20000)]
    for cmd in A:
        ax,ay = dir[cmd[0]][0],dir[cmd[0]][1]
        for _ in range(int(cmd[1:])):
            cx += ax
            cy += ay
            step += 1
            mapped[cx+10000][cy+10000] = step
    return mapped

def findIntersects(A, B):
    mapped = mapCommands(A);
    cx, cy, step = 0, 0, 0
    dist = 10000000
    steps = 10000000
    for cmd in B:
        for _ in range(int(cmd[1:])):
            cx += dir[cmd[0]][0]
            cy += dir[cmd[0]][1]
            step += 1
            aStep = mapped[cx+10000][cy+10000]
            aDist = abs(cx)+abs(cy)
            if aStep != 0:
                if (dist > aDist): dist = aDist
                if (steps > aStep + step): steps = aStep + step
    return dist, steps

def main():
    A,B = readFile()

    solA, solB = findIntersects(A, B)

    print(solA, solB)
    #writeFile(str(solA), str(solB))

if __name__ == '__main__': main()