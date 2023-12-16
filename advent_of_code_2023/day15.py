from collections import defaultdict


def parse_data(data):
    return data.strip().split(",")


def run_hash_algo(s):
    current_value = 0
    for c in s:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value


def solve_part1(data):
    initialization_sequence = parse_data(data)
    return sum(run_hash_algo(s) for s in initialization_sequence)


def solve_part2(data):
    initialization_sequence = parse_data(data)
    d: dict[int, dict[str, int]] = defaultdict(dict)
    for s in initialization_sequence:
        label, focal_length_str = s.replace("-", "=").split("=")
        focal_length = int(focal_length_str) if focal_length_str else None
        label_hash = run_hash_algo(label)
        if focal_length:
            d[label_hash][label] = focal_length
        elif label in d[label_hash]:
            del d[label_hash][label]

    return sum(
        (label_hash + 1) * slot_number * focal_length
        for label_hash, box in d.items()
        for slot_number, focal_length in enumerate(box.values(), 1)
    )
