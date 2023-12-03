import re
from collections import defaultdict

with open("2.in") as f:
    lines = f.readlines()

game_bounds = {"red": 12, "green": 13, "blue": 14}

p1 = 0
p2 = 0
for game, line in enumerate(lines):
    line = re.sub("^Game [0-9]+: ", "", line)
    line = re.sub("[,;]", "", line)
    line = re.findall(r"([0-9]+) ([a-z]+)", line)
    valid = True

    most_cubes = defaultdict(int)
    for color in game_bounds:
        m = max([int(x[0]) for x in line if x[1] == color])
        most_cubes[color] = m
        if m < game_bounds[color]:
            valid = False
    if valid:
        p1 += game + 1
    p2 += most_cubes["red"] * most_cubes["green"] * most_cubes["blue"]

print(p1)
print(p2)