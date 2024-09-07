with open('input.txt') as f:
    lines = f.readlines()


def checkForSymbol(y, x1, x2):
    if x1 - 1 > 0:
        if not lines[y][x1 - 1].isdigit() and lines[y][x1 - 1] != ".":
            return True

    if x2 + 1 < len(lines[0]) - 1:
        if not lines[y][x2].isdigit() and lines[y][x2] != ".":
            return True

    for i in range(x1 - 1, x2 + 1, 1):
        if 0 < i < len(lines[0]) - 1:
            if y - 1 >= 0:
                if not lines[y - 1][i].isdigit() and lines[y - 1][i] != ".":
                    return True
            if y + 1 < len(lines):
                if not lines[y + 1][i].isdigit() and lines[y + 1][i] != ".":
                    return True


def checkForGear(y, x1, x2):
    if x1 - 1 > 0:
        if not lines[y][x1 - 1].isdigit() and lines[y][x1 - 1] == "*":
            return y, x1 - 1

    if x2 + 1 < len(lines[0]) - 1:
        if not lines[y][x2].isdigit() and lines[y][x2] == "*":
            return y, x2

    for i in range(x1 - 1, x2 + 1, 1):
        if 0 < i < len(lines[0]) - 1:
            if y - 1 >= 0:
                if not lines[y - 1][i].isdigit() and lines[y - 1][i] == "*":
                    return y - 1, i
            if y + 1 < len(lines):
                if not lines[y + 1][i].isdigit() and lines[y + 1][i] == "*":
                    return y + 1, i

    return -1, -1


def starOne():
    i = j = 0
    result = []

    while i < len(lines):
        while j < len(lines[0]) - 1:
            if lines[i][j].isdigit():
                start = j
                while lines[i][j].isdigit():
                    j += 1
                end = j

                if checkForSymbol(i, start, end):
                    result.append(int(lines[i][start:end]))

            j += 1

        j = 0
        i += 1

    print(sum(result))


def starTwo():
    i = j = 0
    result = [[[1, 0] for x in range(len(lines[0]) - 1)] for y in range(len(lines))]

    while i < len(lines):
        while j < len(lines[0]) - 1:
            if lines[i][j].isdigit():
                start = j
                while lines[i][j].isdigit():
                    j += 1
                end = j

                y, x = checkForGear(i, start, end)

                if y != -1 and x != -1:
                    result[y][x][0] *= int(lines[i][start:end])
                    result[y][x][1] += 1

            j += 1

        j = 0
        i += 1

    summe = 0
    for y in result:
        print(y)
        for x in y:
            if x[1] == 2:
                summe += x[0]

    print(summe)


starTwo()