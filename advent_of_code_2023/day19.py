import operator

import regex


def parse_data(data):
    workflows_str, machine_parts_str = data.split("\n\n")
    pattern = regex.compile(
        r"(?P<name>\w+)\{(?:(?P<category>\w)(?P<op>[<>])(?P<number>\d+):(?P<target>\w+),)+(?P<otherwise>\w+)\}"
    )
    workflows = {}
    for rule_str in workflows_str.splitlines():
        if m := regex.match(pattern, rule_str):
            rules = [
                (category, {"<": operator.lt, ">": operator.gt}[op], int(number), target)
                for category, op, number, target in zip(
                    m.captures("category"), m.captures("op"), m.captures("number"), m.captures("target")
                )
            ]
            workflows[m.group("name")] = (rules, m.group("otherwise"))

    machine_parts = [
        {x[0]: int(x[1]) for x in regex.findall(r"(\w+)=(\d+)", line)} for line in machine_parts_str.splitlines()
    ]

    return (workflows, machine_parts)


def run_workflow(rules, otherwise, machine_part):
    for rule_category, op, rule_number, target in rules:
        if op(machine_part[rule_category], rule_number):
            return target
    return otherwise


def solve_part1(data):
    workflows, machine_parts = parse_data(data)
    ans = 0
    for machine_part in machine_parts:
        current = "in"
        while current not in ["A", "R"]:
            rules, otherwise = workflows[current]
            current = run_workflow(rules, otherwise, machine_part)
        if current == "A":
            ans += sum(machine_part.values())
    return ans


def solve_part2(data):
    pass
