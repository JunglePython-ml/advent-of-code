with open('3.in') as f:
    data = f.read().splitlines()

total = 0
for i in data:
    a, b = i[len(i)//2:], i[:len(i)//2]
    x = set(a) & set(b)
    x = x.pop()
    if 'a' <= x <= 'z':
        total += ord(x) - ord('a') + 1
    else:
        total += ord(x) - ord('A') + 27
print(total)

data = [data[i:i+3] for i in range(0, len(data), 3)]
total = 0
for i in data:
    a, b, c = i
    x = set(a) & set(b) & set(c)
    x = x.pop()
    if 'a' <= x <= 'z':
        total += ord(x) - ord('a') + 1
    else:
        total += ord(x) - ord('A') + 27
print(total)
