def parse_data(data):
    return [[int(x) for x in line.split()] for line in data.splitlines()]


def f(parsed_data):
    ans = 0
    for line in parsed_data:
        xs = line
        diffs = [xs]
        while not all(x == 0 for x in xs):
            xs = [xs[i + 1] - xs[i] for i in range(len(xs) - 1)]
            diffs.append(xs)
        for i in range(len(diffs) - 2, -1, -1):
            diffs[i].append(diffs[i + 1][-1] + diffs[i][-1])
        ans += diffs[0][-1]
    return ans


def solve_part1(data):
    parsed_data = parse_data(data)
    return f(parsed_data)


def solve_part2(data):
    parsed_data = parse_data(data)
    return f(line[::-1] for line in parsed_data)
