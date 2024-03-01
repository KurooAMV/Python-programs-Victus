class Solution:
    ##Complete this function
    def searchInSorted(self,arr, N, K):
        #Your code here
        low=0
        high=N-1
        if low<=high:
            mid=(low+high)//2
            if arr[mid]==K:
                return self.searchInSorted(arr[:mid-1],mid-1,K)
            elif arr[mid]>K:
                return self.searchInSorted(arr[mid+1:],high,K)
        else:
            return -1
        
        


NK = input().strip().split()
N = int(NK[0])
K = int(NK[1])
A = [ int(x) for x in input().strip().split() ]
ob=Solution()
print(ob.searchInSorted(A,N,K))
