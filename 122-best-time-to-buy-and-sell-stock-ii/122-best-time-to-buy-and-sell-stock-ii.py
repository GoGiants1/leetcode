class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        for i, p in enumerate(prices):
            if i > 0 and p > prices[i - 1]:
                profit += p - prices[i - 1]
        return profit