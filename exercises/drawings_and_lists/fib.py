n = int(input())

F_prev = 0
F_last = 1
print(F_prev)

for i in range(n):
    F_prev, F_last = (F_last, F_last + F_prev)
    print(F_prev)
