from collections import namedtuple
from enum import Enum

Point = namedtuple("Point", ["x", "y"])


class Direction(Enum):
    LEFT = (0, -1)
    RIGHT = (0, 1)
    UP = (-1, 0)
    DOWN = (1, 0)


def parse_dig_plan1(data):
    dig_plan = []
    directions = {"L": Direction.LEFT, "R": Direction.RIGHT, "U": Direction.UP, "D": Direction.DOWN}
    for line in data.splitlines():
        direction_str, length_str, _ = line.split()
        dig_plan.append((directions[direction_str], int(length_str)))
    return dig_plan


def parse_dig_plan2(data):
    dig_plan = []
    directions = {"2": Direction.LEFT, "0": Direction.RIGHT, "3": Direction.UP, "1": Direction.DOWN}
    for line in data.splitlines():
        _, hex_digits = line.removesuffix(")").split("#")
        dig_plan.append((directions[hex_digits[-1]], int(hex_digits[:5], base=16)))
    return dig_plan


def get_polygon_points(dig_plan):
    points = []
    x = 0
    y = 0
    for direction, distance in dig_plan:
        points.append(Point(x, y))
        dx, dy = direction.value
        x += dx * distance
        y += dy * distance
    return points


def shoelace_formula(points):
    """
    Return the area of the polygon defined by `points`.
    """
    # https://en.wikipedia.org/wiki/Shoelace_formula
    return abs(
        sum((points[i - 1].x * points[i].y) - (points[i].x * points[i - 1].y) for i in range(1, len(points))) / 2
    )


def picks_theorem(area, boundary_points_count):
    """
    Return the number of interior points.
    """
    # https://en.wikipedia.org/wiki/Pick%27s_theorem
    # Formula: area = interior_points_count + boundary_points_count / 2 + 1
    # -> interior_points_count is unknown
    return area - boundary_points_count / 2 + 1


def solve_part1(data):
    dig_plan = parse_dig_plan1(data)
    boundary_points_count = sum(x[1] for x in dig_plan)
    polygon_points = get_polygon_points(dig_plan)
    polygon_area = shoelace_formula(polygon_points)
    return int(picks_theorem(polygon_area, boundary_points_count) + boundary_points_count)


def solve_part2(data):
    dig_plan = parse_dig_plan2(data)
    boundary_points_count = sum(x[1] for x in dig_plan)
    polygon_points = get_polygon_points(dig_plan)
    polygon_area = shoelace_formula(polygon_points)
    return int(picks_theorem(polygon_area, boundary_points_count) + boundary_points_count)
