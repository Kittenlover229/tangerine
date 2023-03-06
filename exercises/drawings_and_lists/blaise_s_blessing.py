# Implementation One: The Simple One

n = int(input())
prev_row = [1]

if n >= 1:
    print(1)

for row_number in range(2, n + 1):
    accumulator = []
    accumulator.append(prev_row[0])
    for i in range(len(prev_row) - 1):
        accumulator.append(prev_row[i] + prev_row[i + 1])
    accumulator.append(prev_row[-1])

    for number in accumulator:
        print(number, end=' ')
    print()

    prev_row = accumulator
