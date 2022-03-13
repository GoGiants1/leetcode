class MedianFinder:
    from bisect import bisect_left
    from heapq import heappush, heappop
    def __init__(self):
        self.cnt = 0
        self.lo = []
        self.hi = []


    def addNum(self, num: int) -> None:
        heappush(self.lo, -num)
        heappush(self.hi, -heappop(self.lo))

        if len(self.lo) < len(self.hi):
            heappush(self.lo, -heappop(self.hi))

    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        else:
            return (-self.lo[0] + self.hi[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()