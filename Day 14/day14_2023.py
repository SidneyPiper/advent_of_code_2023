TEST_MODE = False
STAR = 2

if TEST_MODE:
    with open("test_input.txt") as f:
        lines = f.readlines()
else:
    with open("input.txt") as f:
        lines = f.readlines()


def starOne():
    board = list(map(lambda x: list(x.strip()), lines))

    for r in range(len(board)):
        for c in range(len(board[r])):
            cur = board[r][c]
            if cur == "O":
                nxt = r

                while nxt - 1 >= 0 and board[nxt - 1][c] == ".":
                    nxt -= 1

                tmp = board[nxt][c]
                board[nxt][c] = cur
                board[r][c] = tmp

    result = 0

    for i, row in enumerate(reversed(board)):
        result += (i + 1) * "".join(row).count("O")

    print(result)


def spin_cycle(board):
    for r in range(len(board)):
        for c in range(len(board[r])):
            cur = board[r][c]
            if cur == "O":
                nxt = r

                while nxt - 1 >= 0 and board[nxt - 1][c] == ".":
                    nxt -= 1

                tmp = board[nxt][c]
                board[nxt][c] = cur
                board[r][c] = tmp

    for c in range(len(board)):
        for r in range(len(board[r])):
            cur = board[r][c]
            if cur == "O":
                nxt = c

                while nxt - 1 >= 0 and board[r][nxt - 1] == ".":
                    nxt -= 1

                tmp = board[r][nxt]
                board[r][nxt] = cur
                board[r][c] = tmp

    for r in reversed(range(len(board))):
        for c in range(len(board[r])):
            cur = board[r][c]
            if cur == "O":
                nxt = r

                while nxt + 1 < len(board) and board[nxt + 1][c] == ".":
                    nxt += 1

                tmp = board[nxt][c]
                board[nxt][c] = cur
                board[r][c] = tmp

    for c in reversed(range(len(board))):
        for r in range(len(board[r])):
            cur = board[r][c]
            if cur == "O":
                nxt = c

                while nxt + 1 < len(board) and board[r][nxt + 1] == ".":
                    nxt += 1

                tmp = board[r][nxt]
                board[r][nxt] = cur
                board[r][c] = tmp

    return board


def starTwo():
    board = list(map(lambda x: list(x.strip()), lines))

    weights = []

    for j in range(10000):
        old = []
        for row in board:
            old.append(row.copy())

        board = spin_cycle(board)

        result = 0
        for i, row in enumerate(reversed(board)):
            result += (i + 1) * "".join(row).count("O")

        print(result)
        weights.append(result)

        if j > 144:
            first = weights[j - 2 * 72 : j - 72]
            second = weights[j - 72 : j]

            if first == second:
                print(first, len(first))
                print(first[(1000000000 - (j + 1)) % 72])
                break


if STAR == 1:
    starOne()
elif STAR == 2:
    starTwo()
