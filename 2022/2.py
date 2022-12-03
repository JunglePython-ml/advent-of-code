with open('2.in') as f:
    data = [i.split(' ') for i in f.read().splitlines()]

def score(p1, p2):
    if p1 == 'A':
        if p2 == 'X':
            return 4
        elif p2 == 'Y':
            return 8
        else:
            return 3
    elif p1 == 'B':
        if p2 == 'X':
            return 1
        elif p2 == 'Y':
            return 5
        else:
            return 9
    else:
        if p2 == 'X':
            return 7
        elif p2 == 'Y':
            return 2
        else:
            return 6
def score2(p1, p2):
    if p1 == 'A':
        if p2 == 'X':
            return 3
        elif p2 == 'Y':
            return 4
        else:
            return 8
    elif p1 == 'B':
        if p2 == 'X':
            return 1
        elif p2 == 'Y':
            return 5
        else:
            return 9
    else:
        if p2 == 'X':
            return 2
        elif p2 == 'Y':
            return 6
        else:
            return 7

print(sum([score(i[0], i[1]) for i in data]))
print(sum([score2(i[0], i[1]) for i in data]))