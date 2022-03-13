class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        q = deque()
        m = len(flowerbed)
        if flowerbed[0] == 0:
            q.append(0)

        for i in range(1,m):
            if not q:
                if not flowerbed[i]:
                    if not flowerbed[i-1]:
                        q.append(i)
            elif q[-1] == i - 1:
                if flowerbed[i]:
                    q.pop()
                elif not flowerbed[i-1]:
                    q.append(i)
            else:
                if not flowerbed[i] and not flowerbed[i-1]:
                    q.append(i)
        while q and n:
            pos = q.popleft()
            n -= 1
            if q and pos + 1 == q[0]:
                q.popleft()

        return n == 0
    
            

        