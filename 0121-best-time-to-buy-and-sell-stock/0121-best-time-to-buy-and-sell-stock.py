class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        import sys
        min = float('inf')
        maxProfit = 0

        for price in prices:
            if(price < min):
                min = price
            profit = price - min
            if(profit > maxProfit):
                maxProfit = profit
        return maxProfit
        