def sieve(n):
    if n<=1:
        return
    isPrime=[True]*(n+1)
    i=2
    while i<=n:
        if isPrime[i]:
            print(i, end=" ")
            for j in range(i*i,n+1,i):
                isPrime[j]=False
        i+=1


n=int(input("Enter the number: "))
sieve(n)