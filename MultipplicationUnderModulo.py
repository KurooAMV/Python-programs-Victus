class Solution:
    def multiplicationUnderModulo(self,a,b):
        '''
        :param a: given value of a
        :param b: given value of b
        :return: Integer , sum under modulo
        '''  
        p=a%(10**9+7)
        q=b%(10**9+7)
        res=(a+a*(b-1))%(10**9+7)
        return res

a,b = map(int,input().strip().split())
ob=Solution()
print(ob.multiplicationUnderModulo(a,b))

