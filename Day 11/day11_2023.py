TEST_MODE = False
STAR = 2

if TEST_MODE:
    with open("test_input.txt") as f:
        lines = f.readlines()
else:
    with open("input.txt") as f:
        lines = f.readlines()


def starOne():
    empty_rows = []
    empty_cols = []

    image = list(map(lambda x: list(x.strip()), lines))

    for i, row in enumerate(image):
        if "".join(row).replace(".", "") == "":
            empty_rows.append(i)

    for i, col in enumerate(zip(*image)):
        if "".join(col).replace(".", "") == "":
            empty_cols.append(i)

    galaxies = [[r, c] for r in range(len(lines)) for c in range(len(lines[r]))
                    if lines[r][c] == "#"]
    
    for i, galaxy in enumerate(galaxies):
        rc = 0
        for x in empty_rows:
            if galaxy[0] > x:
                rc += 1

        cc = 0
        for x in empty_cols:
            if galaxy[1] > x:
                cc += 1

        galaxies[i] = [galaxy[0] + rc , galaxy[1] + cc]

    distances = []

    for i, first_galaxy in enumerate(galaxies):
        for second_galaxy in galaxies[i:]:
            distances.append(abs(first_galaxy[0] - second_galaxy[0]) + abs(first_galaxy[1] - second_galaxy[1]))

    print(sum(distances))


def starTwo():
    empty_rows = []
    empty_cols = []

    image = list(map(lambda x: list(x.strip()), lines))

    for i, row in enumerate(image):
        if "".join(row).replace(".", "") == "":
            empty_rows.append(i)

    for i, col in enumerate(zip(*image)):
        if "".join(col).replace(".", "") == "":
            empty_cols.append(i)

    galaxies = [[r, c] for r in range(len(lines)) for c in range(len(lines[r]))
                    if lines[r][c] == "#"]
    
    for i, galaxy in enumerate(galaxies):
        rc = 0
        for x in empty_rows:
            if galaxy[0] > x:
                rc += 1

        cc = 0
        for x in empty_cols:
            if galaxy[1] > x:
                cc += 1

        galaxies[i] = [galaxy[0] + rc * (1000000 - 1), galaxy[1] + cc * (1000000 - 1)]

    distances = []

    for i, first_galaxy in enumerate(galaxies):
        for second_galaxy in galaxies[i:]:
            distances.append(abs(first_galaxy[0] - second_galaxy[0]) + abs(first_galaxy[1] - second_galaxy[1]))

    print(sum(distances))


if STAR == 1:
    starOne()
elif STAR == 2:
    starTwo()
