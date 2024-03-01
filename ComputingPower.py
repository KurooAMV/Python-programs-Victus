#To decrease the value of time complexity we need to apply a recursion theorem in the algotrithm
#See the wxample of power and pwer2 functions
#Power2 function is more effective on large value then the Power function 
def power1(n,m):
    res=1
    for i in range(m):
        res=res*n
    return res

def power2(n,m):
    if m==0:
        return 1
    if m%2==0:
        temp=power2(n,m//2)
        return temp*temp
    else:
        return n*power2(n,m-1)


n=int(input("Enter the base value: "))
m=int(input("Enter the power value: "))
#print(power2(n,m))
print(power1(n,m))
