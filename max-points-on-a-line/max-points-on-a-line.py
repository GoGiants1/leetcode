class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # (b, c)
        cnts = defaultdict(set)
        # x + by + c = 0
        n = len(points)
        
        def calcLine(pt1, pt2)->tuple[int, int]:
            if pt1[0] < pt2[0]:
                pt1, pt2 = pt2, pt1
            a = 1
            b = c = 0
            if pt1[0] == pt2[0]:
                b, c = 0, pt1[0]
            elif pt1[1] == pt2[1]:
                a, b, c = 0, 1, pt1[1]
            else:
                b = (pt2[0] - pt1[0]) / (pt1[1] - pt2[1])
                c = pt1[0] + b * pt1[1]
            cnts[(a,b,c)].add(tuple(pt1))
            cnts[(a,b,c)].add(tuple(pt2))

        for i in range(n):
            for j in range(i+1, n):
                calcLine(points[i], points[j])
 
        if len(cnts) == 0:
            return 1
        mx = 1
        for k, v in cnts.items():
            mx = max(mx, len(v))
        return mx
