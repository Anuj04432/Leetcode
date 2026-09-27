from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        counts = Counter(arr1)
        result = []
        for num in arr2:
            if num in counts:
                result.extend([num] * counts[num])
                del counts[num]
        leftovers = sorted(counts.elements())
        result.extend(leftovers)
        
        return result