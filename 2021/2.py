with open("2.txt") as f:
    inp = [i.split() for i in f.readlines()]
p1 = lambda k: sum([int(j) for i, j in inp if i==k])
def p2():
    a = d = 0
    for i, j in inp:
        j = int(j)
        match i:
            case "forward":
                d += a*j
            case "down":
                a += j
            case "up":
                a -= j
    return d
print((p1("down") - p1("up"))*p1("forward"))
print(p2()*p1("forward"))
