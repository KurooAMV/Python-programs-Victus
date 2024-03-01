def power3(x,n):
    res=1
    while n>0:
        if n%2!=0:
            res=res*x
        x=x*x
        n=n//2
    return res

x=int(input("Enter the value x: "))
n=int(input("Enter the value n: "))
print(power3(x,n))