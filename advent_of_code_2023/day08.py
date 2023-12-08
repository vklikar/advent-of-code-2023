import math
import re
from itertools import cycle


def parse_data(data):
    instructions, network = data.split("\n\n")
    network_lines = network.splitlines()
    parsed_data = {}
    for line in network_lines:
        src, dst_l, dst_r = re.findall(r"\w+", line)
        parsed_data[src] = {"L": dst_l, "R": dst_r}
    return instructions, parsed_data


def solve_part1(data):
    instructions, network = parse_data(data)
    current = "AAA"
    for count, instruction in enumerate(cycle(instructions)):
        if current == "ZZZ":
            return count
        current = network[current][instruction]


def solve_part2(data):
    instructions, network = parse_data(data)
    elements = [x for x in network if x.endswith("A")]

    combs: list[set[int]] = []
    for element in elements:
        i = 0
        count = 0
        current = element
        prev = None
        dp = {}
        while current != prev and (current, i) not in dp:
            if current.endswith("Z"):
                dp[(current, i)] = count
            prev, current = current, network[current][instructions[i]]
            count += 1
            i = (i + 1) % len(instructions)

        combs = [xs | {x} for xs in combs for x in dp.values()] if combs else [{x} for x in dp.values()]

    return min(math.lcm(*x) for x in combs)
