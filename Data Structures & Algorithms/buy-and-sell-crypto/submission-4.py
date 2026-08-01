class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        j = 0
        maxprofit = 0
        while j != len(prices):
            for i in range(j, len(prices)):
                profit = prices[i] - prices[j]
                if profit > 0:
                    if profit > maxprofit:
                        maxprofit = profit
                       
            j += 1
        return maxprofit
        