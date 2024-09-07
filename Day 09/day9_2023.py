TEST_MODE = False
STAR = 2

if TEST_MODE:
    with open("test_input.txt") as f:
        lines = f.readlines()
else:
    with open("input.txt") as f:
        lines = f.readlines()


def starOne():
    historys = list(map(lambda x: x.strip().split(" "), lines))
    historys = list(map(lambda x: list(map(lambda y: int(y), x)), historys))

    result = []

    for history in historys:
        i = len(history)

        while history[0:i] != [0] * i:
            for j in range(i - 1):
                history[j] = history[j + 1] - history[j]
            i -= 1

        result.append(sum(history[i:]))

    print(sum(result))
    


def starTwo():
    historys = list(map(lambda x: x.strip().split(" "), lines))
    historys = list(map(lambda x: list(map(lambda y: int(y), x)), historys))

    result = []

    for history in historys:
        i = len(history)

        while history[0:i] != [0] * i:
            tmp = history[0]
            for j in range(i - 1):
                history[j] = history[j + 1] - history[j]
            i -= 1
            history[i] = tmp

        for j in range(i - 1, len(history) - 1):
            history[j + 1] = history[j + 1] - history[j]

        result.append(history[-1])

    print(sum(result))


if STAR == 1:
    starOne()
elif STAR == 2:
    starTwo()
