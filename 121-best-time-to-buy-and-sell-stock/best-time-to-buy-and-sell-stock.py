class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy_price = prices[0]
        sell_price = prices[0]

        out = 0
        for p in prices:
            buy_price = min(buy_price, p)
            if buy_price == p:
                sell_price = p
                continue
            else:
                sell_price = max(sell_price, p)
            out = max(out, sell_price - buy_price)

        return out