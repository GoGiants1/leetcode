class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        mx = mn = prices[0]
        out = 0
        for i in range(1, n):
            if prices[i] < mn:
                mn = mx = prices[i]
            
            if prices[i] > mx:
                mx = prices[i]
            out = max(mx - mn, out)
            
        return out

        