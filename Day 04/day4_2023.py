with open('input.txt') as f:
    lines = f.readlines()


def starOne():
    result = 0
    for line in lines:
        line = line.split(":")[1:]
        line = line[0].replace("\n", "").split("|")

        winner = line[0].split(" ")
        numbers = line[1].split(" ")

        winner = set(winner)
        numbers = set(numbers)

        if "" in winner:
            winner.remove("")
        if "" in numbers:
            numbers.remove("")

        union = winner & numbers

        if len(union) > 0:
            result += 2 ** (len(union) - 1)

    print(result)


def starTwo():
    copies = [1] * len(lines)

    for i, line in enumerate(lines):
        line = line.split(":")[1:]
        line = line[0].replace("\n", "").split("|")

        winner = line[0].split(" ")
        numbers = line[1].split(" ")

        winner = set(winner)
        numbers = set(numbers)

        if "" in winner:
            winner.remove("")
        if "" in numbers:
            numbers.remove("")

        union = winner & numbers

        if len(union) > 0:
            for j in range(len(union)):
                copies[i + j + 1] += 1 * copies[i]


    print(sum(copies))


starTwo()