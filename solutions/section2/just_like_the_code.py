some_cool_list = input().split()

print('[', end='')
for i in range(len(some_cool_list) - 1):
    word = some_cool_list[i]
    print('"', word, '", ', end=' ', sep="")
print('"', some_cool_list[-1], '"]', sep="")
