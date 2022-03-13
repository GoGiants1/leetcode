import heapq as hq
class MinStack:
    def __init__(self):
        # (val, min)
        self.st = []

    def push(self, val: int) -> None:
        # 삽입
        if self.st:
            self.st.append((val, min(self.st[-1][1], val)))
        else:
            self.st.append((val, val))
    
    def pop(self) -> None:
        # 가장 최근꺼 삭제
        v = self.st.pop()
        
    def top(self) -> int:
        # 가장 최근꺼 리턴
        return self.st[-1][0]
    def getMin(self) -> int:
        return self.st[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()