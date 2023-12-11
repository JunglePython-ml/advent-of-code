with open("11.in") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

hashes = []
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == "#":
            hashes.append((i, j))

empty_rows = []
empty_cols = []
for i, line in enumerate(lines):
    if line == "." * len(line):
        empty_rows.append(i)
for j in range(len(lines[0])):
    if all(line[j] == "." for line in lines):
        empty_cols.append(j)

p1 = 0
p2 = 0
for i, h1 in enumerate(hashes):
    for j, h2 in enumerate(hashes[i +1 :]):
        p1 += abs(h1[0] - h2[0]) + abs(h1[1] - h2[1])
        p2 += abs(h1[0] - h2[0]) + abs(h1[1] - h2[1])
        expansion = 0
        if h1[0] > h2[0]:
            expansion += len([x for x in range(h2[0] + 1, h1[0]) if x in empty_rows])
        else:
            expansion += len([x for x in range(h1[0] + 1, h2[0]) if x in empty_rows])
        if h1[1] > h2[1]:
            expansion += len([x for x in range(h2[1] + 1, h1[1]) if x in empty_cols])
        else:
            expansion += len([x for x in range(h1[1] + 1, h2[1]) if x in empty_cols])
        p1 += expansion
        p2 += expansion*999999
print(p1)
print(p2)