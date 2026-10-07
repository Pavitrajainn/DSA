class Solution:
    def maxProfit(self, prices: list[int]) -> int:
     n = len(prices)
     min_per = prices[0]
     max_profit = 0
     for i in range(1,n):
        if min_per > prices[i] :
            min_per = prices[i]
        else:
            max_profit += prices[i] - min_per            
            min_per = prices[i]
     return max_profit