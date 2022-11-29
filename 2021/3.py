from collections import Counter

with open("3.txt") as f:
	inp = list(map(int, f.read().split()))
print([Counter(bit).most_common(1)[0] for bit in zip(*inp)])