from functools import reduce
from math import lcm

TEST_MODE = False
STAR = 2

if TEST_MODE:
    with open("test_input.txt") as f:
        lines = f.readlines()
else:
    with open("input.txt") as f:
        lines = f.readlines()


def starOne():
    instructions = list(lines[0].strip())
    map_ = list(map(lambda x: x.strip(), lines[2:-1]))
    map_ = list(
        map(
            lambda x: x.replace(" ", "")
            .replace("(", "")
            .replace(")", "")
            .replace(",", "=")
            .split("="),
            map_,
        )
    )

    map_ = {x[0]: {"L": x[1], "R": x[2]} for x in map_}

    i = 0
    start = "AAA"
    end = "ZZZ"

    position = start

    while True:
        current_instruction = instructions[i % len(instructions)]
        next_position = map_.get(position).get(current_instruction)

        if next_position == end:
            break

        position = next_position
        i += 1

    i += 1
    print(i)


def starTwo():
    instructions = list(lines[0].strip())
    map_ = list(map(lambda x: x.strip(), lines[2:]))

    map_ = list(
        map(
            lambda x: x.replace(" ", "")
            .replace("(", "")
            .replace(")", "")
            .replace(",", "=")
            .split("="),
            map_,
        )
    )

    map_ = {x[0]: {"L": x[1], "R": x[2]} for x in map_}

    positions = list(filter(lambda x: x[0][2] == "A", map_.items()))

    positions = list(map(lambda x: x[0], positions))

    counter = [0] * len(positions)

    for index, position in enumerate(positions):
        i = 0
        while True:
            current_instruction = instructions[i % len(instructions)]
            next_position = map_.get(position).get(current_instruction)

            if next_position[2] == "Z":
                counter[index] = i + 1
                break

            position = next_position
            i += 1

    print(lcm(*counter))
    # print(reduce(lambda x, y: lcm(x, y), counter))


if STAR == 1:
    starOne()
elif STAR == 2:
    starTwo()
