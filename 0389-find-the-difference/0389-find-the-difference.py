class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Calculate the sum of ASCII values for both strings
        sum_s = sum(ord(c) for c in s)
        sum_t = sum(ord(c) for c in t)
        
        # The difference between the sums corresponds to the extra character
        return chr(sum_t - sum_s)