from typing import Any


def parse_data(data):
    splits = [line.split(":") for line in data.split("\n\n")]
    parsed_data: dict[str | tuple[str, str], Any] = {}
    parsed_data["seeds"] = [int(x) for x in splits[0][1].split()]
    for i in range(1, len(splits)):
        src_name, _, dst_name = splits[i][0].removesuffix(" map").split("-")
        map_name = (src_name, dst_name)
        parsed_data[map_name] = []
        ranges = splits[i][1].strip().split("\n")
        for range_ in ranges:
            dst_start, src_start, length = [int(x) for x in range_.split()]
            parsed_data[map_name].append((dst_start, src_start, length))

    return parsed_data


def get_destination(parsed_data, src):
    return next(mapping[1] for mapping in parsed_data if mapping[0] == src)


def dfs(parsed_data, src, x):
    dst = get_destination(parsed_data, src)
    y = x
    for dst_start, src_start, length in parsed_data[(src, dst)]:
        if src_start <= x < src_start + length:
            y = dst_start + (x - src_start)

    return y if dst == "location" else dfs(parsed_data, dst, y)


def dfs_range(parsed_data, src, x):
    dst = get_destination(parsed_data, src)
    ys = []
    for dst_start, src_start, length in parsed_data[(src, dst)]:
        src_end = src_start + length - 1
        dst_end = dst_start + length - 1

        if src_start < x[1] and x[0] < src_end:
            diff_start = max(0, x[0] - src_start)
            diff_end = max(0, src_end - x[1])
            ys.append((dst_start + diff_start, dst_end - diff_end))

    if not ys:
        ys.append(x)

    return min([y[0] for y in ys] if dst == "location" else [dfs_range(parsed_data, dst, y) for y in ys])


def solve_part1(data):
    parsed_data = parse_data(data)
    return min(dfs(parsed_data, "seed", seed) for seed in parsed_data["seeds"])


def solve_part2(data):
    parsed_data = parse_data(data)
    return min(
        dfs_range(parsed_data, "seed", (start, start + length - 1))
        for start, length in zip(*[iter(parsed_data["seeds"])] * 2)
    )
