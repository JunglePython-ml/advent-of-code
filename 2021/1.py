with open("1.in") as f:
	inp = list(map(int, f.read().split()))
k = lambda x : sum(i < j for i, j in zip(inp, inp[x:]))
print(f"{k(1)}\n{k(3)}")