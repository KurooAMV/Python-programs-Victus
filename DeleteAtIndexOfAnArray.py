def deleteFromArray(arr,n,idx):
    #code here
    
    for i in range(idx,n):
        if i-1==idx:
            arr[idx]=arr[i]
        elif i>idx:
            arr[i-1]=arr[i]
    arr[n-1]=0
n=int(input())
idx=int(input())

arr=[i+1 for i in range(n)]

deleteFromArray(arr,n,idx)

for e in arr:
    print(e,end=' ')
print()
                       