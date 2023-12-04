import re

with open("4.in") as f:
    lines = f.readlines()

p1 = 0
cards = [1] * len(lines)
for game, line in enumerate(lines):
    line = re.sub("^Card * [0-9]+: ", "", line.strip())
    line = line.split(" | ")
    line = [[int(x) for x in y.split()] for y in line]
    n = 0
    for i, x in enumerate(line[0]):
        if x in line[1]:
            n += 1
            cards[n+game] += cards[game]
    p1 += int(2**(n-1))
print(p1)
print(sum(cards))
