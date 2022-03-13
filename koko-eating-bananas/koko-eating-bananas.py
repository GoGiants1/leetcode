class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        lo, hi = 1, max(piles)
        if len(piles) == 1:
            return math.ceil(piles[0] / h)
        
        while lo < hi:
            mid = (lo + hi) // 2
            hr = 0
            for p in piles:
                hr += math.ceil(p/mid)

            if hr <= h:
                hi = mid
            else:
                lo = mid + 1
        return hi
            