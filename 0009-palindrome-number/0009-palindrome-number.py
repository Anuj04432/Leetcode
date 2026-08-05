class Solution:
    def isPalindrome(self, x: int) -> bool:
        # original = x
        # rev = 0
        # if x<0:
        #     return False
        # else:
        #     while x>0:
        #         d = x%10
        #         rev = rev*10+d
        #         x = x//10
        # return original == rev

        a = str(x)
        if a == a[::-1]:
            return True
        else:
            return False