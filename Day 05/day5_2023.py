with open("input.txt") as f:
    lines = f.readlines()

seeds = [
    1044452533,
    40389941,
    3710737290,
    407166728,
    1552449232,
    639689359,
    3327654041,
    26912583,
    3440484265,
    219136668,
    1126550158,
    296212400,
    2332393052,
    229950158,
    200575068,
    532702401,
    4163696272,
    44707860,
    3067657312,
    45353528,
]

seeds2 = [
    (1044452533, 40389941),
    (3710737290, 407166728),
    (1552449232, 639689359),
    (3327654041, 26912583),
    (3440484265, 219136668),
    (1126550158, 296212400),
    (2332393052, 229950158),
    (200575068, 532702401),
    (4163696272, 44707860),
    (3067657312, 45353528),
]


def starOne():
    category = 0
    maps = [[]]

    for line in lines:
        if line == "\n":
            maps.append([])
            category += 1
            continue
        line = line.strip().split(" ")

        sourceStart = int(line[1])
        destStart = int(line[0])
        r = int(line[2])

        maps[category].append([sourceStart, sourceStart + r, destStart])

    locations = []

    for seed in [1893460704]:
        for map in maps:
            for x in map:
                if x[0] <= seed < x[1]:
                    seed = x[2] + (seed - x[0])
                    break
        locations.append(seed)

    print(min(locations))


def starTwo():
    category = 0
    maps = [[]]

    for line in lines:
        if line == "\n":
            maps.append([])
            category += 1
            continue
        line = line.strip().split(" ")

        sourceStart = int(line[1])
        destStart = int(line[0])
        r = int(line[2])

        maps[category].append([destStart, destStart + r, sourceStart])

    for seed in range(10834440 + 1):
        for map in reversed(maps):
            for x in map:
                if x[0] <= seed < x[1]:
                    seed = x[2] + (seed - x[0])
                    break
        if testSeed(seed):
            print(seed)
            break

    print("test")


def testSeed(seed):
    for seedPair in seeds2:
        if seedPair[0] <= seed <= seedPair[0] + seedPair[1]:
            return True
    return False


starTwo()
