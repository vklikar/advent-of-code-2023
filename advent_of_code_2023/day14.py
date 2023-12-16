def parse_data(data):
    return [list(line) for line in data.splitlines()]


def traverse(platform):
    platform[:] = list(list(line) for line in zip(*platform))


def reverse(platform):
    platform.reverse()


def roll_north(platform):
    for i in range(1, len(platform)):
        for j in range(len(platform[0])):
            if platform[i][j] == "O" and platform[i - 1][j] == ".":
                k = i - 1
                while k - 1 >= 0 and platform[k - 1][j] == ".":
                    k -= 1
                platform[k][j] = "O"
                platform[i][j] = "."


def roll_west(platform):
    traverse(platform)
    roll_north(platform)
    traverse(platform)


def roll_south(platform):
    reverse(platform)
    roll_north(platform)
    reverse(platform)


def roll_east(platform):
    traverse(platform)
    reverse(platform)
    roll_north(platform)
    reverse(platform)
    traverse(platform)


def get_total_load(platform):
    return sum((len(platform) - i) * row.count("O") for i, row in enumerate(platform))


def solve_part1(data):
    platform = parse_data(data)
    roll_north(platform)
    return get_total_load(platform)


def solve_part2(data):
    platform = parse_data(data)

    visited: dict[tuple[tuple[str, ...], ...], int] = {}
    computed_loads: list[int] = []

    CYCLES = 1_000_000_000

    for i in range(CYCLES):
        frozen_platform = tuple(tuple(x) for x in platform)
        if frozen_platform in visited:
            loop_size = i - visited[frozen_platform]
            non_loop_size = len(visited) - loop_size
            return computed_loads[non_loop_size + (CYCLES - non_loop_size) % loop_size]
        else:
            visited[frozen_platform] = i
            computed_loads.append(get_total_load(platform))

        roll_north(platform)
        roll_west(platform)
        roll_south(platform)
        roll_east(platform)

    return get_total_load(platform)
