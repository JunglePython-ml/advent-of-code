inp = [int(i) for i in open("1.txt").read().split()]
incr = lambda x : sum(i < j for i, j in zip(inp, inp[x:]))
print(f"{incr(1)}\n{incr(3)}")

