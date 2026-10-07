from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        # Helper function to check if a string has valid parentheses
        def isValid(string: str) -> bool:
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        # If the string is already valid, return it immediately
        if isValid(s):
            return [s]

        queue = deque([s])
        visited = {s}
        found = False
        result = []

        while queue and not found:
            # Process all nodes at the current BFS level
            level_size = len(queue)

            for _ in range(level_size):
                current = queue.popleft()

                if isValid(current):
                    result.append(current)
                    found = True # Signal that the minimum removal level is reached
                
                # If a valid string has already been found, stop generating deeper states
                if found:
                    continue

                # Generate next states by removing one parenthesis at a time
                for i in range(len(current)):
                    if current[i] not in ('(', ')'):
                        continue # Skip letters
                    
                    # Create a new string missing the character at index i
                    next_state = current[:i] + current[i+1:]
                    
                    if next_state not in visited:
                        visited.add(next_state)
                        queue.append(next_state)

        return result
