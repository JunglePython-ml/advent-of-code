import re
with open('3.in') as f:

    lines = ''.join(f.readlines())
    mul = re.findall(r'mul\((\d+),(\d+)\)', lines)
    funcs = [x.group() for x in re.finditer(r'mul\((\d+),(\d+)\)|do\(\)|don\'t\(\)', lines)]
    print(sum(int(x)*int(y) for x, y in mul))

part2 = 0
enabled = True
for func in funcs:
    if func == 'do()':
        enabled = True
    elif func == 'don\'t()':
        enabled = False
    elif enabled:
        x, y = re.match(r'mul\((\d+),(\d+)\)', func).groups()
        part2 += int(x)*int(y)
print(part2)