class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        i , j = 0, 0 

        while len(t) > j:
            if s[i] == t[j]:
                i+=1
                if i == len(s):
                    return True

            j+=1

        return i == len(s)


