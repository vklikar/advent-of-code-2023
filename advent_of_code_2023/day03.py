from math import prod


def parse_data(data):
    return data.splitlines()


def get_neighbor_coords(i, j, data):
    coords = []
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == dj == 0:
                continue
            ni = i + di
            nj = j + dj
            if 0 <= ni < len(data) and 0 <= nj < len(data[i]):
                coords.append((ni, nj))
    return coords


def get_adjacent_numbers(parsed_data, visited, i, j):
    numbers = []
    for ni, nj in get_neighbor_coords(i, j, parsed_data):
        if parsed_data[ni][nj].isdigit() and not visited[ni][nj]:
            start = end = pos = nj
            while pos >= 0 and parsed_data[ni][pos].isdigit():
                visited[ni][pos] = True
                start = pos
                pos -= 1
            pos = nj + 1
            while pos < len(visited[ni]) and parsed_data[ni][pos].isdigit():
                visited[ni][pos] = True
                end = pos
                pos += 1
            numbers.append(int(parsed_data[ni][start : end + 1]))
    return numbers


def is_symbol(c):
    return not c.isdigit() and c != "."


def is_gear(c):
    return c == "*"


def solve_part1(data):
    parsed_data = parse_data(data)
    m = len(parsed_data)
    n = len(parsed_data[0])
    visited = [[False] * n for _ in range(m)]

    return sum(
        sum(get_adjacent_numbers(parsed_data, visited, i, j))
        for i in range(m)
        for j in range(n)
        if is_symbol(parsed_data[i][j])
    )


def solve_part2(data):
    parsed_data = parse_data(data)
    m = len(parsed_data)
    n = len(parsed_data[0])
    visited = [[False] * n for _ in range(m)]

    gear_numbers = [
        get_adjacent_numbers(parsed_data, visited, i, j)
        for i in range(m)
        for j in range(n)
        if is_gear(parsed_data[i][j])
    ]
    return sum(prod(x) for x in gear_numbers if len(x) == 2)
