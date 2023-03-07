from collections import defaultdict

string = input()
accumulator = defaultdict(lambda: 0)

for ch in string:
    accumulator[ch] += 1

for k, v in accumulator.items():
    print(k, v)
