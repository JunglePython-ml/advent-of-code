import numpy as np

with open("8.in") as f:
    data = np.array([[int(i) for i in j] for j in f.read().splitlines()])

def visable(x, y):
    return np.all(data[x, y + 1:] < data[x, y]) or np.all(data[x, :y] < data[x, y]) or np.all(data[x + 1:, y] < data[x, y]) or np.all(data[:x, y] < data[x, y])

def scenic(x, y):
    score = 1
    for i, j in [1, 0], [-1, 0], [0, 1], [0, -1]:
        s = 0
        k, l = x + i, y + j
        while 0 <= k < data.shape[0] and 0 <= l < data.shape[1]:
            s += 1
            if data[k, l] >= data[x, y]:
                break
            k, l = k + i, l + j
        score *= s
    return score


print(np.sum([visable(x, y) for x in range(data.shape[0]) for y in range(data.shape[1])]))
print(np.max([scenic(x, y) for x in range(data.shape[0]) for y in range(data.shape[1])]))