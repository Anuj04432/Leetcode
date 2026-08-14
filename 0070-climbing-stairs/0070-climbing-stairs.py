class Solution:
    def climbStairs(self, n: int) -> int:
        first = 0 
        second = 1
        total = 0
        for i in range(n):
            total = first + second
            first = second
            second = total
        return total
        