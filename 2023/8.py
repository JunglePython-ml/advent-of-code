from collections import defaultdict
import math

with open("8.in") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    directions = lines[0]

    mapping = defaultdict(tuple)
    for line in lines[2:]:
        line = line.split(" = ")
        mapping[line[0]] = tuple(line[1].strip(")").strip("(").split(", "))
    current = "AAA"
    p1 = 0
    dir_index = 0
    while current != "ZZZ":
        p1 += 1
        if directions[dir_index % len(directions)] == "R":
            current = mapping[current][1]
        else:
            current = mapping[current][0]
        dir_index += 1
    p2 = 0
    dir_index = 0
    current = []
    for s in mapping:
        if s.endswith("A"):
            current.append(s)
    cycles = []
    for c in current:
        dir_index = 0
        new_cycle = []
        while not c.endswith("Z"):
            new_cycle.append(c)
            if directions[dir_index % len(directions)] == "R":
                c = mapping[c][1]
            else:
                c = mapping[c][0]
            dir_index += 1
        cycles.append(new_cycle)
    print(p1)
    print(math.lcm(*[len(cycle) for cycle in cycles]))