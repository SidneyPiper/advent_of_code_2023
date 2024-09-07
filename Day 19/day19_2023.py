TEST_MODE = False
STAR = 2

if TEST_MODE:
    with open("test_input.txt") as f:
        lines = f.readlines()
else:
    with open("input.txt") as f:
        lines = f.readlines()


def eval_part(x, m, a, s, workflows):
    nxt = "in"

    while nxt != "A" and nxt != "R":
        index = 0
        while not eval(str(workflows[nxt][index][0])):
            index += 1
        nxt = workflows[nxt][index][1]

    if nxt == "A":
        return x + m + a + s
    else:
        return 0


def starOne():
    split_index = lines.index("\n")
    workflows_raw = list(map(str.strip, lines[:split_index]))
    workflows = {}
    for workflow in workflows_raw:
        name, instructions = workflow[:-1].split("{")
        instructions = instructions.split(",")
        for i, instruction in enumerate(instructions):
            if ":" in instruction:
                condition, result = instruction.split(":")
            else:
                condition, result = True, instruction
            instructions[i] = (condition, result)
        workflows[name] = instructions

    parts = list(map(str.strip, lines[split_index + 1 :]))
    parts = list(
        map(
            lambda part: list(
                map(lambda x: int(x.split("=")[1]), part[:-1].split(","))
            ),
            parts,
        )
    )

    result = 0
    for x, m, a, s in parts:
        result += eval_part(x, m, a, s, workflows)

    print(result)


def recurse_workflow(x, m, a, s, nxt, index, workflows, result=0):
    if nxt == "A":
        return len(x) * len(m) * len(a) * len(s)
    if nxt == "R":
        return 0

    current_condition = workflows[nxt][index][0]

    if current_condition == True:
        result += recurse_workflow(x, m, a, s, workflows[nxt][index][1], 0, workflows)
    elif current_condition[1] == "<":
        if current_condition[0] == "x":
            split_index = x.index(int(current_condition[2]))
            x1, x2 = x[:split_index], x[split_index:]
            result += recurse_workflow(
                x1, m, a, s, workflows[nxt][index][1], 0, workflows
            )
            result += recurse_workflow(x2, m, a, s, nxt, index + 1, workflows)
        elif current_condition[0] == "m":
            split_index = m.index(int(current_condition[2]))
            m1, m2 = m[:split_index], m[split_index:]
            result += recurse_workflow(
                x, m1, a, s, workflows[nxt][index][1], 0, workflows
            )
            result += recurse_workflow(x, m2, a, s, nxt, index + 1, workflows)
        elif current_condition[0] == "a":
            split_index = a.index(int(current_condition[2]))
            a1, a2 = a[:split_index], a[split_index:]
            result += recurse_workflow(
                x, m, a1, s, workflows[nxt][index][1], 0, workflows
            )
            result += recurse_workflow(x, m, a2, s, nxt, index + 1, workflows)
        elif current_condition[0] == "s":
            split_index = s.index(int(current_condition[2]))
            s1, s2 = s[:split_index], s[split_index:]
            result += recurse_workflow(
                x, m, a, s1, workflows[nxt][index][1], 0, workflows
            )
            result += recurse_workflow(x, m, a, s2, nxt, index + 1, workflows)

    elif current_condition[1] == ">":
        if current_condition[0] == "x":
            split_index = x.index(int(current_condition[2]))
            x1, x2 = x[: split_index + 1], x[split_index + 1 :]
            result += recurse_workflow(
                x2, m, a, s, workflows[nxt][index][1], 0, workflows
            )
            result += recurse_workflow(x1, m, a, s, nxt, index + 1, workflows)
        elif current_condition[0] == "m":
            split_index = m.index(int(current_condition[2]))
            m1, m2 = m[: split_index + 1], m[split_index + 1 :]
            result += recurse_workflow(
                x, m2, a, s, workflows[nxt][index][1], 0, workflows
            )
            result += recurse_workflow(x, m1, a, s, nxt, index + 1, workflows)
        elif current_condition[0] == "a":
            split_index = a.index(int(current_condition[2]))
            a1, a2 = a[: split_index + 1], a[split_index + 1 :]
            result += recurse_workflow(
                x, m, a2, s, workflows[nxt][index][1], 0, workflows
            )
            result += recurse_workflow(x, m, a1, s, nxt, index + 1, workflows)
        elif current_condition[0] == "s":
            split_index = s.index(int(current_condition[2]))
            s1, s2 = s[: split_index + 1], s[split_index + 1 :]
            result += recurse_workflow(
                x, m, a, s2, workflows[nxt][index][1], 0, workflows
            )
            result += recurse_workflow(x, m, a, s1, nxt, index + 1, workflows)

    return result


def starTwo():
    split_index = lines.index("\n")
    workflows_raw = list(map(str.strip, lines[:split_index]))
    workflows = {}
    for workflow in workflows_raw:
        name, instructions = workflow[:-1].split("{")
        instructions = instructions.split(",")
        for i, instruction in enumerate(instructions):
            if ":" in instruction:
                condition, result = instruction.split(":")
                condition = [condition[:1], condition[1:2], condition[2:]]
            else:
                condition, result = True, instruction
            instructions[i] = (condition, result)
        workflows[name] = instructions

    interval = list(range(1, 4001))

    print(
        recurse_workflow(
            interval,
            interval,
            interval,
            interval,
            "in",
            0,
            workflows,
        )
    )


if STAR == 1:
    starOne()
elif STAR == 2:
    starTwo()
