class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pop_idx = 0
        for i, v in enumerate(pushed):
            if v == popped[pop_idx]:
                stack.append(v)
                while stack and stack[-1] == popped[pop_idx]:
                    v = stack.pop()
                    pop_idx += 1
            else:
                stack.append(v)
        
        return len(stack) == 0