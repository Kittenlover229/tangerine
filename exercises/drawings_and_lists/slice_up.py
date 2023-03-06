L = int(input())
S = list(map(int, input().split()))

index = None
for i, l in enumerate(S):
    if L == l:
        index = i

first_part = []
for i in range(0, index):
    first_part.append(S[i])

second_part = []
for i in range(index + 1, len(S)):
    second_part.append(S[i])

for number in first_part:
    print(number, end=' ')
print()

for number in second_part:
    print(number, end=' ')
print()
