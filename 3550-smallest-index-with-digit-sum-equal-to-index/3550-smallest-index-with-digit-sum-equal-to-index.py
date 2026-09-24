class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        i = 0
        index = -1
        while i < len(nums):
            a = sum([int(j) for j in str(nums[i])])
            if a == i:
                index = i
                break
            i+=1
        return index