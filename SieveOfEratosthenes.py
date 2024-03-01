#O(n*(n^(1/2)))
def check_prime(a):
    if a<2:
        return False
    i=2
    while i*i<=a:
        if a%i==0:
            return False
        i+=1
    return True

def is_prime(a):
    if a!=2 and a!=3 and a!=5:
        if a%2==0 or a%3==0 or a%5==0:
            return False
        else:
            return True
    else:
        return True

num=int(input("Enter a number: "))
for i in range(2,num+1):
    if is_prime(i):
        print(i)

#O(sqrt(n))
