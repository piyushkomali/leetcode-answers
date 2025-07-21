class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxVal = 0
        def visit(i, j, number):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != 1:
                return number
            grid[i][j] = 0
            number +=1
            n = visit(i, j+1, number)
            n = visit(i+1, j, n)
            n = visit(i, j-1, n)
            n = visit(i-1, j, n)
            return n

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    val = visit(i,j,0)
                    maxVal = max(maxVal, val)
        return maxVal
        