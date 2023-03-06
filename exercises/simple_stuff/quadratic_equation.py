a = int(input())
b = int(input())
c = int(input())

d = b**2 - 4 * a * c
if d < 0:
    print("NaN")
elif d == 0:
    print(-b / (2 * a))
else:
    print((-b + d**0.5) / (2 * a))
    print((-b - d**0.5) / (2 * a))
