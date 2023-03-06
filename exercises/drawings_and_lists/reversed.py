some_list = list(map(int, input().split()))

for i in range((len(some_list) - 1) // 2):
    some_list[len(some_list)-i - 1], some_list[i] = some_list[i], some_list[len(some_list)-i - 1]

print(some_list)
