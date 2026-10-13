class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:


        n = len(nums)
        
        squares = [x * x for x in nums]
        
        squares.sort()
        
        minus_count = n // 2
        
        smallest_half_sum = sum(squares[:minus_count])
        largest_half_sum = sum(squares[minus_count:])
        
        return largest_half_sum - smallest_half_sum
        