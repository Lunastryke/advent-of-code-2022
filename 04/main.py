# Part 1
def part1():
    input = readInput(True)
    count = 0
    for pair in input:
        alf, elf = pair.split(",")
        alfLeft, alfRight = [int(i) for i in alf.split("-")]
        elfLeft, elfRight = [int(i) for i in elf.split("-")]
        # elf range contains alf range OR alf range contains elf range
        if (elfRight >= alfRight and elfLeft <= alfLeft) or (
            alfRight >= elfRight and alfLeft <= elfLeft
        ):
            count += 1
    print(count)


# Part 2
def part2():
    input = readInput(True)
    count = 0
    for pair in input:
        alf, elf = pair.split(",")
        alfLeft, alfRight = [int(i) for i in alf.split("-")]
        elfLeft, elfRight = [int(i) for i in elf.split("-")]
        if (alfRight < elfLeft) or (alfLeft > elfRight):
            continue
        count += 1
    print(count)


def readInput(isTest):
    filename = "test.txt" if isTest else "example.txt"
    inputFile = open(filename, "r")
    input = inputFile.readlines()
    return [i.strip() for i in input]


print("Part 1: ")
part1()
print("Part 2: ")
part2()
