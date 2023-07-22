class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        out = []
        curr = newInterval[:]

        for i, itv in enumerate(intervals):
            is_overlap = False
            if itv[1] < newInterval[0]:
                out.append(itv)
                continue
            if curr is None:
                out.append(itv)
                continue
            
            if itv[0] <= curr[0] <= itv[1] or itv[0] <= curr[1] <= itv[1]:
                curr[0] = min(itv[0], curr[0])
                curr[1] = max(itv[1], curr[1])
            
            elif curr[1] < itv[0]:
                out.append(curr)
                curr = None
                out.append(itv)
        if curr:
            out.append(curr)
        return out