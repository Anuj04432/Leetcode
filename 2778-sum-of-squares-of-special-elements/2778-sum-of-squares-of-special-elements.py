class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        one_indexed_dict = {i: item for i, item in enumerate(nums, start=1)}
        for i in one_indexed_dict:
            if n % i == 0:
                result += one_indexed_dict[i]*one_indexed_dict[i]

        return result

        