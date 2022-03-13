class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        # state variable : cost, cut order, stick
        # recurrence relation
        # cut(cuted)
        cache = {}
        cuts_set = set(cuts)
        cuts.sort()
        def dp(l: int, r: int) -> int:
            if (l, r) in cache:
                return cache[(l, r)]
            if l == r:
                return 0
            cost = r - l
            min_cost = math.inf
            cuts_idx = bisect_left(cuts, l+1)
            while cuts_idx < len(cuts) and cuts[cuts_idx] < r:
                min_cost = min(min_cost, dp(l, cuts[cuts_idx]) + dp(cuts[cuts_idx], r) + cost)
                cuts_idx += 1
            if min_cost is not math.inf:
                cache[(l,r)] = min_cost
            else:
                cache[(l,r)] = 0
            return cache[(l,r)]
        return dp(0,n)