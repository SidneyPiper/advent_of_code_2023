TEST_MODE = False
STAR = 2

if TEST_MODE:
    with open("test_input.txt") as f:
        lines = f.readlines()
else:
    with open("input.txt") as f:
        lines = f.readlines()


def hash(str):
    current_value = 0

    for char in str:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256

    return current_value


def starOne():
    steps = []
    for line in lines:
        line = line.strip().split(",")
        for step in line:
            if step != "":
                steps.append(step)

    result = 0

    for step in steps:
        result += hash(step)

    print(result)


def starTwo():
    steps = []
    for line in lines:
        line = line.strip().split(",")
        for step in line:
            if step != "":
                if "=" in step:
                    label, num = step.split("=")
                else:
                    label = step[:-1]
                    num = 0
                steps.append([label, num])

    boxes = {i: [] for i in range(256)}

    for label, num in steps:
        box_number = hash(label)
        box = boxes[box_number]

        index = -1

        for i, l in enumerate(box):
            if l[0] == label:
                index = i

        if num == 0:
            if index != -1:
                del box[index]
        else:
            if index != -1:
                del box[index]
                box.insert(index, [label, num])
            else:
                box.append([label, num])

    result = 0

    for i, box in boxes.items():
        for j, (_, n) in enumerate(box):
            result += (i + 1) * (j + 1) * int(n)

    print(result)

if STAR == 1:
    starOne()
elif STAR == 2:
    starTwo()
