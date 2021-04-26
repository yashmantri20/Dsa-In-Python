# Best time to buy and Sell stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if min_val > prices[i]:
                min_val = prices[i]
            else:
                p = prices[i] - min_val
                if profit > p:
                    profit = profit
                else:
                    profit = p
        return profit
                