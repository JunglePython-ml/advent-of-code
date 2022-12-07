with open("7.in") as f:
    data = f.read().splitlines()

fs = {('/',): 0}
pwd = []

for i in data:
    match i.split():
        case ["$", "ls"]:
            pass
        case ["$", "cd", ".."]:
            pwd.pop()
        case ["$", "cd", d]:
            pwd.append(d)
        case ["dir", d]:
            fs[tuple(pwd + [d])] = 0
        case [size, name]:
            print(pwd)
            for i, j in enumerate(pwd):
                fs[tuple(pwd[:i+1])] += int(size)
        case _:
            pass

print(sum(x for x in fs.values() if x <= 100000))
print(min(x for x in fs.values() if x >= 30000000 + fs[('/',)] - 70000000))