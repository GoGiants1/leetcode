import heapq as hq
class StockPrice:
    # from collections import defaultdict
    def __init__(self):
        # HashMap key: timestamp, value: price
        # min price field
        # max price field
        # latest price filed
        self.latest_time = None
        self.max_hq = []
        self.min_hq = []
        self.book = {}
        
    def update(self, timestamp: int, price: int) -> None:
        if self.latest_time is None or self.latest_time < timestamp:
            self.latest_time = timestamp
        self.book[timestamp] = price
        hq.heappush(self.min_hq, (price, timestamp))
        hq.heappush(self.max_hq, (-price, timestamp))
        
    def current(self) -> int:
        return self.book[self.latest_time]

    def maximum(self) -> int:
        p, t = self.max_hq[0]
        
        while -p != self.book[t]:
            hq.heappop(self.max_hq)
            p, t = self.max_hq[0]
        return -p

    def minimum(self) -> int:
        p, t = self.min_hq[0]

        while p != self.book[t]:
            hq.heappop(self.min_hq)
            p, t = self.min_hq[0]

        return p

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()