with open('4.in') as f:
    data = f.read().splitlines()
    data = [i.split(',') for i in data]
    for i in range(len(data)):
        data[i] = [i.split('-') for i in data[i]]

def valid1(i):
    ab = set(range(int(i[0][0]), int(i[0][1]) + 1))
    cd = set(range(int(i[1][0]), int(i[1][1]) + 1))
    if ab <= cd or cd <= ab:
        return True
    return False

def valid2(i):
    ab = set(range(int(i[0][0]), int(i[0][1]) + 1))
    cd = set(range(int(i[1][0]), int(i[1][1]) + 1))
    if ab & cd:
        return True
    return False

print(sum([valid1(i) for i in data]))
print(sum([valid2(i) for i in data]))