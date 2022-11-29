from itertools import groupby

with open("10.in") as f:
    inp = list(map(int, f.read()))

def iterate(n):
    global inp
    for i in range(n):
        tmp = ''
        for k, g in groupby(inp):
            tmp += str(len(list(g))) + str(k)
        inp = tmp
    return len(inp)

print(iterate(40))
print(iterate(10))


