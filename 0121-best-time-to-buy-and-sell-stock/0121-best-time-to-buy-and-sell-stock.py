class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        max_profit = 0
        min_price = prices[0]
        for i in range (1,n):
          if prices[i] < min_price:
            min_price = prices[i]
          else:
             total = prices[i] - min_price
             if total > max_profit:
                 max_profit = total
        return max_profit 