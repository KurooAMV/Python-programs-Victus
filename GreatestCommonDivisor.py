def gcd1(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a
def gcd2(a,b):
    if b==0:
        return a
    else: 
        return gcd2(b,a%b)
a=int(input("Enter a: "))
b=int(input("Enter b: "))
print(f"The GCD of {a} and {b} is {gcd2(a,b)}.")