class Solution:
    def isSorted(self,arr,n):
        #code here
        count1=0
        count2=0
        for i in range(1,n):
            if arr[i-1]<arr[i]:
                count1+=1
            elif arr[i-1]==arr[i]:
                count1+=1
            if arr[i-1]>=arr[i]:
                count2+=1
            elif arr[i-1]==arr[i]:
                count2+=1
        if count1==n-1:
            return 1
        if count2==n-1:
            return 1
        return 0

n=int(input())
arr=[int(x) for x in input().split()]

print(Solution().isSorted(arr,n))
