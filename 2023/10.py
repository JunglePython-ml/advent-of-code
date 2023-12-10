import numpy as np
import sys

# Recursion goes brrrrrrr
sys.setrecursionlimit(10000000)

with open("10.in") as f:
    lines = f.readlines()
    lines = np.array([line.strip() for line in lines])

BLOW_UP_MAPPING = {
    "L": [[0, 1, 0], [0, 1, 1], [0, 0, 0]],
    "F": [[0, 0, 0], [0, 1, 1], [0, 1, 0]],
    "7": [[0, 0, 0], [1, 1, 0], [0, 1, 0]],
    "J": [[0, 1, 0], [1, 1, 0], [0, 0, 0]],
    "|": [[0, 1, 0], [0, 1, 0], [0, 1, 0]],
    "-": [[0, 0, 0], [1, 1, 1], [0, 0, 0]],
    "S": [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
}
start = None
grid = np.zeros((len(lines) * 3, len(lines[0]) * 3))
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c in BLOW_UP_MAPPING:
            grid[i * 3 : i * 3 + 3, j * 3 : j * 3 + 3] = np.array(BLOW_UP_MAPPING[c])
        if c == "S":
            start = (i * 3 + 1, j * 3 + 1)

main_loop = []

queue = [start]
seen = set()
while queue:
    x, y = queue.pop(0)
    if (x, y) in seen:
        continue
    seen.add((x, y))
    if grid[x, y] == 1:
        main_loop.append((x, y))
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if grid[x + dx, y + dy] == 1:
            queue.append((x + dx, y + dy))

print(len(main_loop) // 6)
grid = np.zeros((len(lines) * 3, len(lines[0]) * 3))
for x, y in main_loop:
    grid[x, y] = 1

visited = set()
def flood_fill(x, y):
    if 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]:
        if grid[x, y] == 1:
            return
        if (x, y) in visited:
            return
        visited.add((x, y))
        grid[x, y] = 2
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            flood_fill(x + dx, y + dy)
flood_fill(0, 0)

# Debugging
p2 = 0
mapping = {
    "F": "╔",
    "7": "╗",
    "J": "╝",
    "L": "╚",
    "-": "═",
    "|": "║",
    "S": "╬",
}
grid2 = [[" "] * len(lines[0]) for _ in range(len(lines))]
for i in range(1, grid.shape[0] - 1, 3):
    for j in range(1, grid.shape[1] - 1, 3):
        x, y = i // 3, j // 3
        if grid[i, j] == 1:
            grid2[x][y] = mapping[lines[x][y]]
            p2 += 1
        if grid[i, j] == 2:
            grid2[x][y] = "O"

print(sum([x.count(" ") for x in grid2]))
