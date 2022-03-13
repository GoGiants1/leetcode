class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # max
        # Greedy, DP, ...
        
        # 직선 개수는 n C 2
        # O(n^2) : 직선 다 찾는거.
        
        # y = ax + b
        
        if len(points) == 1:
            return 1
        
        from fractions import Fraction
        def findGradAndIntercept(p: List[List[int]]) -> (int|None , int):
            [[x1, y1], [x2, y2]] = p
            if x1 == x2:
                grad = None
                intercept = x1
            else:
                grad = Fraction((y1 - y2),(x1 - x2))
                intercept = y1 - grad * x1
            
            return grad, intercept
        
        
        # 2차 방정식
        def findN(n:int):
            # N**2 - N - n = 0
            n *= 2
            
            s = math.sqrt(1 + 4 * n)
            
            x, y = (1 + s) // 2, (1 - s) // 2
            
            return int(max(x, y))
        
        cnt = Counter()
        
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                line = findGradAndIntercept([points[i], points[j]])
                
                cnt[line] += 1

                
        c = cnt.most_common(1)
        
        print(c, cnt)
        return findN(c[0][1])
                    
            
            
            
            
            
        