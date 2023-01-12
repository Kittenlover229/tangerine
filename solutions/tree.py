h = int(input())

for i in range(h):
    if i % 2 == 0:
        ch = "e"
    else:
        ch = "a"
    print(ch * (i + 1))
print(ch)
