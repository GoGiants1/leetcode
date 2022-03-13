class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        @cache
        def dfs(amt: int):
            if amt < 0:
                return -1
            if amt == 0:
                return 0
            min_cost = math.inf
            for c in coins:
                out = dfs(amt - c)
                if out != -1:
                    min_cost = min(min_cost, out + 1)
            return min_cost if min_cost != math.inf else -1

        return dfs(amount)
