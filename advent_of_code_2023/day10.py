from enum import Enum


class Direction(Enum):
    """
       S
       |
    E -o- W
       |
       N
    """

    NORTH = (1, 0)
    SOUTH = (-1, 0)
    EAST = (0, -1)
    WEST = (0, 1)


PIPE_CONNECTIONS = {
    Direction.NORTH: "|LJ",
    Direction.SOUTH: "|7F",
    Direction.EAST: "-LF",
    Direction.WEST: "-7J",
}

PIPE_DIRECTIONS = {
    "|": {Direction.NORTH, Direction.SOUTH},
    "-": {Direction.EAST, Direction.WEST},
    "L": {Direction.SOUTH, Direction.WEST},
    "J": {Direction.SOUTH, Direction.EAST},
    "7": {Direction.NORTH, Direction.EAST},
    "F": {Direction.NORTH, Direction.WEST},
}

PIPE_DIRECTIONS_INV = {frozenset(v): k for k, v in PIPE_DIRECTIONS.items()}


def parse_data(data):
    return [list(line) for line in data.splitlines()]


def determine_start_pipe(parsed_data, i, j):
    start_pipe_directions = set()

    for direction in Direction:
        ni = i + direction.value[0]
        nj = j + direction.value[1]
        if (
            0 <= ni < len(parsed_data)
            and 0 <= nj < len(parsed_data[ni])
            and parsed_data[ni][nj] in PIPE_CONNECTIONS[direction]
        ):
            start_pipe_directions.add(direction)

    return PIPE_DIRECTIONS_INV[frozenset(start_pipe_directions)]


def get_adjacent_pipes(parsed_data, i, j):
    current = parsed_data[i][j]
    adjacent_pipes = []
    for direction in PIPE_DIRECTIONS[current]:
        ni = i + direction.value[0]
        nj = j + direction.value[1]
        if 0 <= ni < len(parsed_data) and 0 <= nj < len(parsed_data[ni]) and parsed_data[ni][nj] != ".":
            if parsed_data[ni][nj] in PIPE_CONNECTIONS[direction]:
                adjacent_pipes.append((ni, nj, parsed_data[ni][nj]))

    return adjacent_pipes


def override_start_tile(parsed_data, m, n):
    for i in range(m):
        for j in range(n):
            if parsed_data[i][j] == "S":
                start_pipe = determine_start_pipe(parsed_data, i, j)
                parsed_data[i][j] = start_pipe
                return (i, j, start_pipe)


def build_graph(parsed_data, m, n):
    g = {}
    start_tile = override_start_tile(parsed_data, m, n)
    for i in range(m):
        for j in range(n):
            if parsed_data[i][j] != ".":
                g[(i, j, parsed_data[i][j])] = get_adjacent_pipes(parsed_data, i, j)

    return g, start_tile


def get_loop(parsed_data, m, n):
    loop = [["."] * n for _ in range(m)]
    g, start_tile = build_graph(parsed_data, m, n)
    prev = None
    current = None
    while current != start_tile:
        if current is None:
            current = start_tile
        i, j, pipe = current

        loop[i][j] = pipe
        prev, current = current, next(x for x in g[current] if x != prev)
    return loop


def solve_part1(data):
    parsed_data = parse_data(data)
    m = len(parsed_data)
    n = len(parsed_data[0])
    g, start_tile = build_graph(parsed_data, m, n)

    q = [start_tile]
    visited = set()
    count = 0
    while q:
        next_q = []
        while q:
            current = q.pop()
            visited.add(current)
            for adjacent in g[current]:
                if adjacent not in visited:
                    next_q.append(adjacent)
        q = next_q
        count += 1
    return count - 1


def solve_part2(data):
    parsed_data = parse_data(data)
    m = len(parsed_data)
    n = len(parsed_data[0])
    loop = get_loop(parsed_data, m, n)

    ans = 0
    for i in range(m):
        is_inside = False
        for j in range(n):
            if is_inside and loop[i][j] == ".":
                ans += 1

            if (
                loop[i][j] == "|"
                or (loop[i][j] == "F" and "".join(loop[i][j + 1 :]).lstrip("-").startswith("J"))
                or (loop[i][j] == "L" and "".join(loop[i][j + 1 :]).lstrip("-").startswith("7"))
            ):
                is_inside = not is_inside

    return ans
