class Solution:
    def sumUnderModulo(self,a,b):
        # code here
        a=a%(10**9 +7)
        b=b%(10**9 +7)
        rem=(a+b)%(10**9+7)
        return rem
    
a,b = map(int,input().strip().split())
ob=Solution()
print(ob.sumUnderModulo(a,b))   