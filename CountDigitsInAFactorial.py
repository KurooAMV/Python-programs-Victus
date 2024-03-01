def factorial(n):
    fact=1
    for i in range(1, n+1):
        fact=fact*i
    return fact

def CountDigits(n):
    flag=0
    while n>0:
        n=n//10
        flag+=1
    return flag

def digitsInFactorial(n):
    if n>0:
        if n in range(0,4):
            return 1
        else:
            
            while n>1:
                fact= n*digitsInFactorial(n-1)
                return fact

n=int(input("Enter the number: "))
print(CountDigits(factorial(n)))
#print(digitsInFactorial(n))