class Solution:
    def immediateSmaller(self, arr, n, x):
        ai = -1  # Initialize ai to -1
        dist = float('inf')  # Initialize dist to positive infinity

        for num in arr:
            if num < x:
                current_dist = x - num
                if current_dist < dist:
                    dist = current_dist
                    ai = num

        return ai

# Example usage
n = int(input())
arr = [int(e) for e in input().split()]
x = int(input())
ob = Solution()
ans = ob.immediateSmaller(arr, n, x)
print(ans)
