class Solution:
    def longestPalindrome(self, s: str) -> str:
        temp = ""
        for i in range(len(s)):
            a = ""
            for j in range(i,len(s)):
                a+=s[j]
                if a == a[::-1]:
                    if len(a)>len(temp):
                        temp = a
        return temp