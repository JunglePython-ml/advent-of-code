with open('4.in') as f:
    chars = [[c for c in line.strip()] for line in f]

directions = ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1))


starts = [(x,y) for y in range(len(chars)) for x in range(len(chars[y])) if chars[y][x] == 'X']
xmas = 'XMAS'
ans = 0

for i in starts:
    for d in directions:
        for j in range(1, 4):
            x, y = i[0] + d[0] * j, i[1] + d[1] * j
            if x < 0 or x >= len(chars[0]) or y < 0 or y >= len(chars):
                break
            if chars[y][x] != xmas[j]:
                break
        else:
            ans += 1
print(ans)

directions = ((1, 1), (-1, 1), (-1, -1), (1, -1))

starts = [(x,y) for y in range(len(chars)) for x in range(len(chars[y])) if chars[y][x] == 'A']
ans = 0
for i in starts:
    tally = 0
    for d in directions:
        x1, y1, x2, y2 = i[0] - d[0], i[1] - d[1], i[0] + d[0], i[1] + d[1]
        if x1 < 0 or x1 >= len(chars[0]) or y1 < 0 or y1 >= len(chars):
            continue
        if x2 < 0 or x2 >= len(chars[0]) or y2 < 0 or y2 >= len(chars):
            continue
        if chars[y1][x1] == 'M' and chars[y2][x2] == 'S':
            tally += 1
    if tally > 1:
        ans += 1

print(ans)