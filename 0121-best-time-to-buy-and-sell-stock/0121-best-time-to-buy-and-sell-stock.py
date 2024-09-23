#objective: use the array given to find the best time to buy and sell stock(cannot sell before you buy), then return max profit
    # prices = [7,1,5,3,6,4]; best time to buy is i = 1 and sell is i = 4, maxprofit = 6-1 = 5

# min needs to be highest possible value to make sure that the first array value is set to min
# iterate through the prices array and compare min to current price to make sure you have the lowest price possible set to min and in turn the max profit
# in the same loop calculate the profit from the min price to the current price you are looking at and decide whether that is greater than the max profit
#                                    if it is greater than maxprofit than set that to maxprofit
# return maxprofit
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
        
