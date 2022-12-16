input = { } -- input as comma-separated list

function fuel(mass)
    return math.floor(mass / 3) - 2
end

function smartFuel(mass)
    mass = fuel(mass)

    total = 0
    while mass > 0 do
        total = total + mass
        mass = fuel(mass)
    end

    return total
end

function main()
    solA,solB = 0,0

    for i = 1, #input do
        solA = solA + fuel(input[i])
        solB = solB + smartFuel(input[i])
    end

    print(solA, solB)
end

startTime = timer.getMilliSecCounter()
main()
endTime = timer.getMilliSecCounter()
print((endTime - startTime) / 1000, "s")