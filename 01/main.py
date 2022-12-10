# Part 1
def part1():
    input = readInput(True)
    currMax = 0
    curr = 0
    for line in input:
        if line == "":
            if curr > currMax:
                currMax = curr
            curr = 0
            continue
        curr += int(line)
    print(curr if curr > currMax else currMax)


# Part 2
def part2():
    input = readInput(True)
    currMax = [0 for i in range(3)]
    curr = 0
    for line in input:
        if line == "":
            if curr > currMax[0]:
                currMax[0] = curr
            currMax.sort()
            curr = 0
            continue
        curr += int(line)
    if curr > currMax[0]:
        currMax[0] = curr
    print(sum(currMax))


def readInput(isTest):
    filename = "test.txt" if isTest else "example.txt"
    inputFile = open(filename, "r")
    input = inputFile.readlines()
    return [i.strip() for i in input]


print("Part 1: ")
part1()
print("Part 2: ")
part2()
