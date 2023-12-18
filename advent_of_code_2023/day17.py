import heapq
from collections import defaultdict, namedtuple
from enum import Enum


def parse_data(data):
    return [[int(x) for x in line] for line in data.splitlines()]


class Direction(Enum):
    LEFT = (0, -1)
    RIGHT = (0, 1)
    UP = (-1, 0)
    DOWN = (1, 0)


Vertex = namedtuple("Vertex", ["i", "j", "direction", "moves"])


def dijkstra(parsed_data, min_moves, max_moves):
    m = len(parsed_data)
    n = len(parsed_data[0])
    s = Vertex(0, 0, None, 0)

    d: dict[Vertex, float] = defaultdict(lambda: float("inf"))

    d[s] = 0
    q: list[tuple[float, Vertex]] = [(0, s)]
    while q:
        _, v = heapq.heappop(q)
        for next_direction in Direction:
            di, dj = next_direction.value
            ni = v.i + di
            nj = v.j + dj
            if ni < 0 or nj < 0 or ni >= m or nj >= n:
                continue

            is_opposing_direction = v.direction and next_direction == Direction((-v.direction[0], -v.direction[1]))
            is_below_min_moves = v.direction and v.moves < min_moves and next_direction.value != v.direction
            is_at_max_moves = v.direction and v.moves == max_moves and next_direction.value == v.direction

            if is_opposing_direction or is_below_min_moves or is_at_max_moves:
                continue

            next_moves = v.moves + 1 if v.direction == next_direction.value else 1

            to = Vertex(ni, nj, next_direction.value, next_moves)
            weight = parsed_data[ni][nj]

            if d[v] + weight < d[to]:
                d[to] = d[v] + weight
                heapq.heappush(q, (d[to], to))

    return d


def solve_part1(data):
    parsed_data = parse_data(data)
    m = len(parsed_data)
    n = len(parsed_data[0])
    d = dijkstra(parsed_data, min_moves=0, max_moves=3)
    return min(v for k, v in d.items() if k.i == m - 1 and k.j == n - 1)


def solve_part2(data):
    parsed_data = parse_data(data)
    m = len(parsed_data)
    n = len(parsed_data[0])
    min_moves = 4
    d = dijkstra(parsed_data, min_moves=min_moves, max_moves=10)
    return min((v, k) for k, v in d.items() if k.i == m - 1 and k.j == n - 1 and k.moves >= min_moves)[0]
