import re
from collections import defaultdict

with open('5.in') as f:
    data = f.readlines()
    data = [re.findall(r'\d+', line) for line in data]
    page_ordering, updates = data[:data.index([])], data[data.index([])+1:]

order = defaultdict(list)
for page in page_ordering:
    order[page[0]].append(page[1])

def insertionsort(arr):
    arr = arr.copy()

    for i in range(len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key in order[arr[j]]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

ans = 0
for update in updates:
    for i, j in enumerate(update[:-1]):
        if update[i+1] not in order[j]:
            break
    else:
        ans += int(update[len(update)//2])
print(ans)

ans = 0
for update in updates:
    sorted_order = insertionsort(update)[::-1]

    if update != sorted_order:
        ans += int(sorted_order[len(sorted_order)//2])
print(ans)