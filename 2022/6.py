with open('6.in') as f:
    data = f.readline()

def get_char(s, m):
    for i, d in enumerate(s):
        if len(set(s[i:i+m])) == m:
            return i + m

print(get_char(data, 4))
print(get_char(data, 14))