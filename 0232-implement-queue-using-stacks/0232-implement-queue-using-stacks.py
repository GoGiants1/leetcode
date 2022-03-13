class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []
        

    def push(self, x: int) -> None:
        if len(self.out_stack) > 0:
            # 만약 In stack에 있으면 out으로 먼저 다 옮기기
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
            while self.out_stack:
                self.in_stack.append(self.out_stack.pop())
        
        self.in_stack.append(x)

    def pop(self) -> int:
        if len(self.in_stack) > 0:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        
        return self.out_stack.pop()

    def peek(self) -> int:
        if len(self.in_stack):
            return self.in_stack[0]
        else:
            return self.out_stack[-1]

    def empty(self) -> bool:
        if len(self.in_stack) + len(self.out_stack) == 0:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()