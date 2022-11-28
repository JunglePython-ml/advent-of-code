from itertools import cycle

with open("1.in") as f:
    x = []
    a = 0
    for line in cycle(f):
        a += int(line)
        if a in x:
            print(a)
            break
        x.append(a)

