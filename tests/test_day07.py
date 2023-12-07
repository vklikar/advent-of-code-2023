from advent_of_code_2023.day07 import solve_part1, solve_part2

example1 = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


def test_part1():
    assert solve_part1(example1) == 6440


def test_part2():
    assert solve_part2(example1) == 5905
