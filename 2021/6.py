with open("6.txt") as f:
    inp = list(map(int, f.read().split(',')))
def p(d):
    fish = [inp.count(i) for i in range(9)] 
    for i in range(d):
        temp = fish[0]
        for j in range(8):
            fish[j] = fish[j + 1]
        fish[6] += temp
        fish[8] = temp
    return sum(fish)
print(f"{p(80)}\n{p(256)}")