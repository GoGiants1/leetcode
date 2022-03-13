class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        import heapq as hq
        now = []
        future = []
        for i, p in enumerate(profits):
            c = capital[i]
            if w >= c:
                hq.heappush(now, (-p, c))
            else:
                hq.heappush(future, (c, p))

        while now and k:
            price, _ = hq.heappop(now)
            w -= price
            k -= 1
            while future and future[0][0] <= w:
                hq.heappush(now, (-future[0][1], future[0][0]))
                hq.heappop(future)
        
        return w