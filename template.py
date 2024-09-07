TEST_MODE = True
STAR = 1

if TEST_MODE:
    with open("test_input.txt") as f:
        lines = f.readlines()
else:
    with open("input.txt") as f:
        lines = f.readlines()


def starOne():
    pass


def starTwo():
    pass


if STAR == 1:
    starOne()
elif STAR == 2:
    starTwo()
