import pytest

from advent_of_code_2023.day12 import solve_part1, solve_part2

example1 = """\
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


def test_part1():
    assert solve_part1(example1) == 21


@pytest.mark.xfail
def test_part2():
    assert solve_part2(example1) == 525152
