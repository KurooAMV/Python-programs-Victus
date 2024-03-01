import math
class Solution:
    def R(self,a,b):
        return b/a
    def Nth(self,a,r,n):
        return a*(r**(n-1))
    def termOfGP(self,a,b,n):
        r=self.R(a,b)
        an=self.Nth(a,r,n)
        return an

AB=[int(x) for x in input().strip().split()]
A=AB[0]
B=AB[1]

N=int(input())
ob=Solution()
print(math.floor(ob.termOfGP(A,B,N)))