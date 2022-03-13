# import numpy as np
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        """
            grid의 column 개수로 k를 나눈 나머지를 shift하기. <-- 이거는 맨 마지막 열의 shift 규칙 때문에 불가능
        """
        m = len(grid)
        n = len(grid[0])
        
        k = k % (m*n)
        ans = []
        deq = collections.deque(range(m*n))
        deq.rotate(k)
        
        while deq:
            idx = deq.popleft()
            ans.append(grid[idx // n][idx % n])
        
        return [ ans[i * n : i * n + n] for i in range(m)]
        
        