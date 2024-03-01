n=int(input("Enter the number: "))
f=n
flag=0
while n>0:
    n= n//10
    flag+=1
print(f"The number of digits in number {f} is {flag}.")