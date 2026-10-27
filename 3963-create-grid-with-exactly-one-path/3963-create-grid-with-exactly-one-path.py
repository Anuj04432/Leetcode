class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [['#' for _ in range(n)] for _ in range(m)]

        # Fill the first row with '.'
        for j in range(n):
            grid[0][j] = '.'

        # Fill the last column with '.'
        for i in range(m):
            grid[i][n - 1] = '.'

        return [''.join(row) for row in grid]