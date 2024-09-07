TEST_MODE = False
STAR = 2

if TEST_MODE:
    with open("test_input.txt") as f:
        lines = f.readlines()
else:
    with open("input.txt") as f:
        lines = f.readlines()


def starOne():
    bricks = list(
        map(
            lambda p: [
                tuple(map(lambda x: int(x), p[0].split(","))),
                tuple(map(lambda x: int(x), p[1].split(","))),
            ],
            map(lambda l: l.strip().split("~"), lines),
        )
    )

    bricks = sorted(bricks, key=lambda x: min(x[0][2], x[1][2]))

    max_x = 0
    max_y = 0
    max_z = 0

    for (x1, y1, z1), (x2, y2, z2) in bricks:
        if max(x1, x2) > max_x:
            max_x = max(x1, x2)
        if max(y1, y2) > max_y:
            max_y = max(y1, y2)
        if max(z1, z2) > max_z:
            max_z = max(z1, z2)

    tower = [
        [[0 for z in range(max_z + 1)] for y in range(max_y + 1)]
        for x in range(max_x + 1)
    ]

    for x in range(max_x + 1):
        for y in range(max_y + 1):
            tower[x][y][0] = "-"

    for i, ((x1, y1, z1), (x2, y2, z2)) in enumerate(bricks):
        while True:
            under = set()
            for dx in range(x1, x2 + 1):
                for dy in range(y1, y2 + 1):
                    under.add(tower[dx][dy][min(z1, z2) - 1])

            if under != {0}:
                break

            z1 -= 1
            z2 -= 1
            bricks[i] = [(x1, y1, z1), (x2, y2, z2)]

        for dx in range(x1, x2 + 1):
            for dy in range(y1, y2 + 1):
                for dz in range(z1, z2 + 1):
                    tower[dx][dy][dz] = i + 1

    support = {}
    for i, ((x1, y1, z1), (x2, y2, z2)) in enumerate(bricks):
        under = set()
        above = set()
        for dx in range(x1, x2 + 1):
            for dy in range(y1, y2 + 1):
                under.add(tower[dx][dy][min(z1, z2) - 1])
                above.add(tower[dx][dy][max(z1, z2) + 1])

        support[i + 1] = [
            set(filter(lambda x: x == "-" or x > 0, under)),
            set(filter(lambda x: x > 0, above)),
        ]

    removeable = set()
    for item, (_, supports) in support.items():
        r = True
        for x in supports:
            if not support[x][0] - {item}:
                r = False
                break

        if r:
            removeable.add(item)

    print(len(removeable))
    return support, removeable


def check_brick(brick, support):
    fall = {brick}
    stack = [brick]
    while stack:
        nxt = stack.pop(0)
        for x in support[nxt][1]:
            if not support[x][0] - fall:
                fall.add(x)
                stack.append(x)

    return len(fall) - 1


# 98703 too high
def starTwo():
    support, removeable = starOne()

    result = []
    for brick in support:
        if brick in removeable:
            continue
        result.append(check_brick(brick, support))

    print(sum(result))


if STAR == 1:
    starOne()
elif STAR == 2:
    starTwo()
