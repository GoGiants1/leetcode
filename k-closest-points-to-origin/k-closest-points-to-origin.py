class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        from heapq import heappush, heappop

        pq = []

        for i, (x, y) in enumerate(points):
            heappush(pq, (-(x**2 + y **2), x, y))
            while len(pq) > k:
                heappop(pq)
        
        return [[a, b] for _, a, b in pq]
