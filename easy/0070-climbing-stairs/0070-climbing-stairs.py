class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        table = [1, 2]

        for i in range(2,n):
            table.append(table[i-2] + table[i-1])
        return table[-1]