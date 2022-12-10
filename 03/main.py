# Part 1
def part1():
    input = readInput(True)
    priority = 0
    for backpack in input:
        item = getCommonItem(list(backpack))
        if item is None:
            continue
        if item.islower():
            priority += ord(item) - ord("a") + 1
        else:
            priority += ord(item) - ord("A") + 27
    print(priority)


# Part 2
def part2():
    input = readInput(True)
    priority = 0
    for groupNum in range(0, len(input), 3):
        itemSet = (
            set(input[groupNum])
            .intersection(set(input[groupNum + 1]))
            .intersection(set(input[groupNum + 2]))
        )
        item = itemSet.pop()
        if item is None:
            continue
        if item.islower():
            priority += ord(item) - ord("a") + 1
        else:
            priority += ord(item) - ord("A") + 27
    print(priority)


def getCommonItem(itemList):
    itemSet = set()
    for i in itemList[0 : len(itemList) // 2]:
        itemSet.add(i)
    for i in itemList[len(itemList) // 2 : :]:
        if i in itemSet:
            return i
    return


def readInput(isTest):
    filename = "test.txt" if isTest else "example.txt"
    inputFile = open(filename, "r")
    input = inputFile.readlines()
    return [i.strip() for i in input]


print("Part 1: ")
part1()
print("Part 2: ")
part2()
