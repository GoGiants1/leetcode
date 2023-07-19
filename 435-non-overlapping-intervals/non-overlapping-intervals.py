class Solution:
    def is_overlap(r1: list[int], r2: list[int]):
        if r1[0] > r2[0]:
            r1, r2 = r2, r1
        
        if r1[1] <= r2[0]:
            return False
        return True
    
    def merge(r1: list[int], r2: list[int])->list[int]:
        return [min(r1[0], r2[0]), max(r1[1], r2[1])]

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        last_end = -math.inf
        ans = 0 
        for x, y in intervals:
            if x >= last_end:
                last_end = y
            else:
                ans += 1
            
        return ans