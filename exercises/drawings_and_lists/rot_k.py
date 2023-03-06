k = int(input())
some_cool_list = list(map(int, input().split()))

# Since rotating the list by any number K and K + length is effectively 
# the same. This also guarantees that k < length, which in turn
# guarantees no index-out-of-bounds errors. Note the special behaviour when
# dividing a negative number like this, the result is actually POSITIVE and 
# equal to length - |k| % length. This is actually desired behaviour for
# our usecase, since shifting a list of 4 to by -1 is the same as shifting 
# it by 3. A very powerful line.
k = k % len(some_cool_list)

for _ in range(k):
    # remove last element
    # put it as the first
    some_cool_list.insert(0, some_cool_list.pop())
    # do that k times

for number in some_cool_list:
    print(number, end=' ')
print()
