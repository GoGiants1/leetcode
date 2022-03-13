class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq as hq
        h = []
        for i, v in enumerate(stones):
            hq.heappush(h, -v)

        while len(h) > 1:
            if h[0] == h[1]:
                hq.heappop(h)
                hq.heappop(h)
            else:
                a, b = hq.heappop(h), hq.heappop(h)
                hq.heappush(h, a-b)
    
        return -h[0] if h else 0