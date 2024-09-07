from enum import Enum

TEST_MODE = False
STAR = 2

if TEST_MODE:
    with open("test_input.txt") as f:
        lines = f.readlines()
else:
    with open("input.txt") as f:
        lines = f.readlines()

grid = []
beams = []
visited = set()


class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    RIGHT = (0, 1)
    LEFT = (0, -1)


class Beam:
    def __init__(self, position, direction) -> None:
        self.position = position
        self.direction = direction

    def __str__(self) -> str:
        return "Position: " + str(self.position) + ", Direction: " + str(self.direction)

    def update(self):
        self.position = (
            self.position[0] + self.direction.value[0],
            self.position[1] + self.direction.value[1],
        )

        if not (0 <= self.position[0] < len(grid)):
            return False
        if not (0 <= self.position[1] < len(grid[0])):
            return False

        nxt = grid[self.position[0]][self.position[1]]

        global beams, visited
        valid = True

        match self.direction:
            case Direction.UP:
                if nxt == "-":
                    if self.position in visited:
                        return False
                    beams.append(
                        Beam((self.position[0], self.position[1]), Direction.LEFT)
                    )
                    beams.append(
                        Beam((self.position[0], self.position[1]), Direction.RIGHT)
                    )
                    valid = False
                elif nxt == "/":
                    self.direction = Direction.RIGHT
                elif nxt == "\\":
                    self.direction = Direction.LEFT
            case Direction.RIGHT:
                if nxt == "|":
                    if self.position in visited:
                        return False
                    beams.append(
                        Beam((self.position[0], self.position[1]), Direction.UP)
                    )
                    beams.append(
                        Beam((self.position[0], self.position[1]), Direction.DOWN)
                    )
                    valid = False
                elif nxt == "/":
                    self.direction = Direction.UP
                elif nxt == "\\":
                    self.direction = Direction.DOWN
            case Direction.DOWN:
                if nxt == "-":
                    if self.position in visited:
                        return False
                    beams.append(
                        Beam((self.position[0], self.position[1]), Direction.LEFT)
                    )
                    beams.append(
                        Beam((self.position[0], self.position[1]), Direction.RIGHT)
                    )
                    valid = False
                elif nxt == "/":
                    self.direction = Direction.LEFT
                elif nxt == "\\":
                    self.direction = Direction.RIGHT
            case Direction.LEFT:
                if nxt == "|":
                    if self.position in visited:
                        return False
                    beams.append(
                        Beam((self.position[0], self.position[1]), Direction.UP)
                    )
                    beams.append(
                        Beam((self.position[0], self.position[1]), Direction.DOWN)
                    )
                    valid = False
                elif nxt == "/":
                    self.direction = Direction.DOWN
                elif nxt == "\\":
                    self.direction = Direction.UP
            case _:
                pass

        visited.add(self.position)

        return valid


def printGrid():
    for r in grid:
        print("".join(r))


def starOne():
    global grid, beams, visited
    grid = list(map(lambda x: list(x.strip()), lines))

    beams.append(Beam((0, -1), Direction.RIGHT))
    visited.add((0, 0))

    while beams:
        for beam in beams.copy():
            if not beam.update():
                beams.remove(beam)

    print(len(visited))


def starTwo():
    global grid, beams, visited
    grid = list(map(lambda x: list(x.strip()), lines))

    energy = []

    for i in range(len(grid)):
        beams = []
        visited = set()

        beams.append(Beam((i, -1), Direction.RIGHT))
        visited.add((i, 0))

        while beams:
            for beam in beams.copy():
                if not beam.update():
                    beams.remove(beam)

        energy.append(len(visited))

        beams = []
        visited = set()

        beams.append(Beam((i, len(grid)), Direction.LEFT))
        visited.add((i, len(grid) - 1))

        while beams:
            for beam in beams.copy():
                if not beam.update():
                    beams.remove(beam)

        energy.append(len(visited))

    for i in range(len(grid[0])):
        beams = []
        visited = set()

        beams.append(Beam((-1, i), Direction.DOWN))
        visited.add((0, i))

        while beams:
            for beam in beams.copy():
                if not beam.update():
                    beams.remove(beam)

        energy.append(len(visited))

        beams = []
        visited = set()

        beams.append(Beam((len(grid[0]), i), Direction.UP))
        visited.add((len(grid[0]) - 1, i))

        while beams:
            for beam in beams.copy():
                if not beam.update():
                    beams.remove(beam)

        energy.append(len(visited))

    print(max(energy))


if STAR == 1:
    starOne()
elif STAR == 2:
    starTwo()
