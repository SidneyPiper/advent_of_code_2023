import functools

TEST_MODE = False
STAR = 2

if TEST_MODE:
    with open("test_input.txt") as f:
        lines = f.readlines()
else:
    with open("input.txt") as f:
        lines = f.readlines()


def starOne():
    result = 0

    for line in lines:
        line = line.strip().split(" ")
        springs = list(line[0])
        springs_count = list(map(lambda x: int(x), line[1].split(",")))

        count = springs.count("?")

        patterns = []

        for i in range(2**count):
            patterns.append(
                format(i, "0" + str(count) + "b").replace("0", ".").replace("1", "#")
            )

        filter_count = abs(sum(springs_count) - "".join(springs).count("#"))
        patterns = list(filter(lambda x: x.count("#") == filter_count, patterns))

        arrangements = 0

        for pattern in patterns:
            pattern_index = 0
            springs_str = ""

            for x in springs:
                if x == "?":
                    springs_str += pattern[pattern_index]
                    pattern_index += 1
                    continue
                springs_str += x

            pattern_arr = list(
                map(lambda x: len(x), springs_str.replace(".", " ").split())
            )

            if pattern_arr == springs_count:
                arrangements += 1

        result += arrangements

    print(result)


@functools.cache
def find_arrangements(records, springs, result=0):
    if not springs:
        return "#" not in records
    if not records:
        return False

    current_record = records[0]
    current_spring = springs[0]

    if current_spring > len(records):
        return False

    if current_record in ".?":
        result += find_arrangements(records[1:], springs)

    if current_record in "#?":
        slice = records[:current_spring]

        if "." not in slice:
            if current_spring == len(records):
                return len(springs) == 1
            if records[current_spring] in ".?":
                result += find_arrangements(records[current_spring + 1 :], springs[1:])

    return result


def starTwo():
    result = 0

    for line in lines:
        records, springs = line.strip().split()
        records = "?".join([records] * 5)
        springs = tuple(map(lambda x: int(x), springs.split(","))) * 5

        result += find_arrangements(records, springs)

    print(result)


if STAR == 1:
    starOne()
elif STAR == 2:
    starTwo()