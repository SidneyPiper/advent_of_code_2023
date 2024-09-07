TEST_MODE = True
STAR = 2

if TEST_MODE:
    with open("test_input.txt") as f:
        lines = f.readlines()
else:
    with open("input.txt") as f:
        lines = f.readlines()


def starOne():
    pos = (-1, -1)

    for i, line in enumerate(lines):
        if line.find("S") != -1:
            pos = (i, line.find("S"))
            break

    for i in range(len(lines)):
        lines[i] = list(lines[i])

    # nach unten gehen von start, weil in test und normal
    pos = (pos[0] + 1, pos[1], "n")

    count = 1
    while True:
        old = (pos[0], pos[1])
        big_pipe = lines[pos[0]][pos[1]]
        
        if big_pipe == "S":
            break
        elif big_pipe == "|":
            if pos[2] == "n":
                pos = (pos[0] + 1, pos[1], "n")
            elif pos[2] == "s":
                pos = (pos[0] - 1, pos[1], "s")
        elif big_pipe == "-":
            if pos[2] == "e":
                pos = (pos[0], pos[1] - 1, "e")
            elif pos[2] == "w":
                pos = (pos[0], pos[1] + 1, "w")
        elif big_pipe == "L":
            if pos[2] == "n":
                pos = (pos[0], pos[1] + 1, "w")
            elif pos[2] == "e":
                pos = (pos[0] - 1, pos[1], "s")
        elif big_pipe == "J":
            if pos[2] == "n":
                pos = (pos[0], pos[1] - 1, "e")
            elif pos[2] == "w":
                pos = (pos[0] - 1, pos[1], "s")
        elif big_pipe == "7":
            if pos[2] == "s":
                pos = (pos[0], pos[1] - 1, "e")
            elif pos[2] == "w":
                pos = (pos[0] + 1, pos[1], "n")
        elif big_pipe == "F":
            if pos[2] == "s":
                pos = (pos[0], pos[1] + 1, "w")
            elif pos[2] == "e":
                pos = (pos[0] + 1, pos[1], "n")


        count += 1
    
    print(count / 2)
        


def starTwo():
    pos = (-1, -1)

    for i, line in enumerate(lines):
        if line.find("S") != -1:
            pos = (i, line.find("S"))
            break

    for i in range(len(lines)):
        lines[i] = list(lines[i])

    # nach unten gehen von start, weil in test und normal
    pos = (pos[0] + 1, pos[1], "n")

    while True:
        old = (pos[0], pos[1])
        big_pipe = lines[pos[0]][pos[1]]
        
        if big_pipe == "S":
            lines[old[0]][old[1]] = '┓'
            break
        elif big_pipe == "|":
            if pos[2] == "n":
                pos = (pos[0] + 1, pos[1], "n")
            elif pos[2] == "s":
                pos = (pos[0] - 1, pos[1], "s")
            lines[old[0]][old[1]] = "┃"
        elif big_pipe == "-":
            if pos[2] == "e":
                pos = (pos[0], pos[1] - 1, "e")
            elif pos[2] == "w":
                pos = (pos[0], pos[1] + 1, "w")
            lines[old[0]][old[1]] = "━"
        elif big_pipe == "L":
            if pos[2] == "n":
                pos = (pos[0], pos[1] + 1, "w")
            elif pos[2] == "e":
                pos = (pos[0] - 1, pos[1], "s")
            lines[old[0]][old[1]] = "┗"
        elif big_pipe == "J":
            if pos[2] == "n":
                pos = (pos[0], pos[1] - 1, "e")
            elif pos[2] == "w":
                pos = (pos[0] - 1, pos[1], "s")
            lines[old[0]][old[1]] = "┛"
        elif big_pipe == "7":
            if pos[2] == "s":
                pos = (pos[0], pos[1] - 1, "e")
            elif pos[2] == "w":
                pos = (pos[0] + 1, pos[1], "n")
            lines[old[0]][old[1]] = "┓"
        elif big_pipe == "F":
            if pos[2] == "s":
                pos = (pos[0], pos[1] + 1, "w")
            elif pos[2] == "e":
                pos = (pos[0] + 1, pos[1], "n")
            lines[old[0]][old[1]] = "┏"

    inside_counter = 0

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] not in {"┃", "━", "┗", "┛", "┓", "┏"}:
                lines[i][j] = "."

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            tmp_j = j
            if lines[i][j] == "┏":
                while tmp_j < len(lines[i]):
                    tmp_j += 1
                    if lines[i][tmp_j] == "━":
                        continue
                    elif lines[i][tmp_j] == "┛":
                        lines[i][tmp_j] = "#"
                        break
                    else:
                        break

            tmp_j = j
            if lines[i][j] == "┗":
                while tmp_j < len(lines[i]):
                    tmp_j += 1
                    if lines[i][tmp_j] == "━":
                        continue
                    elif lines[i][tmp_j] == "┓":
                        lines[i][tmp_j] = "#"
                        break
                    else:
                        break

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            tmp_j = j
            if lines[i][j] == ".":
                walls = 0
                while tmp_j < len(lines[i]):
                    cur = lines[i][tmp_j]
                    if cur == "┃" or cur == "┗" or cur == "┛" or cur == "┓" or cur == "┏":
                        walls += 1
                    tmp_j += 1
                
                if walls % 2 == 1:
                    inside_counter += 1
                    lines[i][j] = "1"
            
    for line in lines:
        print("".join(line))

    print(inside_counter)

        


if STAR == 1:
    starOne()
elif STAR == 2:
    starTwo()
