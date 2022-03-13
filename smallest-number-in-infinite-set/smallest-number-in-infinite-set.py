class SmallestInfiniteSet:
    
    def __init__(self):
        self.h = set()
        

    def popSmallest(self) -> int:
        i = 1
        while i in self.h:
            i +=1
        self.h.add(i)
        return i

    def addBack(self, num: int) -> None:
        if num in self.h:
            self.h.remove(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)