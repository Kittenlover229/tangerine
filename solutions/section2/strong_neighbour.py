some_cool_list = list(map(int, input().split()))

for i in range(len(some_cool_list) - 2):
    print(max(some_cool_list[i], some_cool_list[i + 1], some_cool_list[i + 2]), end=' ')
print()
