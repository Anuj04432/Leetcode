class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        answer = []
        depth = 0
        
        for char in seq:
            if char == '(':
                # Allocate to group 0 if current depth is even, group 1 if odd
                answer.append(depth % 2)
                depth += 1
            else:
                depth -= 1
                # Allocate to group 0 if new depth is even, group 1 if odd
                answer.append(depth % 2)
                
        return answer