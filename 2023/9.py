from numpy.polynomial import Polynomial

with open("9.in") as f:
    lines = f.readlines()
    lines = [list(map(int, line.strip().split())) for line in lines]

p1 = 0
p2 = 0
for line in lines:
    poly = Polynomial.fit(range(len(line)), line, len(line) - 1)
    p1 += int(round(poly(len(line)), 0))
    p2 += int(round(poly(-1), 0))
print(p1)
print(p2)
