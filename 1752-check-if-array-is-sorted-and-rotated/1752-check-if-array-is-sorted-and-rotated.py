class Solution:
    def check(self, nums: list[int]) -> bool:
        d = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                d += 1

            if d > 1:
                return False
        return True