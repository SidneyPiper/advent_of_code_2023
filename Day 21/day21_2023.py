import matplotlib.pyplot as plt

TEST_MODE = False
STAR = 2

if TEST_MODE:
    with open("test_input.txt") as f:
        lines = f.readlines()
else:
    with open("input.txt") as f:
        lines = f.readlines()


def showGarden(garden):
    for r in garden:
        print("".join(r))


def step_old(garden, rocks):
    positions = {
        (r, c)
        for c in range(len(lines))
        for r in range(len(lines))
        if garden[r][c] in "SO"
    }

    edges = set()
    for r, c in positions:
        garden[r][c] = "."
        edges |= set(
            filter(
                lambda p: 0 <= p[0] < len(garden) and 0 <= p[1] < len(garden),
                {(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)},
            )
        )

    new_positions = edges - rocks

    for r, c in new_positions:
        garden[r][c] = "O"

    return len(new_positions)


def simulate_step(positions, rocks, length):
    new_positions = set()
    for r, c in positions:
        new_positions |= set(
            filter(
                lambda p: (p[0] % length, p[1] % length) not in rocks,
                {(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)},
            )
        )

    return new_positions


def starOne():
    garden = list(map(lambda l: list(l.strip()), lines))

    rocks = {
        (r, c)
        for c in range(len(lines))
        for r in range(len(lines))
        if lines[r][c] == "#"
    }

    for i in range(64):
        result = step_old(garden, rocks)

    print(result)


def starTwo():
    garden = [[0 for c in range(len(lines))] for r in range(len(lines))]

    rocks = [
        (r, c)
        for c in range(len(lines))
        for r in range(len(lines))
        if lines[r][c] == "#"
    ]

    positions = {
        (r, c)
        for c in range(len(lines))
        for r in range(len(lines))
        if lines[r][c] == "S"
    }

    # results = []
    # for i in range(65 + 131 * 2):
    #     positions = simulate_step(positions, rocks, len(lines))
    #     results.append(len(positions))

    # print(results[65 - 1])
    # print(results[65 + 131 - 1])
    # print(results[65 + 131 * 2 - 1])

    # calcutate by my function
    # https://www.reddit.com/r/adventofcode/comments/18nevo3/comment/keaiiq7/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
    # https://github.com/thomasjevskij/advent_of_code/blob/master/2023/aoc21/day21.py
    # then used this formula to get the answere
    # f0 = p(65) f1 = p(65 + 131) f2 = p(65 + 2* 131) | 65 = n, 131 = len(garden)
    # System of equations:
    # f(0) = a*0**2 + b*0 + c = f0, so c = f0
    # f(1) = a*1**2 + b*1 + c = f1, so  a +  b = f1 - f0
    # f(2) = a*2**2 + b*2 + c = f2, so 4a + 2b = f2 - f0
    # Gauss elimination gives:         2a      = f2 - f0 - 2*(f1 - f0) = f2 - 2f1 + f0
    # This gives:                            b = f1 - f0 - a
    f0 = 3751
    f1 = 33531
    f2 = 92991

    c = f0
    a = (f2 - 2 * f1 + f0) // 2  # Don't worry this is an integer :-)
    b = f1 - f0 - a
    # Now we have our polynomial!
    f = lambda n: a * n**2 + b * n + c
    n = 26501365 // len(lines)
    print(f(n))
    # b0 = f0
    # b1 = f1 - f0
    # b2 = f2 - f1

    # n = 26501365 // len(lines)
    # result = b0 + b1 * n + (n * (n - 1) // 2) * (b2 - b1)

    # print(result)


if STAR == 1:
    starOne()
elif STAR == 2:
    starTwo()
