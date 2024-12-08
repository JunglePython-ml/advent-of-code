from collections import defaultdict
from itertools import combinations

with open('8.in') as f:
    lines = f.read().splitlines()
    grid = [[c for c in line] for line in lines]

def find_pairs(arr):
    characters = defaultdict(list)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == '.':
                continue
            characters[arr[i][j]].append((i, j))
    pairs = []
    for v in characters.values():
        if len(v) >= 2:
            pairs.extend(combinations(v, 2))
    return pairs

def find_antinodes(pairs, part=1):
    antinodes = []
    for pair in pairs:
        diff = (pair[1][0] - pair[0][0], pair[1][1] - pair[0][1])
        for i in [2] if part == 1 else range(-50, 51):
            antinodes.append((pair[0][0] + diff[0]*i, pair[0][1] + diff[1]*i))
            antinodes.append((pair[1][0] - diff[0]*i, pair[1][1] - diff[1]*i))
    return antinodes

def sum_in_bounds(arr, coords):
    arr = set(coords)
    sum = 0
    for coord in arr:
        if 0 <= coord[0] < len(grid) and 0 <= coord[1] < len(grid[0]):
            sum += 1
    return sum

print(sum_in_bounds(grid, find_antinodes(find_pairs(grid))))
print(sum_in_bounds(grid, find_antinodes(find_pairs(grid), 2)))