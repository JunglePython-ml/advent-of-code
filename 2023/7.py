from collections import Counter

with open("7.in") as f:
    lines = f.readlines()
    lines = [(a, int(b)) for a, b in [line.strip().split() for line in lines]]

def get_rank(hand, part=1):
    CARDS = "AKQJT98765432"
    if part == 2:
        CARDS = "AKQT98765432J"
        if hand == "J" * 5:
            return ([5], [0] * 5)
    based_counts = [13 - CARDS.index(x) for x in hand]
    most_common = Counter(hand).most_common(5)
    if part == 2:
        if most_common[0][0] == "J":
            hand = hand.replace("J", most_common[1][0])
        else:
            hand = hand.replace("J", most_common[0][0])
        most_common = Counter(hand).most_common(5)
    counts = [x[1] for x in most_common]
    return (counts, based_counts)

for i in range(1,3):
    lines = sorted(lines, key=lambda x: get_rank(x[0], i))
    total = 0
    for i, (hand, bid) in enumerate(lines):
        total += bid * (i + 1)
    print(total)