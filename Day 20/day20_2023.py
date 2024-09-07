from math import prod, lcm

TEST_MODE = False
STAR = 2

if TEST_MODE:
    with open("test_input2.txt") as f:
        lines = f.readlines()
else:
    with open("input.txt") as f:
        lines = f.readlines()


def send_signal(signal, receiver, sender, queue, modules):
    if receiver == "rx" or receiver == "output":
        # print(modules["cl"][1])
        return

    module_type, state, outputs = modules[receiver]
    match module_type:
        case "-":
            for output in outputs:
                queue.append((receiver, output, signal))
        case "%":
            if signal == False:
                for output in outputs:
                    queue.append((receiver, output, not state))
                modules[receiver][1] = not state
        case "&":
            modules[receiver][1][sender] = signal
            if all(modules[receiver][1].values()):
                for output in outputs:
                    queue.append((receiver, output, False))
            else:
                for output in outputs:
                    queue.append((receiver, output, True))


def push_button(modules, i):
    queue = [("button", "broadcaster", False)]
    signals = {True: 0, False: 0}
    rx = 0

    while queue:
        sender, receiver, signal = queue.pop(0)
        signals[signal] += 1
        send_signal(signal, receiver, sender, queue, modules)
        if signal and receiver == "cl":
            print(i, modules[receiver][1])

    return signals[True], signals[False], rx


def starOne():
    modules = {}
    modules_raw = list(map(lambda x: x.strip().replace(" ", "").split("->"), lines))
    modules_raw = list(map(lambda x: [x[0], x[1].split(",")], modules_raw))
    for module, outputs in modules_raw:
        if module[0] == "%":
            module_type, module, state = "%", module[1:], False
        elif module[0] == "&":
            module_type, module, state = "&", module[1:], {}
        else:
            module_type, state = "-", None

        modules[module] = [module_type, state, outputs]

    for module, (_, _, outputs) in modules.items():
        for output in outputs:
            if output == "rx" or output == "output":
                continue
            module_type, state, _ = modules[output]
            if module_type == "&":
                state[module] = False

    signals = {True: 0, False: 0}
    for i in range(1000):
        high_signals, low_signals, _ = push_button(modules, i)
        signals[True] += high_signals
        signals[False] += low_signals

    print(prod(signals.values()))


def starTwo():
    modules = {}
    modules_raw = list(map(lambda x: x.strip().replace(" ", "").split("->"), lines))
    modules_raw = list(map(lambda x: [x[0], x[1].split(",")], modules_raw))
    for module, outputs in modules_raw:
        if module[0] == "%":
            module_type, module, state = "%", module[1:], False
        elif module[0] == "&":
            module_type, module, state = "&", module[1:], {}
        else:
            module_type, state = "-", None

        modules[module] = [module_type, state, outputs]

    for module, (_, _, outputs) in modules.items():
        for output in outputs:
            if output == "rx" or output == "output":
                continue
            module_type, state, _ = modules[output]
            if module_type == "&":
                state[module] = False

    i = 0
    while True:
        if i % 100000 == 0:
            print(i)
        push_button(modules, i + 1)
        i += 1

    print(modules["cl"][1])

    # queue = list(modules["cl"][1].keys())
    # needed_modules = []

    # while queue:
    #     nxt = queue.pop(0)
    #     if modules[nxt][0] != "&":
    #         needed_modules.append(nxt)
    #     else:
    #         print(nxt, modules[nxt])
    #         for m in modules[nxt][1].keys():
    #             queue.append(m)

    # patterns = {m: ["", 0] for m in queue}
    # i = 0
    # while i < 1000000:
    #     push_button(modules)
    #     if i == 0:
    #         for m in needed_modules:
    #             patterns[m][0] += str(int(modules[m][1]))
    #     else:
    #         for m in needed_modules:
    #             if patterns[m][0][-1] != str(int(modules[m][1])):
    #                 patterns[m][1] += 1
    #             if patterns[m][1] < 2:
    #                 patterns[m][0] += str(int(modules[m][1]))
    #     i += 1

    # patterns = list(map(lambda x: len(x[0]) + 1, patterns.values()))

    # for pattern in patterns:
    #     print(pattern)

    # print(lcm(*patterns))


if STAR == 1:
    starOne()
elif STAR == 2:
    starTwo()
