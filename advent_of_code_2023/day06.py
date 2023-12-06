from bisect import bisect_left


def parse_data(data):
    parsed_data = {}
    lines = data.splitlines()
    for line in lines:
        name, numbers = line.split(":")
        parsed_numbers = numbers.split()
        parsed_data[name] = parsed_numbers

    return parsed_data


def solve_part1(data):
    parsed_data = parse_data(data)
    ans = 1
    for i in range(len(parsed_data["Time"])):
        time = int(parsed_data["Time"][i])
        distance = int(parsed_data["Distance"][i])
        ans *= sum(1 for speed in range(1, time + 1) if (time - speed) * speed > distance)
    return ans


def solve_part2(data):
    parsed_data = parse_data(data)
    time = int("".join(parsed_data["Time"]))
    distance = int("".join(parsed_data["Distance"]))
    speeds = range(1, time + 1)
    lo = bisect_left(speeds, True, key=lambda speed: (time - speed) * speed > distance)
    hi = bisect_left(speeds[::-1], True, key=lambda speed: -(time - speed) * speed < -distance)
    return speeds[len(speeds) - hi] - speeds[lo]
