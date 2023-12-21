import numpy as np

with open("13.in") as f:
    lines = f.read().split('\n\n')
    lines = [line.split('\n') for line in lines]
    lines = [[[char for char in line] for line in pattern if line] for pattern in lines]

for d in [0, 1]:
    ans = 0
    for pattern in lines:
        pattern = np.array(pattern)
        for x in [100, 1]:
            for r in range(pattern.shape[0]):
                diffs = 0
                for i, j in zip(pattern[r-1::-1], pattern[r:]):
                    diffs += np.sum(i != j)
                if diffs == d:
                    ans += r*x
            pattern = pattern.T
    print(ans)