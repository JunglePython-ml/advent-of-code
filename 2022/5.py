import copy
from copy import deepcopy

with open('5.in') as f:
    data = f.read().splitlines()

stacks = [[] for i in range(9)]
for i in data:
    x = 0
    if i.startswith("1"):
        break
    while '[' in i:
        elm = i.index('[') + 1
        x += elm // 4
        stacks[x].append(i[elm])
        i = i[elm:]
stacks = [i[::-1] for i in stacks]
stacks2 = copy.deepcopy(stacks)

for i in data[10:]:
    i = i.split()
    amount, orig, dest = int(i[1]), int(i[3]), int(i[5])

    for j in range(amount):
        stacks[dest - 1].append(stacks[orig - 1].pop())

    stacks2[dest - 1].extend(stacks2[orig - 1][-amount:])
    stacks2[orig - 1] = stacks2[orig - 1][:-amount]

print(''.join([i[-1] for i in stacks]))
print(''.join([i[-1] for i in stacks2]))