class Solution:
    def countCommas(self, n: int) -> int:
        comma = 0
        threshold = 1000
        while threshold <= n:
            comma += n-threshold+1
            threshold *= 1000
        return comma
