import re

with open('7.in') as f:
    lines = f.read().splitlines()

def solvable(nums, target, concat=False):
    targets = [nums[0]]
    for i in range(1, len(nums)):
        new_targets = []
        for t in targets:
            new_targets.append(t + nums[i])
            new_targets.append(t * nums[i])
            if concat:
                new_targets.append(int(str(t) + str(nums[i])))
        targets = new_targets
    return target if target in targets else 0

p1,p2 = 0,0
for line in lines:
    target, *nums = map(int, re.findall(r'\d+', line))
    p1 += (s := solvable(nums, target))
    p2 += s if s != 0 else solvable(nums, target, True)
print(p1)
print(p2)