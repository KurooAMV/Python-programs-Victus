def reverseArray(arr,n):
    a=[]
    a.extend(arr)
    arr.clear()
    for i in range(1,n+1):
        arr.append(a[n-i])
    return arr

n=int(input())
arr=[int(x) for x in input().split()]
reverseArray(arr,n)
for e in arr:
    print(e,end=' ')
