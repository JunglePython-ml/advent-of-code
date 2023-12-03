from collections import defaultdict

with open("3.in", "r") as f:
    lines = f.read().split("\n")
    char_grid = [[char for char in line if char] for line in lines]

def is_adjacent(x, y, g=False):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if x+i < 0 or y+j < 0 or y+j == len(char_grid) or x+i == len(char_grid[0]):
                continue
            if char_grid[x+i][y+j] not in "0123456789." and not g:
                return True
            elif char_grid[x+i][y+j] == "*" and g:
                return (x+i, y+j)
    return False

p1 = 0
gears = defaultdict(list)
for i, line in enumerate(char_grid):
    num = ""
    gear_pos = None
    adj = False
    for j, char in enumerate(line):
        if char.isdigit():
            num += char
            if is_adjacent(i, j):
                adj = True
            if pos := is_adjacent(i, j, True):
                gear_pos = pos
        else:
            if num:
                if gear_pos is not None:
                    gears[gear_pos].append(int(num))
            if adj:
                p1 += int(num)
            num = ""
            gear_pos = None
            adj = False
    if adj:
        p1 += int(num)
    if num:
        if gear_pos is not None:
            gears[gear_pos].append(int(num))
print(p1)

p2 = 0
for pos in gears:
    if len(gears[pos]) == 2:
        p2+= gears[pos][0] * gears[pos][1]
print(p2)