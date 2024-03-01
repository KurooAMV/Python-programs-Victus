def lcm(a,b):
    r=max(a,b)
    while True:
        if r%a==0 & r%b==0:
            return r
        r+=1
    return r

a=int(input("Enter a: "))
b=int(input("Enter b: "))
print(lcm(a,b)) 