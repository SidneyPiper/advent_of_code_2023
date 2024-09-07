TEST_MODE = True
STAR = 1

if TEST_MODE:
    with open("test_input.txt") as f:
        lines = f.readlines()
else:
    with open("input.txt") as f:
        lines = f.readlines()


def starOne():
    for i in range(len(lines)):
        lines[i] = (
            lines[i]
            .split(":")[1]
            .strip()
            .replace("     ", " ")
            .replace("   ", " ")
            .replace("  ", " ")
        )

    times = list(map((lambda x: int(x)), lines[0].split(" ")))
    distances = list(map((lambda x: int(x)), lines[1].split(" ")))

    result = 1

    for i, time in enumerate(times):
        tmp = 0
        for t in range(time):
            v = t
            t = abs(time - v) - 1

            dist = v + t * v

            print(
                "race",
                i,
                "distance",
                dist,
            )

            if dist > distances[i]:
                tmp += 1
        result *= tmp

    print(result)


def starTwo():
    for i in range(len(lines)):
        lines[i] = (
            lines[i]
            .split(":")[1]
            .strip()
            .replace("     ", "")
            .replace("   ", "")
            .replace("  ", "")
        )

    times = list(map((lambda x: int(x)), lines[0].split(" ")))
    distances = list(map((lambda x: int(x)), lines[1].split(" ")))

    print(times, distances)

    result = 1

    for i, time in enumerate(times):
        tmp = 0
        for t in range(time):
            v = t
            t = abs(time - v) - 1

            dist = v + t * v

            if dist > distances[i]:
                tmp += 1
        result *= tmp

    print(result)


if STAR == 1:
    starOne()
elif STAR == 2:
    starTwo()
