some_cool_list = list(map(int, input().split()))

output_list = []

# Just random operations with the list lol :P
while len(some_cool_list) != 0:
    output_list.append(some_cool_list.pop())
    if len(some_cool_list) != 0:
        output_list.append(some_cool_list.pop())
    output_list.reverse()
    some_cool_list.reverse()

for number in output_list:
    print(number, end=' ')
print()
