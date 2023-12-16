from collections import deque
from enum import Enum


class Direction(Enum):
    LEFT = (0, -1)
    RIGHT = (0, 1)
    UP = (-1, 0)
    DOWN = (1, 0)


def parse_data(data):
    return data.splitlines()


def solve(layout, beam_start):
    m = len(layout)
    n = len(layout[0])
    visited = set()
    q = deque([beam_start])
    while q:
        i, j, direction = q.popleft()
        if i < 0 or i >= m or j < 0 or j >= n or (i, j, direction) in visited:
            continue

        visited.add((i, j, direction))

        next_directions = []
        if layout[i][j] == "-" and direction in [Direction.UP, Direction.DOWN]:
            next_directions.extend([Direction.LEFT, Direction.RIGHT])
        elif layout[i][j] == "|" and direction in [Direction.LEFT, Direction.RIGHT]:
            next_directions.extend([Direction.UP, Direction.DOWN])
        elif layout[i][j] == "/":
            next_directions.append(Direction((-direction.value[1], -direction.value[0])))
        elif layout[i][j] == "\\":
            next_directions.append(Direction((direction.value[1], direction.value[0])))
        else:
            next_directions.append(direction)

        q.extend((i + d.value[0], j + d.value[1], d) for d in next_directions)

    return len(set((i, j) for i, j, _ in visited))


def solve_part1(data):
    layout = parse_data(data)
    return solve(layout, (0, 0, Direction.RIGHT))


def solve_part2(data):
    layout = parse_data(data)
    m = len(layout)
    n = len(layout[0])
    beam_starts = []
    for i in range(m):
        beam_starts.append((i, 0, Direction.RIGHT))
        beam_starts.append((i, n - 1, Direction.LEFT))
    for j in range(n):
        beam_starts.append((0, j, Direction.DOWN))
        beam_starts.append((m - 1, j, Direction.UP))

    return max(solve(layout, beam_start) for beam_start in beam_starts)
