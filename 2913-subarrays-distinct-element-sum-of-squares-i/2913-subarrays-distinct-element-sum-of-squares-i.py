class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0
        MOD = 10**9 + 7  # Often required for large outputs in these problems
        
        # Iterate over all possible starting positions of subarrays
        for i in range(n):
            distinct_elements = set()
            # Extend the subarray from index i to the end of the array
            for j in range(i, n):
                distinct_elements.add(nums[j])
                # Add the square of the distinct element count
                distinct_cnt = len(distinct_elements)
                total_sum += distinct_cnt * distinct_cnt
                
        return total_sum % MOD