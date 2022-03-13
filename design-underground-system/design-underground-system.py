class UndergroundSystem:

    def __init__(self):
        # key: (start, end)
        self.d = defaultdict(list)
        self.travel = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.travel[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_name, start_time = self.travel[id]
        if (start_name, stationName) in self.d:
            self.d[(start_name, stationName)][0] += t - start_time
            self.d[(start_name, stationName)][1] += 1
        else:
            self.d[(start_name, stationName)] = [t - start_time, 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        acc_time ,ppl = self.d[(startStation, endStation)]
        return acc_time / ppl


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)