from math import sqrt
def isPrime(a):
    if a==1:
        return False
    flag=0
    for i in range(2,a):
        if a%i==0:
            flag+=1
    if flag!=0:
        return False
    else: 
        return True
    
def is_prime(a):
    if a <2:
        return False
    i=2
    while i*i<=a:
        if a%i==0:
            return False
        i+=1
    return True

#The below function fails when multiple recursion are to be used and also take too long to calculate for prime
#It is better to use the function is_prime(a)
def Prime(a,itr):
    if itr==1 or a==2:
        return True
    if a%itr==0:
        return False
    if Prime(a,itr-1)==False:
        return False
    return True

a=int(input("Enter the number: "))
#itr=int(sqrt(a)+1)
#print(isPrime(a))
#print(Prime(a,itr))
print(is_prime(a))