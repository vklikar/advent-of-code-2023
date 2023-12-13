def parse_data(data):
    return [x.splitlines() for x in data.split("\n\n")]


def is_reflected(pattern, i, j, smudges_allowed: int = 0):
    if i < 0 or j == len(pattern):
        return True

    if not smudges_allowed:
        if pattern[i] == pattern[j]:
            return is_reflected(pattern, i - 1, j + 1)
    else:
        smudges_removed = sum(1 for a, b in zip(pattern[i], pattern[j]) if a != b)
        if smudges_removed > 1:
            return False
        return is_reflected(pattern, i - 1, j + 1, smudges_allowed - smudges_removed)

    return False


def get_row_reflection_count(pattern, smudges_allowed: int = 0, ignored: int = 0):
    for i in range(len(pattern) - 1):
        if i + 1 == ignored:
            continue
        if is_reflected(pattern, i, i + 1, smudges_allowed):
            return i + 1
    return 0


def solve_part1(data):
    patterns = parse_data(data)
    ans = 0
    for pattern in patterns:
        transposed_pattern = list(zip(*pattern))
        ans += get_row_reflection_count(transposed_pattern) or 100 * get_row_reflection_count(pattern)
    return ans


def solve_part2(data):
    patterns = parse_data(data)
    ans = 0
    for pattern in patterns:
        transposed_pattern = list(zip(*pattern))
        ans += get_row_reflection_count(
            transposed_pattern, 1, get_row_reflection_count(transposed_pattern)
        ) or 100 * get_row_reflection_count(pattern, 1, get_row_reflection_count(pattern))
    return ans
