with open('1.in') as f:
    data = f.read().splitlines()
    data = [[int(x), int(y)] for x, y in [x.split() for x in data]]
    
x, y = map(sorted,zip(*data))
part1 = 0
part2 = 0
for i, j in zip(x, y):
    part1 += abs(i - j)
    part2 += i*y.count(i)
print(part1)
print(part2)