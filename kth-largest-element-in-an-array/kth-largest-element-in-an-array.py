class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq as hq
        h = []
        for i, v in enumerate(nums):
            hq.heappush(h, v)

            while len(h) > k:
                hq.heappop(h)
        
        return h[0]