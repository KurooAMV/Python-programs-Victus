def Factorial1(n):
   fact=1
   for i in range(2,n+1):
      fact=fact*i
   return fact

def Factorial2(n):
   if n==0:
      return 1
   return n*Factorial2(n-1)

n=int(input("Enter the number: "))
print(f"The factorial of {n} is {Factorial2(n)}.")