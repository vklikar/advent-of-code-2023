from advent_of_code_2023.day15 import solve_part1, solve_part2

example1 = "HASH"
example2 = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"


def test_part1_ex1():
    assert solve_part1(example1) == 52


def test_part1_ex2():
    assert solve_part1(example2) == 1320


def test_part2():
    assert solve_part2(example2) == 145
