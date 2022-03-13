class Logger:

    def __init__(self):
        self.hash_map = {}
    def updateHashMap(self, t: int, m: str)-> bool:
        self.hash_map[m] = t
        return True
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        prev_t = self.hash_map.get(message)
        if prev_t is None or prev_t + 10 <= timestamp:
            return self.updateHashMap(timestamp,message)
        
        return False
            

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)