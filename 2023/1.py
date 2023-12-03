DIGITS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open("1.in") as f:
    lines = f.readlines()

p1 = 0
p2 = 0

for line in lines:
    p1_list = []
    p2_list = []
    for i, char in enumerate(line):
        if char.isdigit():
            p1_list.append(int(char))
            p2_list.append(int(char))
        for d, digit in enumerate(DIGITS):
            if line[i:].startswith(digit):
                p2_list.append(d + 1)
    p1 += 10 * p1_list[0] + p1_list[-1]
    p2 += 10 * p2_list[0] + p2_list[-1]

print(p1)
print(p2)
