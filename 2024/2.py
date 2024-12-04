with open("2.in") as f:
    digits = [[int(d) for d in line.split()] for line in f]

safe = lambda row: (sorted(row) == row or sorted(row, reverse=True) == row) and all(abs(row[i] - row[i+1]) in (1,2,3) for i in range(len(row)-1))
print(sum(safe(row) for row in digits))
print(sum(any(safe(row[:i] + row[i+1:]) for i in range(len(row))) for row in digits))