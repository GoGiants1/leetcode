class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        hm = {}
        
        def dp(i: int, buying: bool) -> int:
            if i >= len(prices):
                return 0
            
            if (i, buying) in hm:
                return hm[(i,buying)]
            
            cooldown = dp(i+1, buying)
            
            if buying:
                buy = dp(i+1, not buying) - prices[i]
                hm[(i, buying)] = max(cooldown, buy)
            else:
                sell = dp(i+2, not buying) + prices[i]
                hm[(i, buying)] = max(cooldown, sell)
            
            return hm[(i,buying)]
        
        return dp(0, True)

        # sell, buy, rest = 0, -prices[0], 0
        # for price in prices:
        #     buy, sell, rest = max(rest - price, buy), max(buy + price, sell), sell
        # return sell