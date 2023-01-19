p = int(input())
numbers = list(map(int, input().split()))

for _ in range(p):
    print(" ".join(map(str, numbers)))
    ls = []
    for i in range(len(numbers) - 1):
        a, b = numbers[i], numbers[i + 1]
        if abs(a) > abs(b):
            ls.append(a)
        else:
            ls.append(b)
    numbers = ls
