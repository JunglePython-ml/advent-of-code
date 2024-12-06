
import numpy as np
from itertools import cycle

with open('6.in') as f:
    data = f.read().splitlines()
    START = np.where(np.array([list(x) for x in data]) == '^')
    START = (int(START[0][0]), int(START[1][0]))
    data = [[1 if x == '#' else 0 for x in line] for line in data]
    grid = np.array(data)


directions = cycle([(-1,0), (0,1), (1,0), (0,-1)])
direction = next(directions)
pos = START

seen = set()
seen.add(pos)
while True:
    candidate_pos = (pos[0] + direction[0], pos[1] + direction[1])
    if candidate_pos[0] < 0 or candidate_pos[0] >= grid.shape[0] or candidate_pos[1] < 0 or candidate_pos[1] >= grid.shape[1]:
        break
    if grid[candidate_pos] == 1:
        direction = next(directions)
        continue
    if grid[candidate_pos] == 0:
        pos = candidate_pos
        seen.add(pos)
print(len(seen))

def find_path(grid, pos, directions):
    directions = cycle([(-1,0), (0,1), (1,0), (0,-1)])
    direction = next(directions)
    pos = START
    seen = set()
    seen.add(pos)
    while True:
        candidate_pos = (pos[0] + direction[0], pos[1] + direction[1])
        if candidate_pos[0] < 0 or candidate_pos[0] >= grid.shape[0] or candidate_pos[1] < 0 or candidate_pos[1] >= grid.shape[1]:
            return False
        if (candidate_pos, direction) in seen:
            return True
        if grid[candidate_pos] == 1:
            direction = next(directions)
            continue
        if grid[candidate_pos] == 0:
            pos = candidate_pos
            seen.add((pos, direction))

ans = 0
for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        if grid[i,j] == 0:
            grid[i,j] = 1
            if find_path(grid, pos, directions):
                ans += 1
            grid[i,j] = 0
print(ans)