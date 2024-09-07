TEST_MODE = False
STAR = 2

if TEST_MODE:
    with open("test_input.txt") as f:
        lines = f.readlines()
else:
    with open("input.txt") as f:
        lines = f.readlines()


def calc_points(instructions):
    points = []
    old = (0, 0)
    circumference = 0

    for direction, length in instructions:
        match direction:
            case "U":
                point = (old[0] - int(length), old[1])
            case "D":
                point = (old[0] + int(length), old[1])
            case "L":
                point = (old[0], old[1] - int(length))
            case "R":
                point = (old[0], old[1] + int(length))

        circumference += int(length)
        points.append(point)
        old = point

    return points, circumference


def calc_area(points, circumference):
    area = 0
    for i in range(len(points)):
        area += (points[i][1] + points[(i + 1) % len(points)][1]) * (
            points[i][0] - points[(i + 1) % len(points)][0]
        )

    area /= 2
    circumference /= 2
    return int(area + circumference + 1)


def starOne():
    instructions = list(map(lambda x: x.strip().split()[:2], lines))

    points, circumference = calc_points(instructions)
    print(calc_area(list(reversed(points)), circumference))


def convert_instructions(instructions):
    instructions_ = []
    for direction, length in instructions:
        match direction:
            case "0":
                direction = "R"
            case "1":
                direction = "D"
            case "2":
                direction = "L"
            case "3":
                direction = "U"

        length = int(length, 16)
        instructions_.append([direction, length])

    return instructions_


def starTwo():
    instructions = list(map(lambda x: x.strip().split()[2], lines))
    instructions = list(
        map(
            lambda x: [
                x[7:8],
                x[2:7],
            ],
            instructions,
        )
    )

    instructions = convert_instructions(instructions)

    points, circumference = calc_points(instructions)
    print(calc_area(list(reversed(points)), circumference))


if STAR == 1:
    starOne()
elif STAR == 2:
    starTwo()
