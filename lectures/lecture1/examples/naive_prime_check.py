n = int(input())

divisors = 0
for i in range(1, n + 1):
    if n % i == 0:
        divisors = divisors + 1

if divisors == 2:
    print("It is prime! Only divisible by itself and 1")
else:
    print(f"Nope, not prime, it has {divisors} divisors")
