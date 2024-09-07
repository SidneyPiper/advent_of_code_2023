from numpy import transpose

TEST_MODE = False
STAR = 2

if TEST_MODE:
    with open("test_input.txt") as f:
        lines = f.readlines()
else:
    with open("input.txt") as f:
        lines = f.readlines()


def pattern_transpose(pattern):
    return list(
        map(lambda x: "".join(x), transpose(list(map(lambda x: list(x), pattern))))
    )


def starOne():
    patterns = [[]]

    pattern_index = 0
    for line in lines:
        if line != "\n":
            patterns[pattern_index].append(line.strip())
        else:
            patterns.append([])
            pattern_index += 1

    vertical_mirrors = []
    horizontal_mirrors = []

    for pattern in patterns:
        length = len(pattern)

        for i in range(1, length):
            if 2 * i > length:
                start = 2 * i - length
                end = length
            else:
                start = 0
                end = 2 * i
            up = pattern[start:i]
            down = list(reversed(pattern[i:end]))

            if up == down:
                horizontal_mirrors.append(i)
                break

    for pattern in patterns:
        pattern = pattern_transpose(pattern)
        length = len(pattern)
        for i in range(1, length):
            if 2 * i > length:
                start = 2 * i - length
                end = length
            else:
                start = 0
                end = 2 * i
            up = pattern[start:i]
            down = list(reversed(pattern[i:end]))

            if up == down:
                vertical_mirrors.append(i)
                break

    horizontal_mirrors = list(map(lambda x: x * 100, horizontal_mirrors))
    print(sum(vertical_mirrors + horizontal_mirrors))


def diff_array(a, b):
    if len(a) == len(b):
        diff = 0
        for x, y in zip(a, b):
            for cx, cy in zip(x, y):
                if cx != cy:
                    diff += 1
        return diff
    return -1


def starTwo():
    patterns = [[]]

    pattern_index = 0
    for line in lines:
        if line != "\n":
            patterns[pattern_index].append(line.strip())
        else:
            patterns.append([])
            pattern_index += 1

    vertical_mirrors = []
    horizontal_mirrors = []

    for j, pattern in enumerate(patterns):
        length = len(pattern)
        for i in range(1, length):
            if 2 * i > length:
                start = 2 * i - length
                end = length
            else:
                start = 0
                end = 2 * i
            up = pattern[start:i]
            down = list(reversed(pattern[i:end]))

            diff = diff_array(up, down)
            if diff == 1:
                horizontal_mirrors.append(i)
                break

    for pattern in patterns:
        pattern = pattern_transpose(pattern)
        length = len(pattern)
        for i in range(1, length):
            if 2 * i > length:
                start = 2 * i - length
                end = length
            else:
                start = 0
                end = 2 * i
            up = pattern[start:i]
            down = list(reversed(pattern[i:end]))

            diff = diff_array(up, down)
            if diff == 1:
                vertical_mirrors.append(i)
                break

    horizontal_mirrors = list(map(lambda x: x * 100, horizontal_mirrors))
    print(sum(vertical_mirrors + horizontal_mirrors))


if STAR == 1:
    starOne()
elif STAR == 2:
    starTwo()
