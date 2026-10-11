class Solution(object):
    def maxProfit(self, prices):
       n = len(prices)
       min_buy = prices[0]
       max_profit = 0
       for i in range(1,n):
         if min_buy > prices[i]:
            min_buy = prices[i]
         else:
            profit = prices[i] - min_buy 
            max_profit = max(profit , max_profit)
       return max_profit