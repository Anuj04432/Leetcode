class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum < 1 or sum > num * 9:
            return ""

        ans = ""

        for i in range(num):
            if sum >= 9:
                ans += "9"
                sum -= 9
            elif sum > 0:
                ans += str(sum)
                sum = 0
            else:
                ans += "0"

        return ans