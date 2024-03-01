from math import sqrt
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def exactly3Divisors(a):
    count = 0
    for i in range(2, int(sqrt(a)) + 1):
        if is_prime(i) and i*i <= a:
            count += 1
    return count

num = int(input("Enter the number: "))
print(exactly3Divisors(num))
