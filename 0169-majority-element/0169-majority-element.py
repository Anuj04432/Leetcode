class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        dic = {}
        for i in range(n):
            if nums[i] in dic:
                dic[nums[i]]+=1
            else:
                dic[nums[i]] = 1

        max_value= max(dic.values())
        for key,value in dic.items():
            if value == max_value and max_value>(n/2):
                return key