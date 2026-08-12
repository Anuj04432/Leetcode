class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        new_string = []
        max_length = 0
        for char in s:
            if char in new_string:
                while char in new_string:
                    new_string.pop(0)
            new_string.append(char)
            max_length = max(max_length,len(new_string))
        
        return max_length