h = int(input())
pm = h >= 12

print((h - 1) % 12 + 1, end="")
if pm:
    print("pm")
else:
    print("am")
