class TimeMap:
    
    def __init__(self):
        self.d = defaultdict(list)
        self.time = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append(value)
        self.time[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        from bisect import bisect_right
        if len(self.d[key]):
            idx = bisect_right(self.time[key], timestamp)
            if idx == 0:
                return ""
            return self.d[key][idx-1]
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)