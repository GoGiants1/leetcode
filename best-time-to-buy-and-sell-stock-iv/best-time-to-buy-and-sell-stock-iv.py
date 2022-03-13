class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if not prices or k==0:
            return 0

        if 2*k > n:
            res = 0
            for i, j in zip(prices[1:], prices[:-1]):
                res += max(0, i - j)
            return res
        
        t_cost = [float('inf') for _ in range(k)]       
        t_profit = [0 for _ in range(k)]

        for price in prices:
            for j in range(k):
                if not j:
                    t_cost[j] = min(t_cost[j], price)
                    t_profit[j] = max(t_profit[j], price - t_cost[j] )
                else:    
                    t_cost[j] = min(t_cost[j], price - t_profit[j-1])
                    t_profit[j] = max(t_profit[j], price - t_cost[j])

        return t_profit[-1]        