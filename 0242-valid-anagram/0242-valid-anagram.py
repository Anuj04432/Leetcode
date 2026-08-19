class Solution(object):
    def isAnagram(self, s, t):
        char = {}

        for ch in s:
            char[ch] = char.get(ch,0) + 1

        for ch in t:
            char[ch] = char.get(ch,0) - 1

        for character in char.values():
            if character != 0:
               return False

        return True
        