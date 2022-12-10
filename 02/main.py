# Part 1
def part1():
    input = readInput(True)
    patternScore = {"X": 1, "Y": 2, "Z": 3}
    score = 0
    for round in input:
        opp, you = round.split(" ")
        score += patternScore[you]
        # Draw
        if ord(you) - ord("X") == ord(opp) - ord("A"):
            score += 3
        # Win
        if (
            (you == "X" and opp == "C")
            or (you == "Y" and opp == "A")
            or (you == "Z" and opp == "B")
        ):
            score += 6
    print(score)


# Part 2
def part2():
    input = readInput(True)
    resultScore = {"X": 0, "Y": 3, "Z": 6}
    patternScore = {"A": 1, "B": 2, "C": 3}
    losePattern = {"A": "C", "B": "A", "C": "B"}
    winPattern = {"A": "B", "B": "C", "C": "A"}
    score = 0
    for round in input:
        opp, you = round.split(" ")
        score += resultScore[you]
        # Draw
        if you == "Y":
            score += patternScore[opp]
        # Lose
        if you == "X":
            score += patternScore[losePattern[opp]]
        # Win
        if you == "Z":
            score += patternScore[winPattern[opp]]
    print(score)


def readInput(isTest):
    filename = "test.txt" if isTest else "example.txt"
    inputFile = open(filename, "r")
    input = inputFile.readlines()
    return [i.strip() for i in input]


print("Part 1: ")
part1()
print("Part 2: ")
part2()
