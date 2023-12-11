from itertools import combinations


def parse_data(data):
    return data.splitlines()


def get_expanding_rows(universe):
    return [i for i in range(len(universe)) if all(c == "." for c in universe[i])]


def solve(data, multiplier):
    parsed_data = parse_data(data)
    expanding_rows = get_expanding_rows(parsed_data)
    expanding_cols = get_expanding_rows(list(zip(*parsed_data)))
    galaxies = [(i, j) for i in range(len(parsed_data)) for j in range(len(parsed_data[i])) if parsed_data[i][j] == "#"]
    ans = 0
    for a, b in combinations(galaxies, 2):
        di = abs(a[0] - b[0])
        dj = abs(a[1] - b[1])
        expanding_row_count = (multiplier - 1) * sum(1 for i in expanding_rows if a[0] < i < b[0] or b[0] < i < a[0])
        expanding_col_count = (multiplier - 1) * sum(1 for i in expanding_cols if a[1] < i < b[1] or b[1] < i < a[1])
        ans += di + dj + expanding_row_count + expanding_col_count
    return ans


def solve_part1(data):
    return solve(data, 2)


def solve_part2(data, multiplier=1_000_000):
    return solve(data, multiplier)
