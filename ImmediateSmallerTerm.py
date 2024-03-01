class Solution:
    
    def immediateSmaller(self,arr,n,x):
        #return required ans
        dist=x
        ai=0
        if x==0 or x==1:
            return -1
        #code here
        for i in  range(0,n):
            '''if x-arr[i]<0:
                dist=min(-(x-arr[i]),dist)
                ai=arr[i]
            else:
                dist=min((x-arr[i]),dist)
                ai=arr[i]'''
            if arr[i]<x:
                dist=min(abs(x-arr[i]),dist)
                ai=max(ai,arr[i])
            
        return ai
#5
#4759 5769 8009 9811 4234
#4769
n=int(input())
arr=[int(e) for e in input().split()]
x=int(input())
ob=Solution()
ans=ob.immediateSmaller(arr,n,x)
print(ans)