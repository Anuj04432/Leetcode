class Solution:
    def countCommas(self, n: int) -> int:
        comma = 0
        value = 1000
        while n>=value:
            comma += (n-value+1)
            value*=1000

        return comma

