class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        # # dp(i) = max(dp(i-1) + prices[i] - fee, dp(i)
        # n = len(prices)

        # dp = [[-math.inf, -math.inf] for _ in range(n)]

        # # hold, not hold
        # dp[0][0] = -prices[0]
        # dp[0][1] = 0

        # for i in range(1, n):
        #     dp[i][0] = max(dp[i-1][1] - prices[i], dp[i-1][0])
        #     dp[i][1] = max(dp[i-1][0] + prices[i] - fee, dp[i-1][1])
        
        
        # return max(dp[-1])

        # Space optimized
        n = len(prices)
        hold, free = -prices[0], 0
        
        for i in range(1, n):
            tmp = hold
            hold = max(hold, free - prices[i])
            free = max(free, tmp + prices[i] - fee)
        
        return free