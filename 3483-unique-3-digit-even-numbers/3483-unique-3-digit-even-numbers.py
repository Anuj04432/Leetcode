class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        # A dictionary/hash map acts as a set to track unique formed numbers 
        # without needing to import any library
        unique_even_numbers = {}
        n = len(digits)
        
        # Loop 1: Pick the hundreds digit (i)
        for i in range(n):
            if digits[i] == 0:  # No leading zeros
                continue
                
            # Loop 2: Pick the tens digit (j)
            for j in range(n):
                if i == j:  # Can't reuse the same element index
                    continue
                    
                # Loop 3: Pick the units digit (k)
                for k in range(n):
                    if i == k or j == k:  # Can't reuse the same element index
                        continue
                        
                    # Must be even
                    if digits[k] % 2 == 0:
                        num = digits[i] * 100 + digits[j] * 10 + digits[k]
                        # Store in dict to automatically handle duplicate values
                        unique_even_numbers[num] = True
                        
        return len(unique_even_numbers)
