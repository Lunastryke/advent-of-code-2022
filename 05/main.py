# Part 1
def part1():
    input = readInput(True)


# Part 2
def part2():
    input = readInput(True)


def readInput(isTest):
    filename = "test.txt" if isTest else "example.txt"
    inputFile = open(filename, "r")
    input = inputFile.readlines()
    return [i.strip() for i in input]


print("Part 1: ")
part1()
print("Part 2: ")
part2()
