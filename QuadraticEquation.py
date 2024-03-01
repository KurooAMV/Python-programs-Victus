import math

class Solution:
    def discriminant(self, a, b, c):
        return (b**2) - (4 * a * c)

    def quadraticRoots(self, a, b, c):
        D = self.discriminant(a, b, c)
        if D < 0:
            return [-1]
        root1 = math.floor((-(b) + math.sqrt(D)) / (2 * a))
        root2 = math.floor((-(b) - math.sqrt(D)) / (2 * a))
        #return [int(root1), int(root2)] if root1 <= root2 else [int(root2), int(root1)]
        if root1<0 and root2<0:
            r=(min(-root1,-root2))
            s=(max(-root1,-root2))
            return [int(-s),int(-r)]
        elif root1<=root2:
            return [int(root2),int(root1)]
        else:
            return [int(root1),int(root2)]

# Uncomment the following lines to take input from the user
# a, b, c = map(int, input().strip().split())
# ob = Solution()
# ans = ob.quadraticRoots(a, b, c)

# For the given example input:
abc=[int(x) for x in input().strip().split()]
a = abc[0]
b = abc[1]
c = abc[2]
ob = Solution()
ans = ob.quadraticRoots(a, b, c)

if ans[0] == -1:
    print("Imaginary")
else:
    for i in ans:
        print(i, end=" ")
    print()


