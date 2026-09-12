class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # output = []
        # for i in range(1,n+1):
        #     if i not in nums:
        #         output.append(i)

        # return output
        for n in nums:
            i = abs(n)-1
            if nums[i] > 0:
                nums[i] = -nums[i]

        return [i + 1 for i, num in enumerate(nums) if num > 0]
