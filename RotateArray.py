class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,A,D,N):
        #Your code here
        '''temp=[]
        for i in range(1,N+1):
            if i < D:
                temp.append(A[i])
            elif i > D :
                A[i-D]=A[i]
        A.extend(temp)
        return A'''
        k = A.index(D)
        new_lis = []
        new_lis = A[k+1:]+A[0:k+1]
        return new_lis

nd=[int(x) for x in input().strip().split()]
N=nd[0]
D=nd[1]
A=[int(x) for x in input().strip().split()]
ob=Solution()
ob.rotateArr(A,D,N)

for i in A:
    print(i,end=" ")

print()

