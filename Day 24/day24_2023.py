import sympy

TEST_MODE = False
STAR = 2

if TEST_MODE:
    with open("test_input.txt") as f:
        lines = f.readlines()
else:
    with open("input.txt") as f:
        lines = f.readlines()


def starOne():
    stones = list(
        map(
            lambda xs: list(map(lambda x: int(x), xs)),
            map(
                lambda x: filter(
                    lambda y: y not in " @",
                    x.replace("\n", "").replace(",", "").split(" "),
                ),
                lines,
            ),
        )
    )

    if TEST_MODE:
        lower_limit = 7
        upper_limit = 27
    else:
        lower_limit = 200000000000000
        upper_limit = 400000000000000

    n = 0
    for i, (pxa, pya, _, vxa, vya, _) in enumerate(stones):
        for j, (pxb, pyb, _, vxb, vyb, _) in enumerate(stones):
            if j <= i:
                continue

            if (vya - (vxa * vyb / vxb)) == 0:
                continue

            ta = (pyb - pya + ((pxa - pxb) / vxb) * vyb) / (vya - (vxa * vyb / vxb))
            tb = (pxa - pxb) / vxb + (vxa / vxb) * ta

            if ta < 0 or tb < 0:
                continue

            x = ta * vxa + pxa
            y = ta * vya + pya

            if lower_limit <= x <= upper_limit and lower_limit <= y <= upper_limit:
                n += 1

    print(n)


def starTwo():
    stones = list(
        map(
            lambda xs: list(map(lambda x: int(x), xs)),
            map(
                lambda x: filter(
                    lambda y: y not in " @",
                    x.replace("\n", "").replace(",", "").split(" "),
                ),
                lines,
            ),
        )
    )

    rx, ry, rz, rvx, rvy, rvz = sympy.symbols("rx, ry, rz, rvx, rvy, rvz")

    equations = []

    # rx + t * rvx = x + t * vx for alle dimensionen und alle hailstones, das dann nach t umstellen und gleichsetzen für transitive formel
    for x, y, z, vx, vy, vz in stones:
        equations.append((rx - x) * (vy - rvy) - (ry - y) * (vx - rvx))
        equations.append((ry - y) * (vz - rvz) - (rz - z) * (vy - rvy))

    rock = sympy.solve(equations)[0]

    print(rock[rx] + rock[ry] + rock[rz])


if STAR == 1:
    starOne()
elif STAR == 2:
    starTwo()
