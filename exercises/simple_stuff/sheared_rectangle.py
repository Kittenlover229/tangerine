from math import floor, ceil, pi, tan

A = float(input())
B = float(input())
a = float(input())

B = floor(B)

total = 0
for y in range(-B, B+1):
    q1 = y / tan(a*pi/180) + A
    q2 = y / tan(a*pi/180) - A
    total += floor(max(q2, q1)) - ceil(min(q2, q1))
    total += 1

print(total)
