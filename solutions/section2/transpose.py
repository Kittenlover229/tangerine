first_row = list(map(int, input().split()))
matrix = []
matrix.append(first_row)

# Since we know that this is an NxN matrix columns are equal to rows
N = len(first_row)
for i in range(N - 1):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(N - 1):
    for j in range(1, N):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for row in matrix:
    for number in row:
        print(number, end=' ')
    print()
print()
