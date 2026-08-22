class Solution(object):
    def checkDivisibility(self, n):
        s = str(n)
        add = 0
        mul = 1
        for i in s:
            add += int(i)
            mul *= int(i)
        total = add+mul
        return n%total ==0
        
        