def is_prime(a):
    if a <2:
        return False
    i=2
    while i*i<=a:
        if a%i==0:
            return False
        i+=1
    return True

def divides(a, factors):
    while a != 1:
        for i in range(2, a + 1):
            if a % i == 0 and is_prime(i):
                a = a // i
                factors.append(i)
                break
    return True

def show_factors(fact):
    for i in fact:
        print(i)

num = int(input("Enter the number: "))
fact = [1]
if divides(num, fact):
    print("The factors of", num, "are:")
    if num not in fact:
        fact.append(num)
    show_factors(fact)

